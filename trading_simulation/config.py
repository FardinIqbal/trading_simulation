# trading_simulation/config.py

class SimulationConfig:
    def __init__(self):
        self.num_trials = 1000
        self.num_trades = 1000
        self.win_rate = 0.50
        self.reward_per_win = 500
        self.risk_per_loss = 500
        self.profit_target = 3000
        self.trailing_stop = 2500
