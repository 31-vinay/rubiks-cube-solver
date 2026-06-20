def validate_cube(cube_state):

    if len(cube_state) != 54:
        return False, "Cube state must contain 54 stickers."

    colors = ['U', 'R', 'F', 'D', 'L', 'B']

    for color in colors:
        if cube_state.count(color) != 9:
            return False, f"{color} must appear exactly 9 times."

    return True, "Valid cube."