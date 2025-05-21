# Simple Port Scanner 🔍

A basic Python-based TCP port scanner that scans for open ports on a given target IP or domain.

---

## 🔥 Features

- Scans common or custom port ranges
- Supports hostname and IP input
- Displays open ports in real time
- Fast and lightweight tool for basic recon

---

## 📁 Project Structure

```
simple-port-scanner/
├── port_scanner.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/simple-port-scanner.git
cd simple-port-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📦 Requirements

- Python 3.7+
- rich (for colored CLI output)

To install manually:

```bash
pip install rich
```

---

## 🧪 Usage

```bash
python port_scanner.py
```

Input the target when prompted:

```
Enter target IP or hostname: scanme.nmap.org
```

The script will display a list of open ports like:

```
[+] Port 22 is open
[+] Port 80 is open
```

---

## ⚠️ Legal Warning

Use this tool only on **authorized networks**. Unauthorized scanning may violate laws or terms of service.

---

## 🧾 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

- GitHub: [@muuhsi](https://github.com/muuhsi)
