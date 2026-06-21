import json
import os

FACE_ORDER = [
    "U",
    "R",
    "F",
    "D",
    "L",
    "B"
]

cube_faces = {
    "U": None,
    "R": None,
    "F": None,
    "D": None,
    "L": None,
    "B": None
}

DATA_FILE = "scanner/cube_data.json"

def load_cube_faces():

    global cube_faces

    if os.path.exists(DATA_FILE):

        with open(DATA_FILE, "r") as file:

            cube_faces = json.load(file)

def save_cube_faces():

    with open(DATA_FILE, "w") as file:

        json.dump(
            cube_faces,
            file,
            indent=4
        )

def all_faces_scanned():

    return all(
        face is not None
        for face in cube_faces.values()
    )

def scanned_count():

    count = 0

    for face in cube_faces.values():

        if face is not None:
            count += 1

    return count

def next_face_to_scan():

    for face in FACE_ORDER:

        if cube_faces[face] is None:
            return face

    return None

def save_face(face_name, face_colors):

    cube_faces[face_name] = face_colors

    save_cube_faces()

    print(
        f"\n{face_name} face saved "
        f"({scanned_count()}/6)"
    )

    for row in face_colors:
        print(row)

def show_cube():

    print("\n===== STORED FACES =====")

    for face, data in cube_faces.items():

        print(f"\n{face}:")
        print(data)

def generate_cube_state():

    if not all_faces_scanned():

        print("Not all faces scanned")

        return None

    center_map = {}

    for face in FACE_ORDER:

        center_color = cube_faces[face][1][1]

        center_map[center_color] = face

    cube_state = ""

    for face in FACE_ORDER:

        for row in cube_faces[face]:

            for color in row:

                cube_state += center_map[color]

    return cube_state

def solve_scanned_cube():

    cube_state = generate_cube_state()

    if cube_state is None:
        return None

    if cube_state == (
        "UUUUUUUUU"
        "RRRRRRRRR"
        "FFFFFFFFF"
        "DDDDDDDDD"
        "LLLLLLLLL"
        "BBBBBBBBB"
    ):
        return "Cube is already solved"

    try:

        import kociemba

        solution = kociemba.solve(cube_state)

        return solution

    except Exception as e:

        return f"Error: {e}"

def all_faces_scanned():

    return all(
        face is not None
        for face in cube_faces.values()
    )

def scanned_count():

    count = 0

    for face in cube_faces.values():

        if face is not None:
            count += 1

    return count

load_cube_faces()