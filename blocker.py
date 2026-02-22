import time
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
TARGET_DIR = "./demo/docs"
THRESHOLD_FILES = 5          # Number of files
THRESHOLD_SECONDS = 10       # Time window
# ---------------------

class RansomwareDetector(FileSystemEventHandler):
    def __init__(self):
        self.change_log = []

    def on_modified(self, event):
        if not event.is_directory:
            current_time = time.time()
            self.change_log.append(current_time)
            
            # Remove timestamps older than our window
            self.change_log = [t for t in self.change_log if current_time - t <= THRESHOLD_SECONDS]

            print(f"[!] Activity detected: {event.src_path} | Window count: {len(self.change_log)}")

            if len(self.change_log) >= THRESHOLD_FILES:
                self.trigger_alert()

    def trigger_alert(self):
        print("\n" + "!"*40)
        print("ALERT: RANSOMWARE BEHAVIOR DETECTED!")
        print(f"More than {THRESHOLD_FILES} changes in {THRESHOLD_SECONDS}s.")
        print("ACTION: Locking directory and halting simulation...")
        print("!"*40 + "\n")
        
        # In a real tool, you'd kill the PID or revoke write permissions
        # For a demo, we'll just exit the script to 'stop' the monitor
        os._exit(1)

if __name__ == "__main__":
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"[*] Created target directory: {TARGET_DIR}")

    event_handler = RansomwareDetector()
    observer = Observer()
    observer.schedule(event_handler, TARGET_DIR, recursive=False)
    
    print(f"[*] Monitoring started on: {TARGET_DIR}")
    print(f"[*] Threshold: {THRESHOLD_FILES} changes in {THRESHOLD_SECONDS}s")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()