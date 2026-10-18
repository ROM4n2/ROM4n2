#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification harness for GitHub Profile README.
Enforces:
1. Zero emojis in text.
2. Zero raw HTML tags or innerHTML patterns.
3. Valid markdown table balance (matching column counts).
4. All external markdown links resolve to HTTP 200.
"""

import argparse
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# Force UTF-8 stdout to avoid Windows GBK encoding traps
if hasattr(sys.stdout, "reconfigure"):
    getattr(sys.stdout, "reconfigure")(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    getattr(sys.stderr, "reconfigure")(encoding="utf-8", errors="replace")

# Emoji regex covering Unicode symbols, pictographs, transport, emoticons, and supplemental symbols
EMOJI_PATTERN = re.compile(
    r"["
    r"\U0001F600-\U0001F64F"  # Emoticons
    r"\U0001F300-\U0001F5FF"  # Misc Symbols and Pictographs
    r"\U0001F680-\U0001F6FF"  # Transport and Map
    r"\U0001F700-\U0001F77F"  # Alchemical Symbols
    r"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    r"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    r"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    r"\U0001FA00-\U0001FA6F"  # Chess Symbols
    r"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    r"\U00002702-\U000027B0"  # Dingbats
    r"\U000024C2-\U0001F251"  # Enclosed Alphanumeric Supplement
    r"]",
    flags=re.UNICODE,
)

RAW_HTML_PATTERN = re.compile(
    r"</?(?:div|span|p|a|table|thead|tbody|tr|th|td|img|h[1-6]|ul|ol|li|script|iframe|style|b|i|strong|em)\b[^>]*>",
    flags=re.IGNORECASE,
)

MARKDOWN_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?://[^\s\)]+)\)")
TABLE_ROW_PATTERN = re.compile(r"^\s*\|(.+)\|\s*$")


def strip_code_blocks(content: str) -> list[tuple[int, str]]:
    """
    Return a list of (line_number, line_text) outside of fenced code blocks.
    Lines are 1-indexed.
    """
    lines = content.splitlines()
    filtered = []
    in_code_block = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        filtered.append((idx, line))

    return filtered


def check_emojis(lines: list[tuple[int, str]]) -> list[str]:
    violations = []
    for line_num, line in lines:
        match = EMOJI_PATTERN.search(line)
        if match:
            char = match.group(0)
            violations.append(f"Line {line_num}: Disallowed emoji '{char}' detected in '{line.strip()}'")
    return violations


def check_raw_html(lines: list[tuple[int, str]]) -> list[str]:
    violations = []
    for line_num, line in lines:
        # Ignore markdown inline code `...`
        sanitized = re.sub(r"`[^`]*`", "", line)
        match = RAW_HTML_PATTERN.search(sanitized)
        if match:
            tag = match.group(0)
            violations.append(f"Line {line_num}: Disallowed raw HTML tag '{tag}' detected in '{line.strip()}'")
    return violations


def check_table_balance(lines: list[tuple[int, str]]) -> list[str]:
    violations = []
    in_table = False
    expected_cols = None
    table_start_line = None

    for line_num, line in lines:
        m = TABLE_ROW_PATTERN.match(line)
        if not m:
            in_table = False
            expected_cols = None
            continue

        raw_inner = m.group(1)
        # Split by unescaped pipes
        cols = [col.strip() for col in re.split(r"(?<!\\)\|", raw_inner)]
        col_count = len(cols)

        if not in_table:
            in_table = True
            expected_cols = col_count
            table_start_line = line_num
            continue

        # Check if separator row (e.g. |---|---|)
        is_sep = all(re.match(r"^:?-+:?$", c) for c in cols if c)
        if is_sep:
            if col_count != expected_cols:
                violations.append(
                    f"Line {line_num}: Table separator column mismatch (expected {expected_cols}, got {col_count}) in table starting at line {table_start_line}"
                )
            continue

        if col_count != expected_cols:
            violations.append(
                f"Line {line_num}: Table row column count mismatch (expected {expected_cols}, got {col_count}) in table starting at line {table_start_line}"
            )

    return violations


def check_links(lines: list[tuple[int, str]], skip_network: bool = False) -> list[str]:
    violations = []
    if skip_network:
        return violations

    urls_to_check = set()
    url_to_first_line = {}

    for line_num, line in lines:
        for match in MARKDOWN_LINK_PATTERN.finditer(line):
            url = match.group(2)
            urls_to_check.add(url)
            if url not in url_to_first_line:
                url_to_first_line[url] = line_num

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    for url in sorted(urls_to_check):
        line_num = url_to_first_line[url]
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                code = resp.getcode()
                if code not in (200, 301, 302, 307, 308):
                    violations.append(f"Line {line_num}: Link '{url}' returned HTTP {code}")
        except urllib.error.HTTPError as e:
            violations.append(f"Line {line_num}: Link '{url}' returned HTTP error {e.code}")
        except urllib.error.URLError as e:
            violations.append(f"Line {line_num}: Link '{url}' connection failed: {e.reason}")
        except Exception as e:
            violations.append(f"Line {line_num}: Link '{url}' error: {e}")

    return violations


def verify_markdown_file(file_path: Path, skip_network: bool = False) -> list[str]:
    if not file_path.exists():
        return [f"File '{file_path}' does not exist."]

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Failed to read file '{file_path}': {e}"]

    if not content.strip():
        return [f"File '{file_path}' is empty."]

    lines = strip_code_blocks(content)
    violations = []
    violations.extend(check_emojis(lines))
    violations.extend(check_raw_html(lines))
    violations.extend(check_table_balance(lines))
    violations.extend(check_links(lines, skip_network=skip_network))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify markdown profile against strict DFS invariants.")
    parser.add_argument("file", help="Path to markdown file to verify")
    parser.add_argument("--skip-network", action="store_true", help="Skip HTTP link verification")
    args = parser.parse_args()

    target = Path(args.file)
    violations = verify_markdown_file(target, skip_network=args.skip_network)

    if violations:
        print(f"FAILED: {len(violations)} violation(s) found in {target}:")
        for v in violations:
            print(f"  - {v}")
        return 1

    print(f"PASSED: All checks green for {target}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
