import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.imshow(
        "Rubik Scanner - Press S to Scan",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord("s"):

        cv2.imwrite(
            "assets/scans/face_1.jpg",
            frame
        )

        print("Image Captured")

        break

    if key == ord("q"):
        break

    if cv2.getWindowProperty(
        "Rubik Scanner - Press S to Scan",
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

cap.release()
cv2.destroyAllWindows()