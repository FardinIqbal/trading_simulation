Here's a comprehensive `README.md` for your trading simulation project:

```markdown
# Trading Simulation Project

## Overview

This project simulates the probability of passing a prop firm trading test with trailing stops and profit targets using a Monte Carlo simulation. The simulation analyzes scenarios under a 1:1 risk/reward ratio and a 50% win rate, aiming to determine the likelihood of achieving the profit target within 1,000 trading attempts.

## Project Structure

```plaintext
trading_simulation/
│
├── trading_simulation/
│   ├── __init__.py
│   ├── simulation.py
│   ├── utils.py
│   ├── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_simulation.py
│   ├── test_utils.py
│
├── scripts/
│   ├── run_simulation.py
│
├── requirements.txt
├── README.md
├── setup.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/trading_simulation.git
cd trading_simulation
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the simulation, execute the following command:

```bash
python scripts/run_simulation.py
```

This will execute the simulation and print the probability of success. Additionally, it will plot the balance progression for a few sample trials.

### Configuration

You can modify the simulation parameters by editing the `SimulationConfig` class in `trading_simulation/config.py`. The default parameters are:

```python
class SimulationConfig:
    def __init__(self):
        self.num_trials = 1000
        self.num_trades = 1000
        self.win_rate = 0.50
        self.reward_per_win = 500
        self.risk_per_loss = 500
        self.profit_target = 3000
        self.trailing_stop = 2500
```

## Testing

To run the unit tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Project Details

### `simulation.py`

Contains the main logic for running the Monte Carlo simulation.

### `utils.py`

Includes utility functions such as calculating the probability of success.

### `config.py`

Holds the configuration settings for the simulation.

### `run_simulation.py`

A script to run the simulation and plot the results.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that you have updated the tests to cover any modifications.

## License

This project is licensed under the MIT License.
