import chess
from fiveaichess.utilities.utility import Utility


class alphaBetaUtility(Utility):
    PIECE_VALUES = {
        chess.PAWN: 100,
        chess.KNIGHT: 300,
        chess.BISHOP: 300,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 0,
    }

    def board_value(self, board: chess.Board) -> int:
        if board.is_checkmate():
            return -999999 if board.turn == chess.WHITE else 999999

        if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw():
            return 0

        score = 0
        for piece_type, value in self.PIECE_VALUES.items():
            score += len(board.pieces(piece_type, chess.WHITE)) * value
            score -= len(board.pieces(piece_type, chess.BLACK)) * value

        return score