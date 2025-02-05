import os
import hashlib
import time

def calculate_hash(file_path):
    """Calculates the hash value of a given file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def monitor_file(file_path, interval=10):
    """Monitors a specific file for changes in hash values."""
    file_hash = calculate_hash(file_path)
    print(f"Initial hash: {file_hash}")
    while True:
        try:
            new_hash = calculate_hash(file_path)
            if file_hash != new_hash:
                print(f"File changed: {file_path}")
                print(f"New hash: {new_hash}")
                file_hash = new_hash
            else:
                print("No change detected.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    file_to_monitor = "/home/krishn/Task/Choco.txt"
    print(f"Monitoring file: {file_to_monitor}")
    monitor_file(file_to_monitor)
