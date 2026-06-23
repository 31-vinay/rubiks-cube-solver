from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QHBoxLayout
)

from cube_face import CubeFace
from color_palette import ColorPalette
from PyQt6.QtWidgets import QPushButton
import sys
import os
import subprocess

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

import scanner.cube_scanner as cube_scanner

from scanner.cube_scanner import (
    solve_scanned_cube,
    all_faces_scanned
)

class CubeEditor(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        title = QLabel("Rubik's Cube Net")

        title.setStyleSheet("""
            color:white;
            font-size:20px;
            font-weight:bold;
        """)

        main_layout.addWidget(title)

        self.palette = ColorPalette()

        content_layout = QHBoxLayout()

        cube_net = QGridLayout()

        self.up = CubeFace("U")
        self.left = CubeFace("L")
        self.front = CubeFace("F")
        self.right = CubeFace("R")
        self.back = CubeFace("B")
        self.down = CubeFace("D")

        self.up.setParent(self)
        self.left.setParent(self)
        self.front.setParent(self)
        self.right.setParent(self)
        self.back.setParent(self)
        self.down.setParent(self)

        cube_net.addWidget(self.up, 0, 1)

        cube_net.addWidget(self.left, 1, 0)
        cube_net.addWidget(self.front, 1, 1)
        cube_net.addWidget(self.right, 1, 2)
        cube_net.addWidget(self.back, 1, 3)

        cube_net.addWidget(self.down, 2, 1)

        content_layout.addWidget(self.palette)
        content_layout.addLayout(cube_net)

        main_layout.addLayout(content_layout)

        self.reset_button = QPushButton("Reset Cube")

        self.reset_button.setStyleSheet("""
            QPushButton{
                background-color:#ef4444;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#dc2626;
            }
        """)

        self.reset_button.clicked.connect(self.reset_cube)

        main_layout.addWidget(self.reset_button)

        self.state_button = QPushButton("Generate State")

        self.state_button.setStyleSheet("""
            QPushButton{
                background-color:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#1D4ED8;
            }
        """)

        self.state_button.clicked.connect(self.generate_state)

        main_layout.addWidget(self.state_button)

        self.validate_button = QPushButton("Validate Cube")

        self.validate_button.setStyleSheet("""
            QPushButton{
                background-color:#16A34A;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#15803D;
            }
        """)

        self.validate_button.clicked.connect(self.validate_cube)

        main_layout.addWidget(self.validate_button)

        self.solve_button = QPushButton("Solve Cube")

        self.solve_button.setStyleSheet("""
            QPushButton{
                background-color:#7C3AED;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#6D28D9;
            }
        """)

        self.solve_button.clicked.connect(self.solve_cube)

        main_layout.addWidget(self.solve_button)

        self.solution_label = QLabel("Solution will appear here")
        self.solution_label.setWordWrap(True)
        self.solution_label.setMaximumHeight(50)

        self.scan_status_label = QLabel()

        self.scan_status_label.setStyleSheet("""
            color:white;
            font-size:13px;
            padding:6px;
        """)

        main_layout.addWidget(self.scan_status_label)

        self.update_scan_status()

        cube_scanner.load_cube_faces()

        self.load_scanned_cube_into_gui()

        self.scan_button = QPushButton("Scan Next Face")

        self.scan_button.setStyleSheet("""
            QPushButton{
                background-color:#F59E0B;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#D97706;
            }
        """)

        self.scan_button.clicked.connect(
            self.scan_face
        )

        self.solve_scan_button = QPushButton(
            "Solve Scanned Cube"
        )

        self.solve_scan_button.setStyleSheet("""
            QPushButton{
                background-color:#DC2626;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#B91C1C;
            }
        """)

        self.solve_scan_button.clicked.connect(
            self.solve_scanned_cube_gui
        )

        main_layout.addWidget(self.scan_button)

        main_layout.addWidget(self.solve_scan_button)

        self.solution_label.setStyleSheet("""
            color:white;
            font-size:13px;
            padding:6px;
        """)

        main_layout.addWidget(self.solution_label)

        self.load_button = QPushButton("Load Solved Cube")

        self.load_button.setStyleSheet("""
            QPushButton{
                background-color:#0891B2;
                color:white;
                border:none;
                border-radius:8px;
                padding:6px;
                font-size:13px;
            }

            QPushButton:hover{
                background-color:#0E7490;
            }
        """)

        self.load_button.clicked.connect(self.load_solved_cube)

        main_layout.addWidget(self.load_button)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#121212;
            }
        """)

    def reset_cube(self):

        faces = [
            self.up,
            self.left,
            self.front,
            self.right,
            self.back,
            self.down
        ]

        center_colors = {
            "U": "white",
            "D": "yellow",
            "F": "green",
            "B": "blue",
            "R": "red",
            "L": "orange"
        }

        for face in faces:

            for row in range(3):

                for col in range(3):

                    sticker = face.stickers[row][col]

                    if sticker.is_center:

                        color = center_colors[face.face_name]

                    else:

                        color = "white"

                    sticker.current_color = color

                    sticker.setStyleSheet(
                        f"""
                        background-color:{color};
                        border:1px solid #444;
                        """
                    )

    def load_solved_cube(self):

        faces = {
            self.up: "white",
            self.right: "red",
            self.front: "green",
            self.down: "yellow",
            self.left: "orange",
            self.back: "blue"
        }

        for face, color in faces.items():

            for row in range(3):

                for col in range(3):

                    sticker = face.stickers[row][col]

                    sticker.current_color = color

                    sticker.setStyleSheet(
                        f"""
                        background-color:{color};
                        border:1px solid #444;
                        """
                    )

        self.solution_label.setText(
            "Solved cube loaded"
        )

    def get_color_counts(self):

        faces = [
            self.up,
            self.right,
            self.front,
            self.down,
            self.left,
            self.back
        ]

        color_counts = {}

        for face in faces:

            for row in face.stickers:

                for sticker in row:

                    color = sticker.current_color

                    color_counts[color] = (
                        color_counts.get(color, 0) + 1
                    )

        return color_counts

    def get_cube_state(self):

        faces = [
            self.up,
            self.right,
            self.front,
            self.down,
            self.left,
            self.back
        ]

        color_to_face = {
            "white": "U",
            "red": "R",
            "green": "F",
            "yellow": "D",
            "orange": "L",
            "blue": "B"
        }

        cube_state = ""

        for face in faces:
            for row in face.stickers:
                for sticker in row:
                    cube_state += color_to_face[
                        sticker.current_color
                    ]

        return cube_state

    def generate_state(self):

        faces = [
            self.up,
            self.right,
            self.front,
            self.down,
            self.left,
            self.back
        ]

        color_to_face = {
            "white": "U",
            "red": "R",
            "green": "F",
            "yellow": "D",
            "orange": "L",
            "blue": "B"
        }

        cube_state = self.get_cube_state()

        color_counts = {}

        for face in faces:
            for row in face.stickers:
                for sticker in row:
                    color_counts[sticker.current_color] = (
                        color_counts.get(sticker.current_color, 0) + 1
                    )

        print("Color Counts:")
        print(self.get_color_counts())

        print("\nCube State:")
        print(cube_state)

        print("\nLength:")
        print(len(cube_state))

        print("Centers:")
        print("U =", self.up.stickers[1][1].current_color)
        print("R =", self.right.stickers[1][1].current_color)
        print("F =", self.front.stickers[1][1].current_color)
        print("D =", self.down.stickers[1][1].current_color)
        print("L =", self.left.stickers[1][1].current_color)
        print("B =", self.back.stickers[1][1].current_color)

    def validate_cube(self):

        counts = self.get_color_counts()

        required_colors = [
            "white",
            "yellow",
            "red",
            "orange",
            "blue",
            "green"
        ]

        print("\n===== VALIDATION =====")

        valid = True

        for color in required_colors:

            count = counts.get(color, 0)

            print(f"{color}: {count}")

            if count != 9:
                valid = False

        if valid:
            print("\nVALID CUBE")
        else:
            print("\nINVALID CUBE")

    def solve_cube(self):

        counts = self.get_color_counts()

        required_colors = [
            "white",
            "yellow",
            "red",
            "orange",
            "blue",
            "green"
        ]

        for color in required_colors:

            if counts.get(color, 0) != 9:

                self.solution_label.setText(
                    "Invalid cube: color counts incorrect"
                )

                return

        try:

            import kociemba

            cube_state = self.get_cube_state()

            print("\nSOLVE STATE:")
            print(cube_state)

            solution = kociemba.solve(cube_state)

            self.solution_label.setText(
                f"Solution: {solution}"
            )

        except Exception as e:

            self.solution_label.setText(
                f"Error: {str(e)}"
            )

    def update_scan_status(self):

        text = "Scanned: "

        for face in ["U", "R", "F", "D", "L", "B"]:

            if (
                cube_scanner.cube_faces[face] is not None
                and cube_scanner.cube_faces[face] != [["null"]]
            ):
                text += f"{face}✓  "
            else:
                text += f"{face}✗  "

        self.scan_status_label.setText(text)

    def scan_face(self):

        try:

            import sys

            subprocess.run(
                [sys.executable, "scanner/color_detector.py"]
            )

            cube_scanner.load_cube_faces()

            self.load_scanned_cube_into_gui()

            self.update_scan_status()

            self.solution_label.setText(
                "Face scanned successfully"
            )

        except Exception as e:

            self.solution_label.setText(
                f"Error: {str(e)}"
            )

    def solve_scanned_cube_gui(self):

        cube_scanner.load_cube_faces()

        if not all_faces_scanned():

            self.solution_label.setText(
                "Please scan all 6 faces first"
            )

            return

        solution = solve_scanned_cube()

        self.solution_label.setText(
            f"Solution: {solution}"
        )

    def load_scanned_cube_into_gui(self):

        face_map = {
            "U": self.up,
            "R": self.right,
            "F": self.front,
            "D": self.down,
            "L": self.left,
            "B": self.back
        }

        for face_name, gui_face in face_map.items():

            scanned_face = cube_scanner.cube_faces[face_name]

            if scanned_face is None:
                continue

            for row in range(3):
                for col in range(3):

                    color = scanned_face[row][col]

                    sticker = gui_face.stickers[row][col]

                    sticker.current_color = color

                    sticker.setStyleSheet(
                        f"""
                        background-color:{color};
                        border:1px solid #444;
                        """
                    )
