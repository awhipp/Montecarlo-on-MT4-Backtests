# Execute MonteCarlo Simulation on MetaTrader 4 Strategy Results

## What does this do

The following python script allows Forex traders who run backtests through the MetaTrader 4 platform to run a Montecarlo Simulation on their results.

This script will do the following:

1. Convert your `.htm` file to a `.csv` (this is because MT4 does not output results in a usable format).
2. Run a MonteCarlo Simulation on the results and provide you with the simulation results.

## To Run

Put this script in the same folder as the backtest results (typically `StrategyTester.htm`) and then execute `py MT4_Results_To_MonteCarlo.py` and it will do the rest.

## Requirements

* Python 3.4+
* pip
* `pip install pandas`
* `pip install numpy`
* `pip install pandas_montecarlo`
