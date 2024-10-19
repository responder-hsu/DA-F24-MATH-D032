#!/usr/bin/env python3
import click
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


@click.command()
@click.option("--min-x", default=0, help="Min. of x")
@click.option("--max-x", default=2 * np.pi, help="Max. of x")
@click.option("--min-pi-x", default=None, help="Min. of x in pi")
@click.option("--max-pi-x", default=None, help="Max. of x in pi")
@click.option("--amplitude", "-A", default=1.0, help="Amplitude (A) of the sine wave.")
@click.option("--frequency", "-B", default=1.0, help="Frequency (B) of the sine wave.")
@click.option("--phase", "-C", default=0.0, help="Phase shift (C) of the sine wave.")
@click.option(
    "--vertical-shift",
    "-D",
    "vertical_shift",
    default=0.0,
    help="Vertical shift (D) of the sine wave.",
)
@click.option(
    "--csv-file",
    "-f",
    default=None,
    help="Path to the CSV file containing data to plot.",
)
@click.option(
    "--csv-x-column",
    default=None,
    help="Column name in the CSV which will be used as x.",
)
@click.option(
    "--csv-y-column",
    default=None,
    help="Column name in the CSV which will be used as y.",
)
@click.option(
    "--csv-data-label",
    default=None,
    help="Label name used for the CSV data in graph.",
)
@click.option(
    "--output",
    "-o",
    default="sine_wave_with_data.jpg",
    help="Output file name for the graph.",
)
@click.option(
    "--title",
    default="Sine Wave with CSV Data",
    help="Title of the graph.",
)
def plot_sine_with_data(
    min_x,
    max_x,
    min_pi_x,
    max_pi_x,
    amplitude,
    frequency,
    phase,
    vertical_shift,
    csv_file,
    csv_x_column,
    csv_y_column,
    csv_data_label,
    output,
    title,
):
    # Generate x values from min_x to max_x
    if min_pi_x is not None and max_pi_x is not None:
        x = np.linspace(min_pi_x * np.pi, max_pi_x * np.pi, 1000)
    else:
        x = np.linspace(min_x, max_x, 1000)

    # Calculate y values using the general form of the sine function
    label = f"y = {amplitude} * sin({frequency} * x - {phase}) + {vertical_shift}"
    print(f"Generating {label}")
    y = amplitude * np.sin(frequency * x - phase) + vertical_shift

    # Create the plot for the sine wave
    plt.plot(
        x,
        y,
        label=label,
        color="b",
    )

    # If a CSV file is provided, load the data and plot it
    if csv_file:
        try:
            data = pd.read_csv(csv_file)
            if csv_x_column in data.columns and csv_y_column in data.columns:
                plt.scatter(
                    data[csv_x_column],
                    data[csv_y_column],
                    label=csv_data_label,
                    color="r",
                )
            else:
                print('CSV file must contain columns "x" and "y"')
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    # Add labels and a title
    plt.xlabel("Day Number")
    plt.ylabel("Hours")
    plt.title(title)

    # Add a legend
    plt.legend()

    # Display grid
    plt.grid()

    # Save the plot as a jpg file
    plt.savefig(output)
    print(f"Graph saved as '{output}'")


if __name__ == "__main__":
    plot_sine_with_data()
