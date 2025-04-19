# 🔐 otpgen (Python CLI Edition)

[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS-blue)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A powerful, portable CLI tool for managing Time-based (TOTP) and Counter-based (HOTP) 2FA secrets—originally inspired by `otpgen.sh`, now reimagined in Python.

---

## ✨ Features

- 🔐 Secure encrypted keystore using AES-256 (via `cryptography`)
- 🔍 Add TOTP/HOTP secrets by scanning QR code images
- 🧾 List, generate, remove, import/export 2FA keys
- 📋 Clipboard support (platform-aware, fallback safe)
- 📸 Generate and open QR codes from stored secrets
- 🧪 Tested with both **Linux** and **macOS**

---

## ⚙️ Installation

### 📦 1. Clone the repo

```bash
git clone https://github.com/yourname/otpgen-cli
cd otpgen-cli
```

### 🐍 2. Install dependencies (platform-aware)

Use the built-in CLI support:

```bash
python3 otpgen.py --install
```

This auto-selects:
- `requirements-linux.txt` (Linux)
- `requirements-macos.txt` (macOS)

Or install manually:

```bash
# For Linux
pip install -r requirements-linux.txt

# For macOS (uses pyzbar + Pillow)
brew install zbar
pip install -r requirements-macos.txt
```

---

## 🚀 Usage

### 🛠 Initialize a keystore

```bash
python3 otpgen.py --install
```

### ➕ Add a 2FA key (from QR code image)

```bash
python3 otpgen.py --add-key myqr.png
```

### 📋 List all keys

```bash
python3 otpgen.py --list-key
```

### 🔢 Generate OTP for a key

```bash
python3 otpgen.py --gen-key 1
```

Use `--no-clip` if you're in a headless session or clipboard fails:

```bash
python3 otpgen.py --gen-key 1 --no-clip
```

### 🧽 Remove a key

```bash
python3 otpgen.py --remove-key 1
```

---

## 📤 Export/Import

### Export as JSON or CSV

```bash
python3 otpgen.py --export json
python3 otpgen.py --export csv
```

### Import from JSON or CSV

```bash
python3 otpgen.py --import keys.json --import-format json
```

---

## 📸 Generate QR code from a stored key

```bash
python3 otpgen.py --qr 1
```

This opens the image automatically (unless in headless mode).

---

## 🧪 Test QR Code Example

Generate one manually:

```python
import qrcode
uri = "otpauth://totp/test@example.com?secret=JBSWY3DPEHPK3PXP&issuer=otpgen-test"
qrcode.make(uri).save("otpgen-test-qr.png")
```

Add it:

```bash
python3 otpgen.py --add-key otpgen-test-qr.png
```

---

## 📎 Clipboard Notes

- Linux: install `xclip`, `xsel`, or `wl-clipboard`
- macOS: ensure `pbcopy` is available (`xcode-select --install`)
- Fallbacks and `--no-clip` supported

---

## 🧪 Testing

```bash
python3 -m unittest test.py
```

---

## 📝 License

MIT © [Shatadru Bandyopadhyay](https://github.com/shatadru)