import cv2
import os

os.makedirs("assets/scans", exist_ok=True)

cap = cv2.VideoCapture(0)

face_number = 1

while True:

    ret, frame = cap.read()

    h, w, _ = frame.shape

    grid_size = 180
    cell_size = grid_size // 3

    start_x = (w - grid_size) // 2
    start_y = (h - grid_size) // 2

    for i in range(4):

        cv2.line(
            frame,
            (start_x + i * cell_size, start_y),
            (start_x + i * cell_size, start_y + grid_size),
            (0, 255, 0),
            2
        )

        cv2.line(
            frame,
            (start_x, start_y + i * cell_size),
            (start_x + grid_size, start_y + i * cell_size),
            (0, 255, 0),
            2
        )

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.imshow("Rubik Scanner", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):

        filename = f"assets/scans/face_{face_number}.jpg"

        cv2.imwrite(filename, frame)

        print(f"Saved: {filename}")

        face_number += 1

    elif key == ord('q'):
        break

    if cv2.getWindowProperty(
        "Rubik Scanner",
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

cap.release()
cv2.destroyAllWindows()
