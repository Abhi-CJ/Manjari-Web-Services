#!/usr/bin/env python
"""
Asset minification script for the Manjari Taxi project.
Minifies CSS and JavaScript source files for production use.
Handles inlining of @import CSS files.

Usage:
    python scripts/minify_assets.py
"""
import re
import os
from typing import Optional

def inline_css_imports(css_content: str, base_dir: str) -> str:
    """Find @import url("..."); and inline the content."""
    def replacer(match):
        import_path = match.group(1).strip()
        full_path = os.path.join(base_dir, import_path)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        return match.group(0)
    
    # Match @import url("path/to/file.css"); or @import url('...');
    pattern = re.compile(r'@import\s+url\([\'"]?([^\'"\)]+)[\'"]?\)\s*;')
    return pattern.sub(replacer, css_content)

def minify_css(css_content: str, base_dir: str = None) -> str:
    """Inline imports, remove comments, collapse whitespace."""
    if base_dir:
        css_content = inline_css_imports(css_content, base_dir)
        
    css = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    css = re.sub(r'\s*([:;{},])\s*', r'\1', css)
    css = re.sub(r'\s+', ' ', css)
    return css.strip()

def minify_js(js_content: str, base_dir: str = None) -> str:
    """Remove comments, collapse whitespace, and strip JS for production."""
    js = re.sub(r'//.*', '', js_content)
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    js = re.sub(r'\s*([=+\-*/{}()\[\],;:<>!|&])\s*', r'\1', js)
    js = re.sub(r'\s+', ' ', js)
    return js.strip()

def _process_file(src: str, dest: str, minifier, label: str, css_base_dir: str = None) -> Optional[str]:
    """Read source file, minify, and write to destination."""
    if not os.path.exists(src):
        print(f"  [SKIP] {label} source not found: {src}")
        return None

    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    minified = minifier(content, css_base_dir) if css_base_dir else minifier(content)

    with open(dest, 'w', encoding='utf-8') as f:
        f.write(minified)

    summary = f"  [OK] {label}: {len(content):,} -> {len(minified):,} bytes"
    print(summary)
    return summary

def main() -> None:
    """Entry point: minify CSS and JS assets."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_dir = os.path.join(base_dir, 'src', 'css')

    print("Minifying assets...")

    _process_file(
        src=os.path.join(css_dir, 'style.css'),
        dest=os.path.join(css_dir, 'style.min.css'),
        minifier=minify_css,
        label="CSS",
        css_base_dir=css_dir
    )

    _process_file(
        src=os.path.join(base_dir, 'src', 'js', 'main.js'),
        dest=os.path.join(base_dir, 'src', 'js', 'main.min.js'),
        minifier=minify_js,
        label="JS"
    )

    print("Done.")

if __name__ == '__main__':
    main()
