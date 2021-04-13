# CSV-Combiner
Uses Python 3 and pandas to combine two csv files, adding a column to the end displaying the original file. Can run using:
```
.\csv_combiner.py accessories.csv clothing.csv > output.csv
```
This syntax (or just csv_combiner.py without ".\") appliers to Windows and may be slightly different on a Unix machine. Python 3 and pandas need to be installed to run the script. Pandas comes by default with the Anaconda distribution or can be installed using pip.
To run the tests in test_csv_combiner.py, pytest needs to be installed as well.

It takes slightly less than 15 minutes to process two files slightly larger than 2 GB on a 2013 Macbook Pro. This was tested using the
train_timeseries.csv file from [here](https://www.kaggle.com/cdminix/us-drought-meteorological-data), though the file is not included in this repository
due to its size.
