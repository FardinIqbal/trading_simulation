# tests/test_simulation.py

import unittest
from trading_simulation.simulation import MarketSimulation
from trading_simulation.config import SimulationConfig

class TestMarketSimulation(unittest.TestCase):
    def setUp(self):
        self.config = SimulationConfig()
        self.simulation = MarketSimulation(
            self.config.num_trials,
            self.config.num_trades,
            self.config.win_rate,
            self.config.reward_per_win,
            self.config.risk_per_loss,
            self.config.profit_target,
            self.config.trailing_stop
        )

    def test_run_simulation(self):
        success_probability, all_balances = self.simulation.run()
        self.assertGreaterEqual(success_probability, 0)
        self.assertLessEqual(success_probability, 1)

if __name__ == '__main__':
    unittest.main()
