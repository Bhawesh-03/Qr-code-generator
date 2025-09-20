import segno
import sys

def make_qr(data: str, png="qrcode.png", svg="qrcode.svg"):
    qr = segno.make(data.strip())
    qr.save(png, scale=8)   # PNG
    qr.save(svg, scale=4)   # SVG (vector)
    print(f"Saved {png} and {svg}")

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter URL: https://example.com ").strip()
    make_qr(url)

