# imports
import os
import pandas as pd
import pingouin as pg
import numpy as np
import seaborn as sns
from scipy.stats import iqr
import matplotlib.pyplot as plt
import scikit_posthocs as sp 

# implements statsistics for KP 2022 - Artificial Intelligence

# read data
d = {}

for file in os.listdir("/home/m_rosa/SAT/SAT_solver/stats/results/"):
    file_open = open("/home/m_rosa/SAT/SAT_solver/stats/results/" + file, "r")

    d["ID"] = []
    d["amount of splitting"] = []
    d["heuristic"] = []
    # read file
    for line in file_open:
        value = line.strip("\n").split(";")[1]
        algorithm = line.strip("\n").split(";")[0]
        ID = line.strip("\n").split(";")[2]
        # d[line.split(" ")[0]] = list(map(int, value))
        d["ID"].append(ID)
        d["amount of splitting"].append(float(value))
        d["heuristic"].append(algorithm)

data_panda = pd.DataFrame.from_dict(data = d)
# # shapiro wilk test
# print("SHAPIRO\n", pg.normality(data = data_panda, dv= "amount of splitting", group="heuristic", alpha = 0.05))

# # repeated measures with sphericity and normal distribution test
# # data_panda = pd.melt(data_panda.reset_index(), id_vars= ["ID"], value_vars= ["MOM", "JW", "DPLL"])
# print("RM ANOVA \n", pg.rm_anova(data = data_panda, dv = "amount of splitting",within = "heuristic", subject = "ID", effsize = "np2", detailed = False, correction = 'auto'), "\n")

# # post hoc parametrical
# print("POST HOC","\n", pg.pairwise_tests(dv = "amount of splitting", within = "heuristic", subject = "ID", data = data_panda))

# Friedman (non parametric)
print(pg.friedman(data = data_panda, dv = "amount of splitting", within = "heuristic", subject = "ID"))

# post hoc non parametrical
print(sp.posthoc_conover_friedman(a = data_panda, y_col = "amount of splitting", group_col = "heuristic", block_col= "ID", p_adjust= "fdr_bh", melted = True))

# descriptive data
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


# print("parametric data\n", data_panda.groupby(['heuristic'])['amount of splitting'].agg(['mean', 'std']).round(2))
print("non parametric data\n", data_panda.groupby(['heuristic'])['amount of splitting'].agg(['median', iqr, q25, q75, min, max]).round(2))

# plotting

sns.set(font_scale = 1)
# sns.set_palette("OrRd")

# boxplot
# plot = sns.swarmplot(x="heuristic", y="amount of splitting", data=data_panda, edgecolor="black", linewidth=.9)
plot = sns.boxplot(data=data_panda, x="heuristic", y="amount of splitting", saturation=0.05, showfliers = True, palette = "dark", orient="v")
plot.set(yscale = "log")

fig = plot.get_figure()
fig.savefig("boxplot.png")

# lineplot connections between sudokus
plt.clf()
df = data_panda
sns.set(font_scale = 3)
plot = sns.catplot(kind = "point", data = data_panda, x="heuristic", y="amount of splitting", hue = "ID", order = ["DPLL", "MOM", "JW"], legend = False, color = "black", height = 15, margin_titles=True, palette = "dark")
plot.set(yscale="log")
# plot.set(xticklabels=[])
plt.grid()
plt.savefig('connections.png')

# # histogram
# plt.clf()
# plot = sns.barplot(data=df, x="heuristic", y = "amount of splitting", color="gray", errorbar="sd")
# plt.savefig('histogram.png')
