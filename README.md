# QR Code Generator (Python) — Biox Systems Assignment

A simple command-line tool that generates a QR code (PNG) when you provide a URL.

## Features
- Validates URL format (must include `http://` or `https://`)
- Configurable error-correction levels (`L`, `M`, `Q`, `H`)
- Adjustable box size and border width
- Saves output to a PNG file

## Project Structure
```
qr_code_generator/
├── qr_generator.py
├── requirements.txt   # Manifest file
├── manifest.txt       # Project metadata
├── .gitignore
└── QR_Code_Generator_Report.rtf   # Word-compatible report template
```

## Getting Started

### 1) Create and activate a virtual environment
**Windows (PowerShell):**
```powershell
cd "C:\Users\<YOUR_USER>\Downloads\QR code generator"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
> If you see an execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

**Windows (Command Prompt):**
```cmd
cd "C:\Users\<YOUR_USER>\Downloads\QR code generator"
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the app
```bash
python qr_generator.py --url "https://bioxsystems.com" --out output/bioxsystems_qr.png --ec H --box-size 10 --border 4
```
You should see:
```
✅ QR code saved to: .../output/bioxsystems_qr.png
```

### 4) Take a screenshot for your report
- Open the generated PNG (`output/bioxsystems_qr.png`) and take a screenshot of the image viewer showing the QR.
- Paste that screenshot into **QR_Code_Generator_Report.rtf** where indicated.

## GitHub Instructions
1. Create a new repo on GitHub (e.g., `qr-code-generator-biox`).
2. In your project folder:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: QR Code Generator"
   git branch -M main
   git remote add origin https://github.com/<your-username>/qr-code-generator-biox.git
   git push -u origin main
   ```
3. Copy your repository URL and include it in your report.

## Example Commands
- Minimum options:
  ```bash
  python qr_generator.py --url "https://example.com"
  ```
  Saves to `output/qr.png` with default settings.

## Troubleshooting
- **`ModuleNotFoundError: No module named 'qrcode'`**
  Run: `pip install -r requirements.txt`
- **Spaces in folder name (Windows)**: Always quote the path: `cd "C:\Users\...\QR code generator"`
- **PowerShell script policy**: Use `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` and retry activation.

---
© 2025 Biox Systems Assignment — QR Code Generator.
