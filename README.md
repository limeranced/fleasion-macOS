# Fleasion for macOS (Unofficial)

Fleasion is a Roblox asset replacement tool that allows users to modify and override Roblox textures, sounds, and more—now fully working on macOS.

This is a community rework for **macOS compatibility** based on the original Fleasion project.

---

## ✅ Features

* Auto-downloads and manages asset packs (e.g., for Phantom Forces, AR2, DaHood).
* Replaces textures, sounds, skyboxes, and other cached files.
* Compatible with macOS filesystem and dynamic cache paths.

---

## 🧠 How It Works

Roblox stores temporary cache files (like textures and sounds) in a unique directory under:

```
/private/var/folders/.../T/Roblox/http-wob/
```

This fork detects that folder dynamically and replaces content based on UUID-named files Roblox loads.

---

## 📦 Folder Structure

```sh
Fleasion_macOS/
├── assets/                  # Game packs and community files
├── storage/                 # Cached file references, user preferences
├── autoupdate.py            # Downloads and installs asset packs
├── cached_files_downloader.py
├── fleasion.py              # Core logic (imported by main.py)
├── main.py                  # Main CLI entry point
├── rbx-storage.db           # Replacement rules database
├── requirements.txt         # Python dependencies
├── run.sh                   # Optional CLI launcher
├── README.md
```

---

## 🚀 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/limeranced/fleasion-macOS.git
cd fleasion-macOS
```

### 2. Install Dependencies

Make sure Python 3.9+ is installed. Then:

```bash
pip3 install -r requirements.txt
```

### 3. Run Fleasion

```bash
python3 main.py
```

### 4. Use Auto-Updater

```bash
python3 autoupdate.py
```

> Downloads latest asset bundles and replacement files

---

## 📁 Cache Path Detection on macOS

On macOS, asset files are dynamically loaded into:

```bash
/private/var/folders/**/<temp>/T/Roblox/http-wob/
```

This app auto-detects and writes replacements there using `psutil`, `os`, and UUID monitoring.

---

## 🔐 Permissions

You may need to grant Full Disk Access to your Terminal or IDE to modify Roblox cache files.

System Settings → Privacy & Security → Full Disk Access → Add Terminal

---

## 🧪 Verify It's Working

You can run the monitor tool to watch Roblox load asset UUIDs:

```bash
./verify_asset_usage.sh
```

It confirms the game is loading patched assets like `cached_files/...` into memory.

---

## ❗ Disclaimer

I made this mainly for myself but why not let others. If this breaks or anything dont blame the fleasion team as i am just a random person who decided ot make this. 

pls give credit to the original Fleasion creators for the idea and architecture.

> This tool is not intended for abuse, cheating, or game exploitation. Use responsibly. Or dont, i dont care

---

## 🧰 Troubleshooting

* Run `python3 autoupdate.py` if you get missing folder errors.
* Make sure Roblox is launched before running `main.py` for changes to take effect.
* Run the game fully and allow assets to be cached before launching Fleasion.

---

## 🙌 Credits

* macOS compatibility and repackaging by [@ver6al](https://discord.com/users/1121335931656478740) (GitHub: [limeranced](https://github.com/limeranced))
* Original project by Tyler @8ar and contributors — credits and license remain theirs

---

## 📎 License

MIT License

