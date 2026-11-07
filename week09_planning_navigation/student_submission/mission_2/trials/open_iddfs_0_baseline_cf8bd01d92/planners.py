"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import free, reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []

    frontier = deque([ctx.start])
    parent = {ctx.start: None}

    while frontier:
        current = frontier.popleft()  # Oldest cell first

        if current == ctx.goal:
            return reconstruct(parent, current)

        for nxt in ctx.expand(current, len(frontier) + 1):
            if nxt not in parent:
                parent[nxt] = current
                frontier.append(nxt)

    return []

def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []

    frontier = [ctx.start]
    parent = {ctx.start: None}

    while frontier:
        current = frontier.pop()  # Newest cell first

        if current == ctx.goal:
            return reconstruct(parent, current)

        for nxt in ctx.expand(current, len(frontier) + 1):
            if nxt not in parent:
                parent[nxt] = current
                frontier.append(nxt)

    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []

    limit = 0

    while True:
        # Each stack entry holds a complete path.
        frontier = [[ctx.start]]
        cutoff = False

        while frontier:
            path = frontier.pop()
            current = path[-1]
            depth = len(path) - 1

            if current == ctx.goal:
                return path

            neighbors = ctx.expand(current, len(frontier) + 1)

            # Prevent cycles within this particular path.
            next_cells = [nxt for nxt in neighbors if nxt not in path]

            if depth == limit:
                if next_cells:
                    cutoff = True  # A deeper search could go farther.
                continue

            for nxt in next_cells:
                frontier.append(path + [nxt])

        if not cutoff:
            return []  # Fully searched; no deeper paths remain.

        limit += 1


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []

    frontier = []
    parent = {ctx.start: None}
    best_cost = {ctx.start: 0}

    # Heap entries: (estimated total cost, cost so far, cell)
    heappush(frontier, (ctx.heuristic(ctx.start), 0, ctx.start))

    while frontier:
        _, cost, current = heappop(frontier)

        # Ignore an entry if a cheaper route was found later.
        if cost != best_cost[current]:
            continue

        if current == ctx.goal:
            return reconstruct(parent, current)

        for nxt in ctx.expand(current, len(frontier) + 1):
            new_cost = cost + 1

            if nxt not in best_cost or new_cost < best_cost[nxt]:
                best_cost[nxt] = new_cost
                parent[nxt] = current
                priority = new_cost + ctx.heuristic(nxt)
                heappush(frontier, (priority, new_cost, nxt))

    return []
