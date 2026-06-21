import cv2
import os

def detect_color(r, g, b):

    if r > 200 and g > 200:
        return "yellow"

    elif b > r and b > g:
        return "blue"

    elif g > r and g > b:
        return "green"

    elif r > 200 and g > 120:
        return "orange"

    elif r > 150 and g < 130:
        return "red"

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

for row in range(3):
    for col in range(3):

        x = start_x + col * cell_size + cell_size // 2
        y = start_y + row * cell_size + cell_size // 2

        sample_points.append((x, y))

        sample = image[
            y-5:y+5,
            x-5:x+5
        ]

        b, g, r = sample.mean(axis=(0, 1))

        color = detect_color(r, g, b)

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

cv2.imshow("Sampling Points", image)

cv2.waitKey(0)
cv2.destroyAllWindows()