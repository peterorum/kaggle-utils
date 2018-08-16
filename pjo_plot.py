#!/usr/local/bin/python3

import matplotlib.pyplot as plt


def plot_histograms(data):
    data[data.dtypes[(data.dtypes == "float64") | (data.dtypes == "int64")].index.values].hist(figsize=[11, 11])
    plt.show()
