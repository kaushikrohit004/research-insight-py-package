__version__ = "0.1.0"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Analyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary(self):
        return self.df.describe(include='all')

    def missing_report(self):
        return self.df.isna().sum()

    def plot_correlations(self):
        plt.figure(figsize=(8,6))
        sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm")
        plt.show()

def analyze(df: pd.DataFrame):
    return Analyzer(df)