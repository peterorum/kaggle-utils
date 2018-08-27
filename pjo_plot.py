#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import seaborn as sns


def plot_histograms(data):
    data[data.dtypes[(data.dtypes == "float64") | (data.dtypes == "int64")].index.values].hist(figsize=[11, 11])
    plt.show()

# Plots the disribution of a variable colored by value of the target


def plot_target_correlation(var_name, target, df):

    # Calculate the correlation coefficient between the new variable and the target
    corr = df[target].corr(df[var_name])

    # Calculate medians for repaid vs not repaid
    avg_repaid = df.ix[df[target] == 0, var_name].median()
    avg_not_repaid = df.ix[df[target] == 1, var_name].median()

    plt.figure(figsize=(12, 6))

    # Plot the distribution for target == 0 and target == 1
    sns.kdeplot(df.ix[df[target] == 0, var_name], label='TARGET == 0')
    sns.kdeplot(df.ix[df[target] == 1, var_name], label='TARGET == 1')

    # label the plot
    plt.xlabel(var_name)
    plt.ylabel('Density')
    plt.title('%s Distribution' % var_name)
    plt.legend()

    # print out the correlation
    print('The correlation between %s and the TARGET is %0.4f' % (var_name, corr))
    # Print out average values
    print('Median value for loan that was not repaid = %0.4f' % avg_not_repaid)
    print('Median value for loan that was repaid =     %0.4f' % avg_repaid)
