def orangesRotting(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    queue = deque()
    fresh_count = 0
      
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1
      
    minutes_passed = 0
      
    while queue and fresh_count > 0:
        minutes_passed += 1
          
        for _ in range(len(queue)):
            i, j = queue.popleft()
              
            for delta_row, delta_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x, y = i + delta_row, j + delta_col
                  
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    fresh_count -= 1
                    grid[x][y] = 2
                    queue.append((x, y))
      
    return minutes_passed if fresh_count == 0 else -1

        