# Week 9: Time Series Basics

## Purpose

This folder contains the Week 9 internship deliverable on basic time series analysis and forecasting.

The notebook uses a monthly sales dataset to practice time series concepts, time-based aggregation, rolling averages, resampling, and simple forecasting methods.

## Requirements Covered

- Understand the difference between time series data and regular tabular data.
- Study trend and seasonality.
- Create and explore a time series dataset.
- Convert dates to datetime format.
- Use a DatetimeIndex.
- Practice time-based aggregation.
- Calculate rolling averages.
- Resample data by month and week.
- Implement a simple moving-average forecast.
- Implement a basic linear-trend forecast.
- Forecast future periods.
- Interpret the observed trend.
- Write a summary of findings and possible explanations.

## Dataset

The notebook uses a synthetic monthly sales dataset covering 36 months from January 2023 through December 2025.

The dataset is created directly in the notebook so that the analysis is reproducible without requiring an external data file.

Because the dataset is synthetic and educational, observed patterns should not be interpreted as evidence about a real business.

## Forecasting Methods

Two simple forecasting approaches are demonstrated:

1. **3-month moving-average forecast**
   - Uses recent observations to estimate the next month's sales.
   - The forecast is shifted by one period to avoid using the current month's actual value.

2. **Linear-trend forecast**
   - Fits a simple straight-line trend to historical sales.
   - The trend is extended to forecast the next six months.

## Files

- `Week_09_Time_Series.ipynb` — completed time series analysis notebook.
- `README.md` — documentation for the Week 9 project.

## How to Run

1. Open Jupyter Notebook or JupyterLab.
2. Open `Week_09_Time_Series.ipynb`.
3. Run the notebook from beginning to end.
4. Review the charts, forecasts, findings, and final summary.

## Submission Check

Before committing:

- Confirm that the notebook runs without errors.
- Confirm that all charts and forecast outputs are displayed.
- Confirm that the final written summary is included.
- Save the notebook before committing.