"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

Example 1
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

Use BFS to expand the area from init point in coordinate to 8 directions. Keep tracking currentX, currentY and steps. Once the (currentX, currentY) is equal to target coordinate return steps.

"""
import collections

def minKnightMoves(x: int, y: int) -> int:
    # 8 directions
    directions = {(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)}
    queue = collections.deque()
    visited = set()
    x, y = abs(x), abs(y)
    if x == 1 and y == 1: return 2
    # (x,y,steps)
    queue = collections.deque([(0, 0, 0)])
    while queue:
        cur_x, cur_y, steps = queue.popleft()
        if [cur_x, cur_y] == [x, y]: return steps

        for dx, dy in directions:
            if 0 <= cur_x + dx <= 300 and 0 <= cur_y + dy <= 300 and (cur_x + dx, cur_y + dy) not in visited:
                visited.add((cur_x + dx, cur_y + dy))
                queue.append((cur_x + dx, cur_y + dy, steps + 1))


print(minKnightMoves(5,5))