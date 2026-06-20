import kociemba

def solve_cube(cube_state):
    try:
        solution = kociemba.solve(cube_state)
        return solution
    except Exception as e:
        return f"Error: {e}"