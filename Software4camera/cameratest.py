import cv2
import time
import os
from datetime import datetime

def capture_every_n_seconds(n, base_folder="Software4camera/Pics"):

    cap = cv2.VideoCapture(2)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    try:
        while True:
            now = datetime.now()
            # e.g. "2025-05-27_14"
            hour_folder = now.strftime("%Y-%m-%d_%H")
            folder_path = os.path.join(base_folder, hour_folder)
            os.makedirs(folder_path, exist_ok=True)

            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            # e.g. "2025-05-27_14-23-05.jpg"
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{timestamp}.jpg"
            filepath = os.path.join(folder_path, filename)

            # Save as JPEG
            cv2.imwrite(filepath, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
            print(f"Saved {filepath}")

            time.sleep(n)
    finally:
        cap.release()

if __name__ == "__main__":
    # capture every 3 seconds
    capture_every_n_seconds(3)
