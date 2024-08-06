# Filename: trading_simulation/simulation.py
# Description: This module contains the main logic for running a Monte Carlo simulation
#              to analyze the probability of passing a prop firm trading test with
#              trailing stops and profit targets.

import numpy as np

class MarketSimulation:
    """
    A class to represent a market simulation for trading strategies.

    Attributes:
    num_trials (int): Number of simulation trials.
    num_trades (int): Number of trades per trial.
    win_rate (float): Probability of winning a trade.
    reward_per_win (float): Amount gained per winning trade.
    risk_per_loss (float): Amount lost per losing trade.
    profit_target (float): Target profit to achieve.
    trailing_stop (float): Trailing stop amount.
    """

    def __init__(self, num_trials, num_trades, win_rate, reward_per_win, risk_per_loss, profit_target, trailing_stop):
        """
        Constructs all the necessary attributes for the MarketSimulation object.
        """
        self.num_trials = num_trials
        self.num_trades = num_trades
        self.win_rate = win_rate
        self.reward_per_win = reward_per_win
        self.risk_per_loss = risk_per_loss
        self.profit_target = profit_target
        self.trailing_stop = trailing_stop

    def run(self):
        """
        Runs the market simulation.

        Returns:
        float: Probability of achieving the profit target.
        list: Balances for each trial.
        """
        success_count = 0  # Counter for successful trials
        all_balances = []  # List to store balances for all trials

        for _ in range(self.num_trials):
            balance = 0  # Initial balance for each trial
            max_balance = 0  # Track the maximum balance achieved during the trial
            trial_balances = []  # List to store balance after each trade in a trial

            for _ in range(self.num_trades):
                # Simulate a trade: win or lose
                if np.random.rand() < self.win_rate:
                    balance += self.reward_per_win  # Increase balance on win
                else:
                    balance -= self.risk_per_loss  # Decrease balance on loss

                max_balance = max(max_balance, balance)  # Update maximum balance

                # Check if profit target is reached
                if balance >= self.profit_target:
                    success_count += 1
                    break  # Exit the trial early if profit target is achieved

                # Check if balance falls below the trailing stop threshold
                if balance <= max_balance - self.trailing_stop:
                    break  # Exit the trial early if balance falls below trailing stop

                trial_balances.append(balance)  # Append current balance to trial balances

            all_balances.append(trial_balances)  # Append the trial balances to all balances

        success_probability = success_count / self.num_trials  # Calculate the success probability
        return success_probability, all_balances
