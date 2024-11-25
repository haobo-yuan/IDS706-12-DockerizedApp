import pytest
import pandas as pd
import os
from main import preprocess_data, generate_plot


# Test the preprocess_data function
def test_preprocess_data():
    # Call the function
    data = preprocess_data()

    # Assert the returned object is a DataFrame
    assert isinstance(
        data, pd.DataFrame
    ), "The returned object should be a pandas DataFrame."

    # Assert the required columns exist
    assert "mean" in data.columns, "'mean' column is missing in the output DataFrame."
    assert (
        "median" in data.columns
    ), "'median' column is missing in the output DataFrame."
    assert "std" in data.columns, "'std' column is missing in the output DataFrame."


# Test the generate_plot function
def test_generate_plot():
    # Prepare dummy data for testing
    data = pd.DataFrame(
        {"mean": [100, 110, 120], "median": [90, 100, 110], "std": [5, 6, 7]},
        index=[2019, 2020, 2021],
    )

    # Call the function
    generate_plot(data)

    # Check if the plot file is created
    assert os.path.exists("plot.png"), "The plot file was not created."

    # Clean up the generated plot file after the test
    os.remove("plot.png")
