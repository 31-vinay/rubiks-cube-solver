from cube_input import get_cube_state
from cube_validator import validate_cube
from cube_solver import solve_cube

print("\n=== Rubik's Cube Solver ===")

cube_state = get_cube_state()

valid, message = validate_cube(cube_state)

if not valid:
    print("\nValidation Failed:")
    print(message)

else:
    print("\nValidation Passed!")

    solution = solve_cube(cube_state)

    print("\nSolution:")
    print(solution)