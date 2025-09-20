# main.py
import sys
from pathlib import Path
import segno

DEFAULT_URL = "https://github.com/Bhawesh-03/Qr-code-generator"

def normalize(u: str) -> str:
    u = (u or "").strip()
    if not u:
        return DEFAULT_URL
    if not u.startswith(("http://", "https://")):
        u = "https://" + u
    return u

def make_qr(data: str):
    out_dir = Path(__file__).resolve().parent
    png = out_dir / "qrcode_repo.png"
    svg = out_dir / "qrcode_repo.svg"

    print("Encoding URL:", data)
    print("Saving to:", png, "and", svg, sep="\n")

    qr = segno.make(data, error="h")
    qr.save(png, scale=10)
    qr.save(svg, scale=5)
    print("Done.")

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else input(f"Enter URL [{DEFAULT_URL}]: ")
    make_qr(normalize(arg))