# NYC_Electricity_Demand_Forecasting

## Project Motivation
For this Project I wanted to analyze the NYC electricity demand enriched using NOAA weather data for NYC whether I could answer the following questions:
- What effect does date & time play in influencing daily electricity demand in NYC?
    - What are the Seasonal (daily, hourly, monthly, etc) patterns in the data?
    - Do holidays or events play any role?
- How viable are traditional ML algorithms in forecasting Day Ahead Elctricity Demand?
- How important are NYC Weather Variables as predictors to forecast energy\electricity demand?

The above questions demonstrate rapid-prototypying and backetesting of ML algorithms for use in electrcicity demand forecasting. This helps businesses optimise resource utilisation and efficient usage of energy. An example of the use of such optimisation could be found in scheduling electrcicty supply by electrcicty regulators\operators\retailers.

## File Descriptions
The notebook titled Download_Data that deals with fetching data from Azure OpenDatasets; a modified version of this [notebook](https://github.com/Azure/OpenDatasetsNotebooks/blob/master/tutorials/energy-join/01-energy-join-weather-in-pandas.ipynb).
[source of data](https://notebooks.azure.com/frlazzeri/projects/automatedml-ms-build/html/nyc_energy.csv)

The notebook titled NYC_Electricity_Demand_Forecasting showcases my work and tries to answer the questions posed above. Some markdown cells peppered throughout the notebook explain the role of each section while a docstring is written for some of the functions used.

## Licensing, Authors, Acknowledgements, etc.
Acknowledgement should go to [Azure Open Datasets](https://azure.microsoft.com/en-us/products/open-datasets) for providing the dataset. Acknowledgement should also go to [Kishan Manani](https://github.com/trainindata/feature-engineering-for-time-series-forecasting) for their through explanation of feature engineering for time series forecasting.