from fiveaichess.agents.alphaBetaAgent import alphaBetaAgent
from fiveaichess.utilities.alphaBetaUtility import alphaBetaUtility
from fiveaichess.engines.uci_engine import UCIEngine

if __name__ == "__main__":
    # create your utility
    utility = alphaBetaUtility()
    # create your agent
    agent = alphaBetaAgent(utility, 5.0)
    # create the engine
    engine = UCIEngine(agent)

    # run the engine (will loop until the game is done or exited)
    engine.run()
