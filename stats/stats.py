# imports
import os
import pandas as pd
import pingouin as pg
import numpy as np
import seaborn as sns
from scipy.stats import iqr
# implements statsistics for KP 2022 - Artificial Intelligence

# read data
d = {}

for file in os.listdir("/home/m_rosa/SAT/SAT_solver/stats/results/"):
    file_open = open("/home/m_rosa/SAT/SAT_solver/stats/results/" + file, "r")

    # read file
    for line in file_open:
        values = line.strip("\n").split(" ")[1:]
        d[line.split(" ")[0]] = list(map(int, values))
    d["ID"] = list(range(1,7))
print(d)

data_panda = pd.DataFrame.from_dict(data = d)

# repeated measures with sphericity and normal distribution test
data_panda = pd.melt(data_panda.reset_index(), id_vars= ["ID"], value_vars= ["MOM", "JW", "DPLL"])
print(data_panda)
print(pg.rm_anova(data = data_panda, dv = "value",within = "variable", subject = "ID", effsize = "np2", detailed = False, correction = 'auto'))

# post hoc
print(pg.pairwise_tests(dv = "value", within = "variable", subject = "ID", data = data_panda))

# plot
# 50th Percentile
def q25(x):
    return x.quantile(0.25)

# 90th Percentile
def q75(x):
    return x.quantile(0.75)

sns.set()

print("parametric data\n", data_panda.groupby(['variable'])['value'].agg(['mean', 'std']).round(2))
print("non parametric data\n", data_panda.groupby(['variable'])['value'].agg(['median', iqr, q25, q75]).round(2))

plot = sns.pointplot(data=data_panda, x="variable", y="value", errorbar=("pi", 100), capsize=.4, join=True, color="black", estimator = "median")
sns.swarmplot(x="variable", y="value", data=data_panda, edgecolor="black", linewidth=.9)
sns.boxplot(data=data_panda, x="variable", y="value", color="gray", saturation=0.05)
fig = plot.get_figure()
fig.savefig("stats2.png")

