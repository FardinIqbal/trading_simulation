# trading_simulation/profitability.py
# This module contains functions to calculate the profitability of participating in the simulations.

def calculate_expected_return(success_probability, profit_target, eval_cost, performance_cost):
    """
    Calculate the expected return of participating in the simulations.

    Parameters:
    success_probability (float): The probability of a successful attempt for one account.
    profit_target (float): The profit target for a successful attempt.
    eval_cost (float): The cost of participating in one evaluation account.
    performance_cost (float): The cost of participating in one performance account.

    Returns:
    tuple: (expected_return, payout_probability)
    """
    # Probability of passing at least one of two evaluation accounts
    eval_success_prob = 1 - (1 - success_probability) ** 2

    total_cost = 2 * eval_cost + performance_cost  # Cost for two eval accounts + one performance account
    net_profit = profit_target - total_cost

    # Probability of passing both evaluation (at least one) and performance accounts
    total_success_probability = eval_success_prob * success_probability

    failure_probability = 1 - total_success_probability
    expected_return = (total_success_probability * net_profit) - (failure_probability * total_cost)
    return expected_return, total_success_probability


# Example usage
if __name__ == '__main__':
    success_probability = 0.498  # Probability of passing one account
    profit_target = 3000
    cost_eval_account = 37.80
    cost_performance_account = 105.00

    expected_return, payout_probability = calculate_expected_return(
        success_probability, profit_target, cost_eval_account, cost_performance_account
    )

    print(f"Probability of Passing One Account: {success_probability:.4f}")
    print(f"Probability of Passing at Least One Evaluation Account: {1 - (1 - success_probability) ** 2:.4f}")
    print(f"Probability of Getting a Payout: {payout_probability:.4f}")
    print(f"Expected Return: ${expected_return:.2f}")
