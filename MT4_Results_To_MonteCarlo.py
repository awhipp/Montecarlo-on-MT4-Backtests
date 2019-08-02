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

# The amount for the initial value
initial = 1000

# Max number of simulations
simLimit = 18500

# Read the MT4 Results HTM to memory
with open(fileName + ".htm", "r") as f:
    lines = f.readlines()

# Convert the HTM file to a legible CSV
with open(fileName + ".csv", "w") as f:
    for line in lines:
        if toExclude not in line and toFind in line:
            line = re.sub(r"<.*?>\s?\<.*?\>", ",", line)
            line = line.split(",")
            if initial == 1000:
                initial = float(line[-2])
            f.write(line[-3] + ',' + line[-2] + '\n')

# Creates a Panda dataframe with the results and adds the log returns
df = pd.read_csv(fileName + '.csv', names=['P/L', 'balance'])
df['pct_change'] = df.balance.pct_change()
df['log_ret'] = np.log(df.balance) - np.log(df.balance.shift(1))

# Generates the number of simulations based on the number of trades squared
simCount = int((len(df.index)*len(df.index)) * multiplier)
if simCount > simLimit:
    simCount = simLimit

# Runs the simulations
mc = df['log_ret'].montecarlo(sims=simCount, bust=dd, goal=target)

# Returns percentage statistics on the simulations
print("===============")
print(mc.stats)
print("Profit:", initial*(1+mc.stats['min']))
print("Max Drawdown:", initial*(1+mc.stats['maxdd']))
print("Under ", str(dd*100) ,"% drawdown:", mc.stats['bust'] * 100)
print("Over ", str(target*100) ,"% target:", mc.stats['goal'] * 100)
print("===============")

# Plots the MonteCarlo Simulation
mc.plot(title="Log Returns at " + str(simCount) + " Simulations")
