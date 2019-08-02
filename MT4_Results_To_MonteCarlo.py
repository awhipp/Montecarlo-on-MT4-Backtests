import re
import pandas_montecarlo
import pandas as pd
import numpy as np

toExclude = "<td colspan=2></td>"
toFind = "class=mspt"
fileName = "StrategyTester"
dd = -0.1
target = 0.1
multiplier = 1

# Read the MT4 Results HTM to memory
with open(fileName + ".htm", "r") as f:
    lines = f.readlines()

# Convert the HTM file to a legible CSV (assumes a starting balance of $1000)
with open(fileName + ".csv", "w") as f:
	f.write("0,1000\n")
	for line in lines:
		if toExclude not in line and toFind in line:
			line = re.sub(r"<.*?>\s?\<.*?\>", ",", line)
			line = line.split(",")
			f.write(line[-3] + ',' + line[-2] + '\n')

# Creates a Panda dataframe with the results and adds the log returns
df = pd.read_csv(fileName + '.csv', names=['P/L', 'balance'])
df['pct_change'] = df.balance.pct_change()
df['log_ret'] = np.log(df.balance) - np.log(df.balance.shift(1))

# Generates the number of simulations based on the number of trades squared
simCount = (len(df.index)*len(df.index)) * multiplier
mc = df['log_ret'].montecarlo(sims=simCount, bust=dd, goal=target)

# Returns percentage statistics on the simulations
print("===============")
print(mc.stats)
print("Profit:", 1000*(1+mc.stats['min']))
print("Max Drawdown:", 1000*(1+mc.stats['maxdd']))
print("Under ", str(dd*100) ,"% drawdown:", mc.stats['bust'] * 100)
print("Over ", str(target*100) ,"% target:", mc.stats['goal'] * 100)
print("===============")

# Plots the MonteCarlo Simulation
mc.plot(title="Log Returns at " + str(simCount) + " Simulations")
