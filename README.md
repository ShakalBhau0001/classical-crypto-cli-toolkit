# 🗝️ Classical-Crypto-CLI-Toolkit

### Classical Cryptography Command-Line Toolkit

**Classical-Crypto-CLI-Toolkit** is a **Python-based command-line tool** for experimenting with classical ciphers and cryptanalysis.  
It is designed for **students, security enthusiasts, and developers** who want to learn or demonstrate classical encryption techniques in a terminal environment.

All operations are **local**, ensuring **full offline use and privacy**.

---

## 🖥️ GUI Alternative

For beginners or users who prefer a graphical interface:

👉 A future **GUI version** could provide the same core features with an easy-to-use desktop interface.

> 🔗 GUI Repository: **[Classical-Crypto-GUI-Toolkit](https://github.com/ShakalBhau0001/classical-crypto-gui-toolkit)**

---

## ✨ Key Principles

1. **Learning-focused** – ideal for beginners exploring cryptography  
2. **CLI-centric** – intuitive, alias-supported commands  
3. **Modular architecture** – separates cipher logic from CLI interface  

This toolkit is **educational, yet fully functional**, with each cipher and attack independently usable.

---

## 🧩 Included Modules

### 🔐 Classical Ciphers

- **Caesar Cipher** (`caesar`, `c`) – shift-based substitution
- **Playfair Cipher** (`playfair`, `pf`) – digraph-based substitution
- **Rail Fence Cipher** (`rail_fence`, `rf`, `rail`) – transposition cipher
- **Row Column Cipher** (`row_column`, `rc`, `row`) – columnar transposition

### 🧪 Attacks

- **Caesar Brute Force** (`attack c`, `atk c`) – tries all possible shifts
- **Rail Fence Brute Force** (`attack rf`, `atk rf`) – tries multiple rail numbers

---

## 📁 Project Structure

```bash
classical-crypto-cli-toolkit/
│
├── core/
│   ├── __init__.py
│   ├── utils.py
│   ├── ciphers/
│   │   ├── __init__.py
│   │   ├── caesar.py
│   │   ├── rail_fence.py
│   │   ├── row_column.py
│   │   └── playfair.py
│   └── attacks/
│       ├── __init__.py
│       ├── caesar_brute.py
│       └── rail_fence_brute.py
│
├── cli/
│   ├── __init__.py
│   ├── parser.py
│   └── controller.py
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

> ✔ Core logic and CLI interface are strictly separated for maintainability and learning.

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ShakalBhau0001/classical-crypto-cli-toolkit.git
cd classical-crypto-cli-toolkit
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Help Command

```bash
python main.py --help
```

---

## 🧪 CLI Usage Examples

> **Syntax**

> ```bash
> python main.py <cipher> [options]
> python main.py <attack> [options]
> ```

### 🔐 Caesar Cipher

**Encrypt**

```bash
python main.py caesar -e "HELLO WORLD" -s 3
python main.py c -e "HELLO WORLD" -s 3
```

**Decrypt**

```bash
python main.py caesar -d "KHOOR ZRUOG" -s 3
python main.py c -d "KHOOR ZRUOG" -s 3
```

---

### 🔐 Playfair Cipher

**Encrypt**

```bash
python main.py playfair -e "HELLO WORLD" -k KEYWORD
python main.py pf -e "HELLO WORLD" -k KEYWORD
```

**Decrypt**

```bash
python main.py playfair -d "GYIZSCOKCFBU" -k KEYWORD
python main.py pf -d "GYIZSCOKCFBU" -k KEYWORD
```

---

### 🔐 Rail Fence Cipher

**Encrypt**

```bash
python main.py rail_fence -e "HELLO WORLD" -r 3
python main.py rf -e "HELLO WORLD" -r 3
python main.py rail -e "HELLO WORLD" -r 3
```

**Decrypt**

```bash
python main.py rail_fence -d "HOLELWRDLO" -r 3
python main.py rf -d "HOLELWRDLO" -r 3
python main.py rail -d "HOLELWRDLO" -r 3
```

---

### 🔐 Row Column Cipher

**Encrypt**

```bash
python main.py row_column -e "HELLO WORLD" -k KEYWORD
python main.py rc -e "HELLO WORLD" -k KEYWORD
python main.py row -e "HELLO WORLD" -k KEYWORD
```

**Decrypt**

```bash
python main.py row_column -d "OXELHROXWXLXLD" -k KEYWORD
python main.py rc -d "OXELHROXWXLXLD" -k KEYWORD
python main.py row -d "OXELHROXWXLXLD" -k KEYWORD
```

---

### 🧪 Cipher Attacks

**Caesar Brute Force**

```bash
python main.py attack c "KHOOR ZRUOG"
python main.py atk c "KHOOR ZRUOG"
```

**Rail Fence Brute Force**

```bash
python main.py attack rf "HOLELWRDLO" --max-rails 10
python main.py atk rf "HOLELWRDLO" --max-rails 10
```

---

## 🆘 Help Commands

**Global help**

```bash
python main.py --help
```

**Module-specific help**

```bash
python main.py caesar --help
python main.py playfair --help
python main.py rail_fence --help
python main.py row_column --help
python main.py attack --help
```

---

## ⚠️ Important Notes

- Modules and attacks are **not flags**  
- Module name must come **immediately after `main.py`**  
- Flags are **case-sensitive**  
- Short and long flags both supported  
- Encrypt = input → output  
- Decrypt = output → original input

---

## 📦 requirements.txt

```txt
cryptography
```

---

## ⚠️ Security Disclaimer

This toolkit is **educational and research-focused**.  
It uses classical ciphers and is **not suitable for modern secure communication**.  
Handle sensitive data with caution.

---

## 🛣️ Roadmap

- Frequency analysis tools
- Batch processing support  
- Linux & macOS packaging  
- PyInstaller standalone binaries  

---

## 🪪 Author

> Developer: **Shakal Bhau**

> GitHub: **[ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

> “Classical ciphers teach discipline before modern encryption.”
