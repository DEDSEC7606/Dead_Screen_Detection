from mss import mss
from PIL import Image
from datetime import datetime
import time
import os

SAVE_DIR = "auto_screens"
os.makedirs(SAVE_DIR, exist_ok=True)

INTERVAL = 60

def take_screenshot():
    
    ts = datetime.now().strftime("%H:%M:%S_%d|%m|%Y")
    path = os.path.join(SAVE_DIR, f"{ts}.png")

    try:
        with mss() as sct:
            monitor = sct.monitors[0]
            img = sct.grab(monitor)

            img_pil = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            img_pil.save(path)

        print(f"[+] Screenshot saved: {path}")

    except Exception as e:
        print("[ERROR] Could not capture screenshot:", e)

if __name__ == "__main__":
    print("[*] Auto Screenshot Capture Running...")
    print(f"[*] Saving every {INTERVAL} seconds")
    print(f"[*] Saving to: {SAVE_DIR}")

    try:
        while True:
            take_screenshot()
            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")