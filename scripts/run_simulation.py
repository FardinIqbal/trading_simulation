# scripts/run_simulation.py

from trading_simulation import MarketSimulation, SimulationConfig
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

    # Plotting the balance of a few trials
    for trial_balances in all_balances[:10]:
        plt.plot(trial_balances)

    plt.title('Balance Over Trades for Sample Trials')
    plt.xlabel('Trade Number')
    plt.ylabel('Balance')
    plt.show()


if __name__ == '__main__':
    main()
