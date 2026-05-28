# 🔒 Caesar Cipher Tool

A Python desktop app that encrypts and decrypts text using the Caesar Cipher — one of the oldest and most well-known encryption techniques in cryptography.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![Cryptography](https://img.shields.io/badge/Cryptography-Beginner-red?style=for-the-badge)

---

## 📸 Screenshot

![Caesar Cipher Screenshot](Caesar%20Cipher%20Screen%20Shot%20.png)

---

## 💡 What It Does

Type any text, choose a shift key (0–25), and the app instantly shows you both the encrypted ciphertext and the decrypted output side by side. Symbols, spaces, and numbers stay unchanged — only letters are shifted.

**Example with shift = 3:**
```
Plaintext:  Hello World
Ciphertext: Khoor Zruog
Decrypted:  Hello World
```

---

## 🔑 How Caesar Cipher Works

Each letter in the text is shifted forward by the key number in the alphabet:
- `A + 3 = D`
- `Z + 3 = C` (wraps around)

Decryption simply shifts in the opposite direction.

---

## ✨ Features

- ✅ Encrypt any text with a custom shift key (0–25)
- ✅ Decrypt back to original automatically
- ✅ Ciphertext and decrypted output shown side by side
- ✅ Handles uppercase, lowercase, spaces and symbols
- ✅ Status bar shows key used and characters processed
- ✅ Press Enter to run

---

## 🚀 How to Run

```bash
git clone https://github.com/G1H6-bit/caesar-cipher.git
cd caesar-cipher
python caesar_cipher.py
```

> Requires Python 3.x — no extra libraries needed

---

## 👤 Author

**Abdelrahman Ashraf**
- GitHub: [@G1H6-bit](https://github.com/G1H6-bit)
- LinkedIn: [Abdelrahman Ashraf](https://www.linkedin.com/in/abdelrahman-ashraf-39169035a/)

---

## 📄 License

MIT License
