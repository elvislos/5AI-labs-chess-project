import random
import chess
from chess import Board, Move
from fiveaichess.agents.agent import Agent
from fiveaichess.utilities.utility import Utility


class alphaBetaAgent(Agent):
    name = "AlphaBetaAgent"
    author = "UAntwerp - Robbe De Wit & Elvis Los"

    def __init__(self, utility: Utility, time_limit_move: float):
        super().__init__(utility, time_limit_move)

    def calculate_move(self, board: Board, constraints: dict[str, int] = {}) -> Move:
        depth = constraints.get("depth", 3)
        legal_moves = list(board.legal_moves)

        if not legal_moves:
            raise ValueError("Geen legale zetten beschikbaar")

        maximizing = board.turn == chess.WHITE
        alpha = -10**9
        beta = 10**9
        best_value = -10**9 if maximizing else 10**9
        best_move = None

        for move in legal_moves:
            board.push(move)
            val = self.alpha_beta(board, depth - 1, alpha, beta, not maximizing)
            board.pop()

            if maximizing:
                if val > best_value:
                    best_value = val
                    best_move = move
                alpha = max(alpha, best_value)
            else:
                if val < best_value:
                    best_value = val
                    best_move = move
                beta = min(beta, best_value)

            if alpha >= beta:
                break

        return best_move if best_move is not None else random.choice(legal_moves)

    def alpha_beta(self, board: Board, depth: int, alpha: int, beta: int, maximizing: bool) -> int:
        if depth == 0 or board.is_game_over():
            return self.utility.board_value(board)

        if maximizing:
            value = -10**9
            for move in board.legal_moves:
                board.push(move)
                val = self.alpha_beta(board, depth - 1, alpha, beta, False)
                board.pop()

                value = max(value, val)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value

        value = 10**9
        for move in board.legal_moves:
            board.push(move)
            val = self.alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()

            value = min(value, val)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value