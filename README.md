# About

A python package to convert the CSV (Comma Separated values) format files to the JSON (JavaScript
Object Notation) files and vice versa i.e. JSON files to CSV.

# Requirements
 
 Python version >= 3.6
 OS independent 

# Installation

Before you can use CSV_JSON, you’ll need to get it installed.

>conda install csv_json

csv_json can be installed via pip from PyPI.

>pip install csv_json

# CSV TO JSON

To convert the csv files to json you will need to import csv_To_json class from csv_to_json module in csv_json

>from csv_json.csv_to_json import csv_To_json as csj

Creating the csv_to_json class object

>var = csj()

Passing csv file path through read_csv() method

>var.read_csv(path=“CSV file path”) 

Writing the json file with json file path or the file name to the write_json() method
You can alternatively pass a list of labels if required.

>var.write_json(path=“JSON file path”, label=None) 

# JSON TO CSV 

To convert the csv files to json you will need to import json_To_csv class from json_to_csv module in csv_json package

>from csv_json.json_to_csv import json_To_csv as jsc

Creating a json_to_csv class object

>var = jsc()

Reading json file by passing the json file path to  read_json() method

>var.read_json(path=“JSON file path”) 

Extracting the labels in the json file through get_label() method

>var.get_label()

Write the csv file by passing csv file path to write_csv() method. 
You can alternatively pass head list representing the first row of the csv file if required.

>var.write_csv(path=“csv file path”, head=None) 

# Applications

1. JSON format files are widely used in parsoning of the web API's and many more..
2. CSV format files are used for handling the databases for various machine learning and AI models and many more..

# Authors

[Daniel S](https://github.com/godisgreat) and [Harish Kumar S Guragol](https://github.com/HarishGuragol)

