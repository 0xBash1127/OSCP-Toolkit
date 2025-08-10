Got it — here’s a **short, straight-to-the-point README** with only what’s needed.

---

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
git clone <repo-url>
cd <repo>
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

---

Do you want me to **also shrink your code** so it’s just the essentials without the extra complexity? That would make it match this short README perfectly.
