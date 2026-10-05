import heapq

goal_states = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = {'U': -3, 'D': 3, 'L': -1, 'R': 1}

class puzzle_state:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other  ):
        return self.cost < other.cost

def print_board(board):
    print("+---+---+---+")
    for row in range(0, 9, 3):
        row_visual = "|"
        for tile in board[row:row + 3]:
            if tile == 0:
                row_visual += f" {(' ')} |"
            else:
                row_visual += f" {(str(tile))} |"
        print(row_visual)
        print("+---+---+---+")

def heuristic(board):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(board[i] - 1, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + moves[move]
    new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
    return new_board

def a_star(start_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, puzzle_state(start_state, None, None, 0, heuristic(start_state)))

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal_states:
            return current_state

        state_tuple = tuple(current_state.board)
        if state_tuple in closed_list:
            continue

        closed_list.add(state_tuple)

        blank_pos = current_state.board.index(0)
        for move in moves:
            if move == 'U' and blank_pos < 3:
                continue
            if move == 'D' and blank_pos > 5:
                continue
            if move == 'L' and blank_pos % 3 == 0:
                continue
            if move == 'R' and blank_pos % 3 == 2:
                continue
                
            new_board = move_tile(current_state.board, move, blank_pos)

            if tuple(new_board) in closed_list:
                continue

            new_state = puzzle_state(new_board, current_state, move, current_state.depth + 1, current_state.depth + 1 + heuristic(new_board))
            heapq. heappush(open_list, new_state)

    return None

def greedy_bf(start_state):
    open_list = []
    closed_list = set()

    initial_heuristic = heuristic(start_state)
    heapq.heappush(open_list, puzzle_state(start_state, None, None, 0, initial_heuristic))

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal_states:
            return current_state

        state_tuple = tuple(current_state.board)
        if state_tuple in closed_list:
            continue

        closed_list.add(state_tuple)

        blank_pos = current_state.board.index(0)
        for move in moves:
            if move == 'U' and blank_pos < 3:
                continue
            if move == 'D' and blank_pos > 5:
                continue
            if move == 'L' and blank_pos % 3 == 0:
                continue
            if move == 'R' and blank_pos % 3 == 2:
                continue
                
            new_board = move_tile(current_state.board, move, blank_pos)

            if tuple(new_board) in closed_list:
                continue
            
            heuristic_cost = heuristic(new_board)
            new_state = puzzle_state(board=new_board, parent=current_state, move=move, depth=current_state.depth + 1, cost=heuristic_cost)
            heapq.heappush(open_list, new_state)

    return None

def print_search(solution):
    path = []
    current = solution

    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    act_cost = 0
    for step in path:
        print(f"Move: {step.move}")
        print(f"Actual cost: {act_cost}")
        act_cost += 1
        print_board(step.board)

initial_state = [0, 1, 3, 4, 2, 5, 7, 8, 6]
solution_a = a_star(initial_state)
solution_b = greedy_bf(initial_state)

if solution_a:
    print(("Solution using A* found!"))
    print_search(solution_a)

print("\n")
if solution_b:
    print(("Solution using Greedy Best First found!"))
    print_search(solution_b)
else:
    print(("No solution"))