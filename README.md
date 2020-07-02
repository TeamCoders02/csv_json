# About

A python package to convert the CSV (Comma Separated values) format files to the JSON (JavaScript
Object Notation) files and vice versa i.e. JSON files to CSV.

 Open-sourced Package : https://pypi.org/project/csv-json/

# Requirements
 
 Python version >= 3.6

 OS (Windows/MacOS/Linux)

# Installation

Before you can use CSV_JSON, you’ll need to get it installed.

>conda install csv_json

csv_json can be installed via pip from PyPI.

>pip install csv_json

# CSV TO JSON
To convert CSV files to JSON files, import csvjson module from csv_json.

>from csv_json import csvjson as cj

Read the CSV file by passing the CSV file path to read_csv().

>cj.read_csv('CSV file path')

Convert the given CSV file to JSON file by passing the JSON file path to write_json().
You can alternatively pass a list of label as an additional argument to the write_json() if required.

>cj.write_json('JSON file path',label=None)

# JSON TO CSV 

To convert JSON files to CSV files, import the csvjson module from csv_json package.

>from csv_json import csvjson as cj

Read the required JSON file by passing the JSON file path to the read_json().

>cj.read_json('JSON file path') 

Convert the Given JSON file to the CSV file by passing the CSV file path to write_csv().
You can pass list of items(header row) as an additional argument to the write_csv().

>cj.write_csv('CSV file path', head=None)

# Applications

1. JSON format files are widely used in parsoning of the web API's and many more..
2. CSV format files are used for handling the databases for various machine learning and AI models and many more..

# Authors

[Daniel S](https://github.com/godisgreat) and [Harish Kumar S Guragol](https://github.com/HarishGuragol)

