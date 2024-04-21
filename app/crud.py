class Piece:
    x_line = 'abcdefgh'

    def __init__(self, color, x, y, symbol):
        self.color = color
        self.x = x
        self.y = y
        self.symbol = symbol

    def __repr__(self):
        return self.symbol

    def available_moves(self):
        moves = [(x, y) for x in range(1, 9) for y in range(1, 9)]
        return moves

    def can_move(self, from_x, from_y, to_x, to_y):
        return True

    def can_attack(self, from_x, from_y, to_x, to_y):
        return True


class Pawn(Piece):
    def __init__(self, color, x, y):
        symbol = '♟' if color == 'b' else '♙'
        super().__init__(color, x, y, symbol)
        self.first_move = True

    def available_moves(self):
        direction = 1 if self.color == 'w' else -1
        moves = [(self.x, self.y + direction)]
        if self.first_move:
            moves.append((self.x, self.y + 2 * direction))
        return moves

    def can_move(self, from_x, from_y, to_x, to_y):
        direction = 1 if self.color == 'w' else -1
        if (to_x == from_x and to_y == from_y + direction) or (
                self.first_move and to_x == from_x and to_y == from_y + 2 * direction):
            return True
        return False

    def can_attack(self, from_x, from_y, to_x, to_y):
        direction = 1 if self.color == 'w' else -1
        if abs(to_x - from_x) == 1 and to_y == from_y + direction:
            return True
        return False


class Rook(Piece):
    def __init__(self, color, x, y):
        symbol = '♜' if color == 'b' else '♖'
        super().__init__(color, x, y, symbol)

    def can_move(self, from_x, from_y, to_x, to_y):
        return from_x == to_x or from_y == to_y

    def can_attack(self, from_x, from_y, to_x, to_y):
        return self.can_move(from_x, from_y, to_x, to_y)


class Bishop(Piece):
    def __init__(self, color, x, y):
        symbol = '♝' if color == 'b' else '♗'
        super().__init__(color, x, y, symbol)

    def can_move(self, from_x, from_y, to_x, to_y):
        return abs(to_x - from_x) == abs(to_y - from_y)

    def can_attack(self, from_x, from_y, to_x, to_y):
        return self.can_move(from_x, from_y, to_x, to_y)


class Queen(Piece):
    def __init__(self, color, x, y):
        symbol = '♛' if color == 'b' else '♕'
        super().__init__(color, x, y, symbol)

    def can_move(self, from_x, from_y, to_x, to_y):
        return abs(to_x - from_x) == abs(to_y - from_y) or from_x == to_x or from_y == to_y

    def can_attack(self, from_x, from_y, to_x, to_y):
        return self.can_move(from_x, from_y, to_x, to_y)


class Knight(Piece):
    def __init__(self, color, x, y):
        symbol = '♞' if color == 'b' else '♘'
        super().__init__(color, x, y, symbol)

    def can_move(self, from_x, from_y, to_x, to_y):
        return (abs(to_x - from_x) == 2 and abs(to_y - from_y) == 1) or (
                abs(to_x - from_x) == 1 and abs(to_y - from_y) == 2)

    def can_attack(self, from_x, from_y, to_x, to_y):
        return self.can_move(from_x, from_y, to_x, to_y)


class King(Piece):
    def __init__(self, color, x, y):
        symbol = '♚' if color == 'b' else '♔'
        super().__init__(color, x, y, symbol)

    def can_move(self, from_x, from_y, to_x, to_y):
        return abs(to_x - from_x) <= 1 and abs(to_y - from_y) <= 1

    def can_attack(self, from_x, from_y, to_x, to_y):
        return self.can_move(from_x, from_y, to_x, to_y)
