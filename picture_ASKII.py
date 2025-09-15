# ascii_cam.py
import cv2
import numpy as np
import shutil
import sys
import time

# Characters from light to dark. Feel free to tweak.
ASCII_CHARS = np.asarray(list(" .:-=+*#%@"))

def frame_to_ascii(gray, max_cols):
    h, w = gray.shape
    # Keep aspect ratio, but compensate because terminal characters are taller than they are wide.
    char_aspect = 0.5  # smaller -> fewer rows (prevents squishing)
    new_w = max(40, min(max_cols, 120))        # cap width to keep it readable
    new_h = max(20, int(h / w * new_w * char_aspect))
    small = cv2.resize(gray, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Map pixel values (0..255) to ASCII_CHARS indices (0..len-1)
    idx = (small.astype(np.float32) / 255.0 * (len(ASCII_CHARS) - 1)).astype(np.int32)
    # Convert to lines of text
    mapped = ASCII_CHARS[idx]
    lines = ["".join(row) for row in mapped]
    return "\n".join(lines)

def main():
    cap = cv2.VideoCapture(0)  # try 1/2 if you have multiple cameras
    if not cap.isOpened():
        print("Could not open webcam.")
        return

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cols = shutil.get_terminal_size((100, 40)).columns
            ascii_art = frame_to_ascii(gray, cols)

            # Print a frame and let the terminal scroll naturally.
            sys.stdout.write(ascii_art + "\n\n")
            sys.stdout.flush()

            # ~100 ms between frames -> ~10 FPS
            time.sleep(0.10)
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()

if __name__ == "__main__":
    main()

