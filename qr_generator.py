#!/usr/bin/env python3
"""
QR Code Generator - Biox Systems Assignment

Description:
    Simple command-line application that generates a QR code PNG from a URL.
    Uses the 'qrcode' library (with Pillow) to render the image.

Usage:
    python qr_generator.py --url https://example.com --out output/qr_example.png --ec H --box-size 10 --border 4

Best Practices Included:
    - Argument parsing and help text
    - URL validation
    - Error handling with clear messages and non-zero exit codes on failure
    - Constants for error-correction mapping
    - Docstrings and comments for maintainability

Author: Bhawesh Shrestha
"""
import argparse
import sys
import os
from urllib.parse import urlparse

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
except Exception as e:
    print("The 'qrcode' package is required. Install dependencies with:\n  pip install -r requirements.txt", file=sys.stderr)
    raise

# Map human-friendly EC codes to qrcode constants
EC_MAP = {
    'L': ERROR_CORRECT_L,  # Recovers ~7% of data
    'M': ERROR_CORRECT_M,  # Recovers ~15% of data
    'Q': ERROR_CORRECT_Q,  # Recovers ~25% of data
    'H': ERROR_CORRECT_H,  # Recovers ~30% of data
}

def is_valid_url(url: str) -> bool:
    """Basic validation to ensure the URL includes a scheme and netloc."""
    try:
        p = urlparse(url)
        return p.scheme in ('http', 'https') and bool(p.netloc)
    except Exception:
        return False

def generate_qr(url: str, outfile: str, ec: str = 'M', box_size: int = 10, border: int = 4) -> str:
    """Generate and save a QR code PNG for the provided URL."""
    if not is_valid_url(url):
        raise ValueError(f"Invalid URL: {url}. Make sure it starts with http:// or https://")

    ec_level = EC_MAP.get(ec.upper(), EC_MAP['M'])

    # Configure the QR Code
    qr = qrcode.QRCode(
        version=None,               # Let library choose minimal version that fits the data
        error_correction=ec_level,
        box_size=box_size,          # Pixel size of each module
        border=border,              # Border width in modules
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Ensure output directory exists
    outdir = os.path.dirname(outfile) or "."
    os.makedirs(outdir, exist_ok=True)

    img.save(outfile)
    return os.path.abspath(outfile)

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Generate a QR code PNG from a URL.")
    parser.add_argument("--url", required=True, help="URL to encode (must include http:// or https://)")
    parser.add_argument("--out", default="output/qr.png", help="Output PNG path (default: output/qr.png)")
    parser.add_argument("--ec", default="M", choices=list(EC_MAP.keys()), help="Error correction level: L, M, Q, H (default: M)")
    parser.add_argument("--box-size", type=int, default=10, help="Pixel size of each QR box/module (default: 10)")
    parser.add_argument("--border", type=int, default=4, help="Border width in modules (default: 4)")
    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    try:
        path = generate_qr(args.url, args.out, args.ec, args.box_size, args.border)
        print(f"✅ QR code saved to: {path}")
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
