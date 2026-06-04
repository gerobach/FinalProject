import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def style_chart(
    title,
    xlabel,
    ylabel,
    legend_title=None,
    legend_outside=True,
    grid_axis="y",
    rotation=0,
    chart_bg="#f8ead6"
):

    # Title
    plt.title(
        title,
        fontsize=16,
        fontweight="bold",
        pad=15
    )

    # Axis labels
    plt.xlabel(
        xlabel,
        fontsize=12
    )

    plt.ylabel(
        ylabel,
        fontsize=12
    )

    # X tick formatting
    plt.xticks(
        rotation=rotation,
        ha="right" if rotation else "center"
    )

    # Legend
    if legend_title:

        if legend_outside:
            plt.legend(
                title=legend_title,
                frameon=False,
                bbox_to_anchor=(1.02, 1),
                loc="upper left"
            )

        else:
            plt.legend(
                title=legend_title,
                frameon=False
            )

    # Background colours
    plt.gcf().set_facecolor(chart_bg)
    plt.gca().set_facecolor(chart_bg)

    # Styling
    sns.despine()

    plt.grid(
        axis=grid_axis,
        alpha=0.3,
        color="#d8c7ae"
    )

    plt.tight_layout()