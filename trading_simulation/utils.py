# trading_simulation/utils.py
# This file contains utility functions for the trading simulation

def calculate_probability(success_count, num_trials):
    """
    Calculate the probability of success based on the number of successful trials.

    Parameters:
    success_count (int): The number of successful trials.
    num_trials (int): The total number of trials.

    Returns:
    float: The probability of success.
    """
    return success_count / num_trials
