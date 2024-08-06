# scripts/run_simulation.py
# This script runs the market simulation and calculates the expected return

from trading_simulation import MarketSimulation, SimulationConfig
from trading_simulation.profitability import calculate_expected_return
import matplotlib.pyplot as plt


def main():
    config = SimulationConfig()
    simulation = MarketSimulation(
        config.num_trials,
        config.num_trades,
        config.win_rate,
        config.reward_per_win,
        config.risk_per_loss,
        config.profit_target,
        config.trailing_stop
    )

    success_probability, all_balances = simulation.run()

    print(f"Probability of passing one account: {success_probability:.4f}")

    # Calculate and print the expected return
    cost_eval_account = 37.80
    cost_performance_account = 105.00
    expected_return, payout_probability = calculate_expected_return(
        success_probability,
        config.profit_target,
        cost_eval_account,
        cost_performance_account
    )

    print(f"Probability of passing at least one evaluation account: {1 - (1 - success_probability) ** 2:.4f}")
    print(f"Probability of getting a payout: {payout_probability:.4f}")
    print(f"Expected Return: ${expected_return:.2f}")

    # Plotting the balance of a few trials
    for trial_balances in all_balances[:10]:
        plt.plot(trial_balances)

    plt.title('Balance Over Trades for Sample Trials')
    plt.xlabel('Trade Number')
    plt.ylabel('Balance')
    plt.show()


if __name__ == '__main__':
    main()
