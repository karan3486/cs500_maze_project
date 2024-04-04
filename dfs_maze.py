def hasPathDFS(maze, start, destination):
    if not maze or not maze[0]:
        return False
    
    m, n = len(maze), len(maze[0])
    visited = set()

    def dfs(x, y):
        if (x, y) in visited:
            return False
        visited.add((x, y))
        if [x, y] == destination:
            return True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                nx += dx
                ny += dy
            nx -= dx
            ny -= dy
            if dfs(nx, ny):
                return True
        return False

    return dfs(start[0], start[1])

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
print("Test Case 1:", hasPathDFS(maze1, start1, destination1))  # Output: True

maze2 = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start2 = [0, 4]
destination2 = [3, 2]
print("Test Case 2:", hasPathDFS(maze2, start2, destination2))  # Output: False
