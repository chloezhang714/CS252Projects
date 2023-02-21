'''analysis.py
Run statistical analyses and plot Numpy ndarray data
Chloe Zhang
CS 251 Data Analysis Visualization, Spring 2022
'''
import numpy as np
import matplotlib.pyplot as plt


class Analysis:
    def __init__(self, data):
        # '''

        # Parameters:
        # -----------
        # data: Data object. Contains all data samples and variables in a dataset.
        # '''
        self.data = data

        # Make plot font sizes legible
        plt.rcParams.update({'font.size': 18})

    def set_data(self, data):
        self.data = data
        # '''Method that re-assigns the instance variable `data` with the parameter.
        # Convenience method to change the data used in an analysis without having to create a new
        # Analysis object.

        # Parameters:
        # -----------
        # data: Data object. Contains all data samples and variables in a dataset.
        # '''
        # pass

    def min(self, headers, rows=[]):
        data = np.array(self.data.select_data(headers,rows))
        return np.min(data,axis = 0)
        # '''Computes the minimum of each variable in `headers` in the data object.
        # Possibly only in a subset of data samples (`rows`) if `rows` is not empty.
        # (i.e. the minimum value in each of the selected columns)

        # Parameters:
        # -----------
        # headers: Python list of str.
        #     One str per header variable name in data
        # rows: Python list of int.
        #     Indices of data samples to restrict computation of min over, or over all indices
        #     if rows=[]

        # Returns
        # -----------
        # mins: ndarray. shape=(len(headers),)
        #     Minimum values for each of the selected header variables

        # NOTE: Loops are forbidden!
        # '''
        # pass

    def max(self, headers, rows=[]):
        return (self.data.select_data(headers,rows)).max(axis = 0)
        # '''Computes the maximum of each variable in `headers` in the data object.
        # Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        # Parameters:
        # -----------
        # headers: Python list of str.
        #     One str per header variable name in data
        # rows: Python list of int.
        #     Indices of data samples to restrict computation of max over, or over all indices
        #     if rows=[]

        # Returns
        # -----------
        # maxs: ndarray. shape=(len(headers),)
        #     Maximum values for each of the selected header variables

        # NOTE: Loops are forbidden!
        # '''
        # pass

    def range(self, headers, rows=[]):
        return [self.min(headers, rows), self.max(headers, rows)]
        # '''Computes the range [min, max] for each variable in `headers` in the data object.
        # Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        # Parameters:
        # -----------
        # headers: Python list of str.
        #     One str per header variable name in data
        # rows: Python list of int.
        #     Indices of data samples to restrict computation of min/max over, or over all indices
        #     if rows=[]

        # Returns
        # -----------
        # mins: ndarray. shape=(len(headers),)
        #     Minimum values for each of the selected header variables
        # maxes: ndarray. shape=(len(headers),)
        #     Maximum values for each of the selected header variables

        # NOTE: Loops are forbidden!
        # '''
        # pass

    def mean(self, headers, rows=[]):
        data = self.data.select_data(headers,rows)
        return (sum(data)/data.shape[0])
        # '''Computes the mean for each variable in `headers` in the data object.
        # Possibly only in a subset of data samples (`rows`).

        # Parameters:
        # -----------
        # headers: Python list of str.
        #     One str per header variable name in data
        # rows: Python list of int.
        #     Indices of data samples to restrict computation of mean over, or over all indices
        #     if rows=[]

        # Returns
        # -----------
        # means: ndarray. shape=(len(headers),)
        #     Mean values for each of the selected header variables

        # NOTE: You CANNOT use np.mean here!
        # NOTE: Loops are forbidden!
        # '''
        # pass

    def var(self, headers, rows=[]):
        data = self.data.select_data(headers,rows)
        # print(data.shape)
        # print(self.mean(headers,rows).shape)
        diff = data-self.mean(headers,rows)
        # print(diff)
        sqr = diff * diff
        # print(sqr)
        # print(np.sum(sqr, axis = 0))
        return np.sum(sqr, axis = 0) /(data.shape[0]-1)
        # '''Computes the variance for each variable in `headers` in the data object.
        # Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        # Parameters:
        # -----------
        # headers: Python list of str.
        #     One str per header variable name in data
        # rows: Python list of int.
        #     Indices of data samples to restrict computation of variance over, or over all indices
        #     if rows=[]

        # Returns
        # -----------
        # vars: ndarray. shape=(len(headers),)
        #     Variance values for each of the selected header variables

        # NOTE: You CANNOT use np.var or np.mean here!
        # NOTE: Loops are forbidden!
        # '''
        # pass

    def std(self, headers, rows=[]):
        return np.sqrt(self.var(headers,rows))
        # '''Computes the standard deviation for each variable in `headers` in the data object.
        # Possibly only in a subset of data samples (`rows`) if `rows` is not empty.

        # Parameters:
        # -----------
        # headers: Python list of str.
        #     One str per header variable name in data
        # rows: Python list of int.
        #     Indices of data samples to restrict computation of standard deviation over,
        #     or over all indices if rows=[]

        # Returns
        # -----------
        # vars: ndarray. shape=(len(headers),)
        #     Standard deviation values for each of the selected header variables

        # NOTE: You CANNOT use np.var, np.std, or np.mean here!
        # NOTE: Loops are forbidden!
        # '''
        # pass

    def show(self):
        # '''Simple wrapper function for matplotlib's show function.

        # (Does not require modification)
        # '''
        plt.show()

    def scatter(self, ind_var, dep_var, title = ''):
        x = self.data.select_data([ind_var])
        y = self.data.select_data([dep_var])
        plt.scatter(x,y)
        plt.title(title)
        plt.xlabel(ind_var)
        plt.ylabel(dep_var)
        return x,y
        # '''Creates a simple scatter plot with "x" variable in the dataset `ind_var` and
        # "y" variable in the dataset `dep_var`. Both `ind_var` and `dep_var` should be strings
        # in `self.headers`.

        # Parameters:
        # -----------
        # ind_var: str.
        #     Name of variable that is plotted along the x axis
        # dep_var: str.
        #     Name of variable that is plotted along the y axis
        # title: str.
        #     Title of the scatter plot

        # Returns:
        # -----------
        # x. ndarray. shape=(num_data_samps,)
        #     The x values that appear in the scatter plot
        # y. ndarray. shape=(num_data_samps,)
        #     The y values that appear in the scatter plot

        # NOTE: Do not call plt.show() here.
        # '''
        # pass

    def pair_plot(self, data_vars, fig_sz=(12, 12), title = 'Pair Plot'):
        dim = len(data_vars)
        fig, axs = plt.subplots(dim,dim, figsize=fig_sz, sharex='none')
        for i in range(dim):
            for j in range(dim):
                    if j == 0:
                        axs[i, j].set(ylabel=data_vars[i])
                    if i == dim-1:
                        axs[i, j].set(xlabel=data_vars[j])
                    x = self.data.select_data([data_vars[i]])
                    y = self.data.select_data([data_vars[j]])
                    axs[i, j].scatter(x,y)
                    axs[i, j].set_xticks([])
                    axs[i, j].set_yticks([])
        fig.subplots_adjust(hspace = 0.5, wspace = 0.3)
        fig.suptitle(title)
        return (fig,axs)
        # '''Create a pair plot: grid of scatter plots showing all combinations of variables in
        # `data_vars` in the x and y axes.

        # Parameters:
        # -----------
        # data_vars: Python list of str.
        #     Variables to place on either the x or y axis of the scatter plots
        # fig_sz: tuple of 2 ints.
        #     The width and height of the figure of subplots. Pass as a paramter to plt.subplots.
        # title. str. Title for entire figure (not the individual subplots)

        # Returns:
        # -----------
        # fig. The matplotlib figure.
        #     1st item returned by plt.subplots
        # axes. ndarray of AxesSubplot objects. shape=(len(data_vars), len(data_vars))
        #     2nd item returned by plt.subplots

        # TODO:
        # - Make the len(data_vars) x len(data_vars) grid of scatterplots
        # - The y axis of the first column should be labeled with the appropriate variable being
        # plotted there.
        # - The x axis of the last row should be labeled with the appropriate variable being plotted
        # there.
        # - There should be no other axis or tick labels (it looks too cluttered otherwise!)

        # Tip: Check out the sharex and sharey keyword arguments of plt.subplots.
        # Because variables may have different ranges, pair plot columns usually share the same
        # x axis and rows usually share the same y axis.
        # '''
        # pass