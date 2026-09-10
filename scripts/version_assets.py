#!/usr/bin/env python3
"""Refresh content-based asset URLs, or verify them with --check.

The site remains plain static HTML. Run after editing CSS, JavaScript or the icon
so a newly deployed page cannot reuse an older browser-cached asset URL.
"""
import argparse
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ('assets/site.css', 'assets/site.js', 'assets/favicon.svg') + tuple(
    path.relative_to(ROOT).as_posix()
    for path in sorted((ROOT / 'assets/projects').glob('*.jpg'))
) + tuple(
    path.relative_to(ROOT).as_posix()
    for path in sorted((ROOT / 'assets/cv').glob('*.pdf'))
)


def versioned_html(source):
    for asset in ASSETS:
        digest = hashlib.sha256((ROOT / asset).read_bytes()).hexdigest()[:16]
        pattern = r'((?:href|src)=")' + re.escape(asset) + r'(?:\?[^"\s]*)?(")'
        source, count = re.subn(pattern, lambda match: match[1] + asset + '?v=' + digest + match[2], source)
        if count < 1:
            raise ValueError(f'Expected at least one reference to {asset}, found {count}')
    return source


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if any asset URL is stale; do not edit files.')
    args = parser.parse_args()
    page = ROOT / 'index.html'
    current = page.read_text(encoding='utf-8')
    updated = versioned_html(current)
    if args.check:
        if current != updated:
            parser.exit(1, 'Asset versions are stale. Run: python3 scripts/version_assets.py\n')
        print('All asset versions match their file contents.')
    elif current != updated:
        page.write_text(updated, encoding='utf-8')
        print('Updated stylesheet, script and icon URLs with content hashes.')
    else:
        print('Asset versions are already current.')


if __name__ == '__main__':
    main()
