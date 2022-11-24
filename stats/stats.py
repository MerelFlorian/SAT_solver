# imports
import os
import pandas as pd
import pingouin as pg
import numpy as np
import seaborn as sns
from scipy.stats import iqr
import matplotlib.pyplot as plt
# implements statsistics for KP 2022 - Artificial Intelligence

# read data
d = {}

for file in os.listdir("/home/m_rosa/SAT/SAT_solver/stats/results/"):
    file_open = open("/home/m_rosa/SAT/SAT_solver/stats/results/" + file, "r")

    d["ID"] = []
    d["amount of splits"] = []
    d["heuristic"] = []
    # read file
    for line in file_open:
        value = line.strip("\n").split(";")[1]
        algorithm = line.strip("\n").split(";")[0]
        ID = line.strip("\n").split(";")[2]
        # d[line.split(" ")[0]] = list(map(int, value))
        d["ID"].append(ID)
        d["amount of splits"].append(float(value))
        d["heuristic"].append(algorithm)
print(d)

data_panda = pd.DataFrame.from_dict(data = d)
print(data_panda)

# repeated measures with sphericity and normal distribution test
# data_panda = pd.melt(data_panda.reset_index(), id_vars= ["ID"], value_vars= ["MOM", "JW", "DPLL"])
print(data_panda)
print("RM ANOVA \n", pg.rm_anova(data = data_panda, dv = "amount of splits",within = "heuristic", subject = "ID", effsize = "np2", detailed = False, correction = 'auto'), "\n")

# post hoc
print("POST HOC \n", pg.pairwise_tests(dv = "amount of splits", within = "heuristic", subject = "ID", data = data_panda))

# plot
# min
def min(x):
    return x.quantile(0)

# 50th Percentile
def q25(x):
    return x.quantile(0.25)

# 90th Percentile
def q75(x):
    return x.quantile(0.75)

# max 
def max(x):
    return x.quantile(1)

sns.set()

print("parametric data\n", data_panda.groupby(['heuristic'])['amount of splits'].agg(['mean', 'std']).round(2))
print("non parametric data\n", data_panda.groupby(['heuristic'])['amount of splits'].agg(['median', iqr, q25, q75, min, max]).round(2))

plot = sns.pointplot(data=data_panda, x="heuristic", y="amount of splits", errorbar=("pi", 100), capsize=.4, join=True, color="black", estimator = "median")
sns.swarmplot(x="heuristic", y="amount of splits", data=data_panda, edgecolor="black", linewidth=.9)
sns.boxplot(data=data_panda, x="heuristic", y="amount of splits", color="gray", saturation=0.05)
fig = plot.get_figure()
fig.suptitle('Amount of splitting to find a solution')
fig.savefig("stats2.png")

df = data_panda
plot = sns.catplot(kind = "point", data = data_panda, x="heuristic", y="amount of splits", hue = "ID", order = ["DPLL", "MOM", "JW"])
plt.savefig('output.png')