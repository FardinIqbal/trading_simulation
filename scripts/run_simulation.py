# scripts/run_simulation.py

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

    print(f"Probability of success: {success_probability * 100:.2f}%")

    # Calculate and print the expected return
    cost_per_attempt = 179.80
    expected_return = calculate_expected_return(
        success_probability,
        config.profit_target,
        cost_per_attempt
    )
    print(f"Expected Return per Attempt: ${expected_return:.2f}")

    # Plotting the balance of a few trials
    for trial_balances in all_balances[:10]:
        plt.plot(trial_balances)

    plt.title('Balance Over Trades for Sample Trials')
    plt.xlabel('Trade Number')
    plt.ylabel('Balance')
    plt.show()


if __name__ == '__main__':
    main()
