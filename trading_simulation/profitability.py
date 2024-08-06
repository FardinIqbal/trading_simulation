# Filename: trading_simulation/profitability.py
# Description: This module contains a function to calculate the profitability of participating in the simulations.

def calculate_expected_return(success_probability, profit_target, cost_per_attempt):
    """
    Calculate the expected return of participating in the simulations.

    Parameters:
    success_probability (float): The probability of a successful attempt.
    profit_target (float): The profit target for a successful attempt.
    cost_per_attempt (float): The cost of participating in one simulation attempt.

    Returns:
    float: The expected return per attempt.
    """
    # Calculate the net profit from a successful attempt
    net_profit = profit_target - cost_per_attempt

    # Calculate the failure probability
    failure_probability = 1 - success_probability

    # Calculate the expected return
    expected_return = (success_probability * net_profit) - (failure_probability * cost_per_attempt)

    return expected_return

# Example usage
if __name__ == '__main__':
    success_probability = 0.498
    profit_target = 3000
    cost_per_attempt = 179.80

    expected_return = calculate_expected_return(success_probability, profit_target, cost_per_attempt)
    print(f"Expected Return per Attempt: ${expected_return:.2f}")
