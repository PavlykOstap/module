from crud import Pawn, Piece, King, Knight, Rook, Bishop, Queen


class Game:
    def __init__(self):
        self.board = {}
        self.setup()
        self.current_player = 'w'

    # Вигляд дошки
    def setup(self):
        self.board = {
            (1, 8): Rook('b', 1, 8), (2, 8): Knight('b', 2, 8), (3, 8): Bishop('b', 3, 8), (4, 8): Queen('b', 4, 8),
            (5, 8): King('b', 5, 8), (6, 8): Bishop('b', 6, 8), (7, 8): Knight('b', 7, 8), (8, 8): Rook('b', 8, 8),
            (1, 7): Pawn('b', 1, 7), (2, 7): Pawn('b', 2, 7), (3, 7): Pawn('b', 3, 7), (4, 7): Pawn('b', 4, 7),
            (5, 7): Pawn('b', 5, 7), (6, 7): Pawn('b', 6, 7), (7, 7): Pawn('b', 7, 7), (8, 7): Pawn('b', 8, 7),
            (1, 6): None, (2, 6): None, (3, 6): None, (4, 6): None,
            (5, 6): None, (6, 6): None, (7, 6): None, (8, 6): None,
            (1, 5): None, (2, 5): None, (3, 5): None, (4, 5): None,
            (5, 5): None, (6, 5): None, (7, 5): None, (8, 5): None,
            (1, 4): None, (2, 4): None, (3, 4): None, (4, 4): None,
            (5, 4): None, (6, 4): None, (7, 4): None, (8, 4): None,
            (1, 3): None, (2, 3): None, (3, 3): None, (4, 3): None,
            (5, 3): None, (6, 3): None, (7, 3): None, (8, 3): None,
            (1, 2): Pawn('w', 1, 2), (2, 2): Pawn('w', 2, 2), (3, 2): Pawn('w', 3, 2), (4, 2): Pawn('w', 4, 2),
            (5, 2): Pawn('w', 5, 2), (6, 2): Pawn('w', 6, 2), (7, 2): Pawn('w', 7, 2), (8, 2): Pawn('w', 8, 2),
            (1, 1): Rook('w', 1, 1), (2, 1): Knight('w', 2, 1), (3, 1): Bishop('w', 3, 1), (4, 1): Queen('w', 4, 1),
            (5, 1): King('w', 5, 1), (6, 1): Bishop('w', 6, 1), (7, 1): Knight('w', 7, 1), (8, 1): Rook('w', 8, 1)
        }

    def move(self, position_from: tuple, position_to: tuple):
        print("Move function called")
        piece = self.board.get(position_from)

        # Перевірка чи існує фігура на заданій позиції
        if piece:
            # Перевірка чи відповідає колір фігури ігрока, який зараз повинен ходити
            if piece.color == self.current_player:
                # Валідація можливості ходу
                if self.validate_move(piece, position_to):
                    # Виконання ходу
                    self.board[position_to] = piece
                    self.board[position_from] = None
                    piece.x, piece.y = position_to  # Оновлення координат фігури
                    # Свайп ігрока, який зараз повинен ходити
                    self.current_player = 'b' if self.current_player == 'w' else 'w'
                    return
                else:
                    raise ValueError("Invalid move")
            else:
                raise ValueError("You cannot move opponent's piece")
        else:
            raise ValueError("No piece at the specified position")

    def validate_move(self, piece: Piece, position_to: tuple):
        target_piece = self.board.get(position_to)
        if target_piece and target_piece.color == piece.color:
            return False  # Фігура не зможе бити свою фігуру

        # Перевірка фігури на хід в задану позицію
        if piece.can_move(piece.x, piece.y, position_to[0], position_to[1]):
            return True
        else:
            return False

    def print_board(self):
        l = list(self.board.values())
        l = [piece if piece else '_' for piece in l]  # Use piece representation if piece exists, otherwise '_'
        l = [l[i: i + 8] for i in range(0, 64, 8)]
        for i, row in enumerate(l):
            print(" | ".join(str(square) for square in row))
