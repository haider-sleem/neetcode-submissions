class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }

        visited = set()
        biggest = 0

        def dfs(row, col):
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[row])
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))

            area = 1

            for dr, dc in directions.values():
                new_row = row + dr
                new_col = col + dc

                area += dfs(new_row, new_col)

            return area

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col)
                    biggest = max(biggest, area)

        return biggest
