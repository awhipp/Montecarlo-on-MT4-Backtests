# MT4 Results to MonteCarlo Simulation

MT4 does not output results in a usable format. This script will convert your `.htm` file to a `.csv`.

The following python script allows Forex traders who run backtests through the MetaTrader 4 platform to run a Montecarlo Simulation on their results.

To run simply put this script in the same folder as the backtest results (typically `StrategyTester.htm`) and then execute `py MT4_Results_To_MonteCarlo.py` and it will do the rest.


## Requirements

* Python 3.4+
* pip
* pandas
* numpy
* pandas_montecarlo
