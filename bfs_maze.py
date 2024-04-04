from collections import deque
def hasPath(maze, start, destination):
    if not maze or not maze[0]:
        return False
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def isValid(x, y):
        return 0 <= x < m and 0 <= y < n and maze[x][y] == 0
    queue = deque([start])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) == tuple(destination):
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x, y
            while isValid(nx + dx, ny + dy):
                nx += dx
                ny += dy
            if (nx, ny) not in visited:
                queue.append((nx, ny))
    return False

# Test cases
maze1 = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start1 = [0, 4]
destination1 = [4, 4]
print("Test Case 1:", hasPath(maze1, start1, destination1))  # Output: True

maze2 = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start2 = [0, 4]
destination2 = [3, 2]
print("Test Case 2:", hasPath(maze2, start2, destination2))  # Output: False
