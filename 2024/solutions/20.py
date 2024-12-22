from collections import deque, defaultdict
G = [line.rstrip('\n') for line in open("inputs/20.txt")]

R = len(G)
C = len(G[0])
S = None
E = None
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            S = (r, c)
        elif G[r][c] == 'E':
            E = (r, c)

N = [(-1,0),(1,0),(0,-1),(0,1)]

def is_track(ch):
    return ch in ('.', 'S', 'E')

# BFS function to find shortest dist from a given S point
def bfs(start_pos):
    dist = [[float('inf')] * C for _ in range(R)]
    sr, sc = start_pos
    dist[sr][sc] = 0
    queue = deque([start_pos])
    while queue:
        x, y = queue.popleft()
        for dx, dy in N:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if is_track(G[nx][ny]) and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return dist

# Get dist_from_S and dist_from_E
dist_from_S = bfs(S)
dist_from_E = bfs(E)

# Normal shortest path from S to E
normal_dist = dist_from_S[E[0]][E[1]]


def one():

    # We'll find all valid cheats.
    # A cheat:
    #   start from a track cell 'start_node'
    #   Perform 1 or 2 steps ignoring walls
    #   end at a track cell 'end_node'
    #   route_with_cheat = dist_from_S[start_node] + cheat_length + dist_from_E[end_node]
    #   savings = normal_dist - route_with_cheat
    # We count how many have savings >= 100

    cheats = set()  # to store (sx, sy, ex, ey)

    for x in range(R):
        for y in range(C):
            # Only consider this cell as a cheat S if it's reachable and is track
            if dist_from_S[x][y] == float('inf'):
                continue
            if not is_track(G[x][y]):
                continue

            base_dist = dist_from_S[x][y]
            # 1-step cheat
            for dx, dy in N:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    # ignoring walls for the cheat step, so no condition here except inside bounds
                    if is_track(G[nx][ny]):
                        # end_node = (nx, ny)
                        # Check if end_node is reachable from E
                        if dist_from_E[nx][ny] != float('inf'):
                            route_with_cheat = base_dist + 1 + dist_from_E[nx][ny]
                            saving = normal_dist - route_with_cheat
                            if saving >= 100:
                                # record cheat
                                if (x,y,nx,ny) not in cheats:
                                    cheats.add((x,y,nx,ny))

            # 2-step cheat
            # For each direction for the first step:
            for dx1, dy1 in N:
                ix, iy = x+dx1, y+dy1
                if 0 <= ix < R and 0 <= iy < C:
                    # first step can go through walls as well
                    # second step:
                    for dx2, dy2 in N:
                        fx, fy = ix+dx2, iy+dy2
                        if 0 <= fx < R and 0 <= fy < C:
                            # final cell must be track
                            if is_track(G[fx][fy]):
                                if dist_from_E[fx][fy] != float('inf'):
                                    route_with_cheat = base_dist + 2 + dist_from_E[fx][fy]
                                    saving = normal_dist - route_with_cheat
                                    if saving >= 100:
                                        if (x,y,fx,fy) not in cheats:
                                            cheats.add((x,y,fx,fy))

    # Count the number of cheats with at least 100 saving
    print(len(cheats))

def two(limit=20):
    # We'll find cheats that can last up to 20 steps.
    # For each track cell reachable from S, we do a BFS ignoring walls (up to 20 steps)
    # to find reachable track cells.
    # This BFS will track how many steps have been taken.
    # We only care about shortest ignoring-wall distance ≤ 20 to each cell.

    cheats = set()

    # Pre-collect all track cells that are reachable from S to limit starting points
    track_cells_from_S = [(x,y) for x in range(R) for y in range(C) 
                          if dist_from_S[x][y] != float('inf') and is_track(G[x][y])]

    for (sx, sy) in track_cells_from_S:
        # BFS ignoring walls from (sx, sy) up to distance 20
        dist_ignore_walls = [[float('inf')] * C for _ in range(R)]
        dist_ignore_walls[sx][sy] = 0
        q = deque([(sx, sy)])
        while q:
            x, y = q.popleft()
            d = dist_ignore_walls[x][y]
            if d == limit:
                # Can't go further than 20 steps
                continue
            for dx, dy in N:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    # ignoring walls, so no condition except bounds
                    if dist_ignore_walls[nx][ny] > d + 1:
                        dist_ignore_walls[nx][ny] = d+1
                        q.append((nx, ny))

        # Now check all track cells reachable within ≤20 steps
        base_dist = dist_from_S[sx][sy]
        for fx in range(R):
            for fy in range(C):
                d = dist_ignore_walls[fx][fy]
                if d != float('inf') and 1 <= d <= limit and is_track(G[fx][fy]):
                    # We have a potential cheat from (sx, sy) to (fx, fy) of length d
                    if dist_from_E[fx][fy] != float('inf'):
                        route_with_cheat = base_dist + d + dist_from_E[fx][fy]
                        saving = normal_dist - route_with_cheat
                        if saving >= 100:
                            cheats.add((sx, sy, fx, fy))

    print(len(cheats))

one()
two()