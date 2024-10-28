import matplotlib.pyplot as plt
import numpy as np
from shiny import App, ui, render

# Define UI with a page title
app_ui = ui.page_fluid(
    ui.input_slider(
        "chosen_bin_count",  # Bin ID String
        "Bin Count",         # Slider Label
        min=0,               # Min Bin Count
        max=100,             # Max Bin Count
        value=20             # Initial Bin Count
    ),
    ui.output_plot("histogram"),
    title="Shiny Histogram App"  # Move title to the end as a keyword argument
)

# Define server logic
def server(input, output, session):
    @output
    @render.plot(alt="A histogram")
    def histogram():
        np.random.seed(19680801)
        pseudo_random_data = 100 + 15 * np.random.randn(437)
        plt.hist(
            pseudo_random_data,
            bins=input.chosen_bin_count(),  # Fixed input access syntax
            density=True
        )
        plt.title("Random Data with Chosen Bin Count")
        plt.xlabel("Measure")
        plt.ylabel("Normalized Frequency")

# Create the app
app = App(app_ui, server)