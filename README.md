# otpgen.py 🛡️🔐

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey?logo=apple)](https://www.apple.com/macos/)
[![Linux](https://img.shields.io/badge/platform-Linux-yellow?logo=linux)](https://www.kernel.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A secure, CLI-based 2FA TOTP/HOTP manager written in Python. Inspired by [`otpgen.sh`](https://github.com/shatadru/otpgen.sh), this version brings modularity, encryption, platform-awareness, and QR support.

---

## 📦 Features

- 🔐 Encrypted keystore using `cryptography.fernet`
- 🖼️ Add 2FA keys from QR code images (TOTP & HOTP)
- 🧾 Export/import in CSV or JSON
- 📋 Clipboard integration (with fallback)
- 📸 QR generation with auto-preview (if not headless)
- 🧠 Platform-aware setup (Linux/macOS)
- 🧪 Unit tested & modular
- 🧰 Auto-installs appropriate dependencies based on platform

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shatadru/otpgen.py.git
cd otpgen.py
```

### 2. Install Requirements

> 🧠 otpgen auto-selects the right requirements file if you use `-i` or `--install`.

Alternatively, you can manually install dependencies:

#### For Linux:
```bash
pip install -r requirements-linux.txt
```

#### For macOS:
```bash
brew install zbar
pip install -r requirements-macos.txt
```

---

## 🛠️ Usage

```bash
# First-time install
python otpgen.py -i

# Add key from QR code image
python otpgen.py -a path/to/qr.png

# Generate OTP
python otpgen.py -g 1

# List saved keys
python otpgen.py -l

# Remove a key
python otpgen.py -r 1

# Export keys
python otpgen.py --export json
python otpgen.py --export csv

# Import keys
python otpgen.py --import keys.json --import-format json
```

Use `--no-clip` to disable clipboard copy for OTPs in headless or minimal systems.

---

## 🧪 Run Tests

```bash
python -m unittest test.py
```

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Created with ❤️ by [Shatadru Bandyopadhyay](https://github.com/shatadru)
