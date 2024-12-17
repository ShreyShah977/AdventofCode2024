def read_map(file_path):
    """
    Reads the map from the file and returns it as a list of strings.
    """
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def guard_patrol(file_path):
    """
    Reads the map, simulates the guard's patrol, and counts the distinct positions visited.
    """
    grid = read_map(file_path)
    
    # Directions are represented as (dx, dy): up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0  # Default direction (up)
    
    # Find the starting position and direction
    start_x, start_y = None, None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in "^>v<":
                start_x, start_y = i, j
                if cell == "^":
                    direction_index = 0
                elif cell == ">":
                    direction_index = 1
                elif cell == "v":
                    direction_index = 2
                elif cell == "<":
                    direction_index = 3
                break
        if start_x is not None:
            break

    visited = set()  # To track distinct positions
    x, y = start_x, start_y

    # Simulate the guard's movement
    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        visited.add((x, y))
        dx, dy = directions[direction_index]
        next_x, next_y = x + dx, y + dy

        # Check if there's an obstacle or the edge of the map
        if not (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0])) or grid[next_x][next_y] == "#":
            # Turn right (90 degrees)
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            x, y = next_x, next_y

    return len(visited)

def main():
    input_file = "input.txt"  # Replace with your actual file path
    result = guard_patrol(input_file)
    print(f"Number of distinct positions visited: {result}")
main()