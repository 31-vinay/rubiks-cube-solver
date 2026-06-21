cube_faces = {
    "U": None,
    "R": None,
    "F": None,
    "D": None,
    "L": None,
    "B": None
}

def save_face(face_name, face_colors):

    cube_faces[face_name] = face_colors

    print(f"\n{face_name} face saved")

    for row in face_colors:
        print(row)

def show_cube():

    print("\n===== STORED FACES =====")

    for face, data in cube_faces.items():

        print(f"\n{face}:")

        print(data)

test_face = [
    ["yellow","green","green"],
    ["red","yellow","orange"],
    ["yellow","blue","blue"]
]

save_face("F", test_face)

show_cube()