import pandas as pd

import random
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import scipy



def correlation_with_level(path="./results/comment_results_without_bias.csv", level="avg", human="Usefulness", corr_type="pearson"):
    df = pd.read_csv(path)
    if level == "low":
        df = df.loc[df[human] <= 2, [human, "BLEU", "METEOR", "ROUGE-L", "CIDEr", "SPICE"]]
    elif level == "high":
        df = df.loc[df[human] > 3, [human, "BLEU", "METEOR", "ROUGE-L", "CIDEr", "SPICE"]]
    else:
        df = df.loc[(df[human] <= 3) & (df[human] > 2), [human, "BLEU", "METEOR", "ROUGE-L", "CIDEr", "SPICE"]]
    return df.corr(corr_type)


for human in ["Naturalness", "Expressiveness", "Adequacy", "Conciseness", "Usefulness", "Understandability"]:
    print(correlation_with_level(human=human))




