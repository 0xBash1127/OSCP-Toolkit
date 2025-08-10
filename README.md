# OSCP Toolkit

Quick helper for OSCP-style labs:

* File transfer payloads (PowerShell / curl / wget)
* Ligolo-NG setup + agent delivery
* Reverse shell generator (Docker)

> **For authorized testing only.**

## Requirements

* Python 3.8+
* `pip install pyfiglet pyperclip colorama`
* `tmux`
* `docker` (for reverse shell)
* (Optional) Ligolo-NG in `/opt/ligolo-ng`
* Linux/macOS recommended

## Install

```bash
git clone https://github.com/0xBash1127/OSCP-Toolkit.git
cd OSCP-toolkit
pip install -r requirements.txt
chmod +x oscp_toolkit.py
```

`requirements.txt`

```
pyfiglet
pyperclip
colorama
```

## Run

```bash
./oscp_toolkit.py
```

Menu:

```
[1] File Transfer Payload
[2] Ligolo setup
[3] Reverse Shell
[4] Exit
```

**File Transfer** → copies one-liner & starts HTTP server
**Ligolo setup** → runs proxy, stages agent for download
**Reverse Shell** → launches generator on `http://127.0.0.1`
