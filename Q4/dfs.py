grid = []
word = 'XMAS'
W = len(word)
# Open the file in read mode
with open('Q4/input.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        lineGrid = []
        for c in line:
            if c != '\n':
                lineGrid.append(c)
        grid.append(lineGrid)

def count_unique_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited = set()  # To track globally visited cells
    unique_count = 0

    def dfs(x, y, index, path):
        # If the index equals the word length, we found the word
        if index == word_length:
            visited.update(path)  # Mark this path as visited
            return True

        # Check bounds and match the current letter
        if (
            x < 0 or x >= rows or y < 0 or y >= cols or  # Out of bounds
            grid[x][y] != word[index] or  # Current cell doesn't match
            (x, y) in visited  # Already part of another match
        ):
            return False

        # Add the current cell to the path
        path.add((x, y))

        # Explore all 8 directions
        found = False
        for dx, dy in directions:
            if dfs(x + dx, y + dy, index + 1, path):
                found = True
                break  # Stop searching further in this DFS branch

        # Backtrack: Remove the current cell from the path
        path.remove((x, y))
        return found

    # Traverse each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Start DFS if the first letter matches
            if grid[i][j] == word[0] and (i, j) not in visited:
                if dfs(i, j, 0, set()):
                    unique_count += 1

    return unique_count


word = "XMAS"

result = count_unique_word_occurrences(grid, word)
print(f"Unique occurrences of the word '{word}': {result}")