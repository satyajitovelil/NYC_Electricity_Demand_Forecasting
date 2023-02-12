import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def create_sns_plot(df, x, y, col, hue, units):
    
    """
    Return the grid plot timeseries grouped by col, hue and unit.

    Parameter
    ---------
    df : pd.DataFrame
        Dataframe used to plot the grid.
    x : str
        column Name of X axis in each of the plots part of the grid.
    y : str
        column Name of Y axis in each of the plots part of the grid.
    col : str
        column Name of Variable used to separate the plots.
    hue : str
        column Name of Variable used to group the relplot.
    units : str
        column Name of Variable used to group the lineplot.

    Returns
    -------
    seaborn.FacetGrid
        FacetGrid for multiple time series.
    """

    sns.set_theme(style="dark")
    g = sns.relplot(
        data=df,
        x=x, y=y, col=col, hue=hue,
        kind="line", palette="crest", linewidth=4, 
        # zorder=5,
        col_wrap=3, 
        height=2, 
        aspect=1.5, 
        legend=False,
    )

    for fig, ax in g.axes_dict.items():

        ax.text(.8, .85, fig, transform=ax.transAxes, fontweight="bold")

        sns.lineplot(
            data=df, x=x, y=y, units=units,
            estimator=None, color=".7", linewidth=1, ax=ax,
        )

    # Reduce the frequency of the x axis ticks
    ax.set_xticks(ax.get_xticks()[::2])

    # Tweak the supporting aspects of the plot
    g.set_titles("")
    g.set_axis_labels("", "Demand")
    g.tight_layout()

class plotwindow:
    '''
    Helps visualise a time window of seasonal and residual components by iterating over a date range. 
    '''

    def __init__(self, decomp, freq):
        '''
        Init Function. 
        Args:
            decomp: the result returned by statsmodels seasonal decompose function.
            freq: the date range to iterate over. 
        Returns:
            Initializes the class for iterative plotting plot of seasonal and residual components.
        '''
        self.get_date_range(decomp, freq)
        self.right_dt_bound = self.date_range[1:]
        self.left_dt_bound = self.date_range[:-1]
        self.strafe = zip(self.left_dt_bound, self.right_dt_bound)
        self.seasonal_df = pd.DataFrame(decomp.seasonal)
        self.residual_df = pd.DataFrame(decomp.resid)

    def get_date_range(self, decomp, freq):
        st = decomp.observed.index.min()
        en = decomp.observed.index.max()
        self.date_range = pd.date_range(start=st, end=en, freq=freq)

    def plot(self):
        '''
        Plots the Components. 
        Args:
            self: Takes args initialized by the Class.
        Returns:
            plots the next window of seasonal and residual components.
        '''
        next_window = next(self.strafe)
        ax = self.seasonal_df.loc[next_window[0]:next_window[1], :].plot(sharey=False)
        self.residual_df.loc[next_window[0]:next_window[1], :].plot(ax=ax, sharey=False)
        plt.show()
