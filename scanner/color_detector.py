import cv2
import os
import numpy as np

def detect_color_hsv(h, s, v):

    if 20 <= h <= 40:
        return "yellow"

    elif 70 <= h <= 95:
        return "green"

    elif 100 <= h <= 130:
        return "blue"

    elif 0 <= h <= 5:
        return "red"

    elif 6 <= h <= 20:
        return "orange"

    return "unknown"

path = "assets/scans/face_1.jpg"

if not os.path.exists(path):
    print(f"Image not found: {path}")
    exit()

image = cv2.imread(path)

height, width, _ = image.shape

print("Image Loaded")
print(image.shape)

# Center of image
center_x = width // 2
center_y = height // 2

grid_size = 180
cell_size = grid_size // 3

start_x = center_x - grid_size // 2
start_y = center_y - grid_size // 2

sample_points = []

face_colors = []

for row in range(3):
    row_colors = []
    for col in range(3):

        x = start_x + col * cell_size + cell_size // 2
        y = start_y + row * cell_size + cell_size // 2

        sample_points.append((x, y))

        sample = image[
            y-5:y+5,
            x-5:x+5
        ]

        avg_bgr = sample.mean(axis=(0, 1))

        pixel = [[[int(avg_bgr[0]),
                int(avg_bgr[1]),
                int(avg_bgr[2])]]]

        hsv = cv2.cvtColor(
            np.uint8(pixel),
            cv2.COLOR_BGR2HSV
        )

        h, s, v = hsv[0][0]

        color = detect_color_hsv(h, s, v)

        row_colors.append(color)

        print(
            f"Cell ({row},{col}) -> {color}"
        )

        cv2.circle(
            image,
            (x, y),
            8,
            (0, 0, 255),
            -1
        )

    face_colors.append(row_colors)

print("\nDetected Face:")
for row in face_colors:
    print(row)

cv2.imshow("Sampling Points", image)

cv2.waitKey(0)
cv2.destroyAllWindows()