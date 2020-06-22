# CSV_JSON

A python package to convert the CSV (Comma Separated values) format files to the JSON (JavaScript
Object Notation) files and vice versa i.e. JSON files to CSV.

# INSTALLATION

Before you can use CSV_JSON, you’ll need to get it installed.

>conda install csv_json

csv_json can be installed via pip from PyPI.

>pip install csv_json

# USAGE

To convert the csv files to json you will need to import the package csv_To_json

>from CSV_JSON import csv_To_json

>var = csv_to_json.csv_to_json()

>var.input(“CSV file path”) 

>var.write_json(“JSON file path”) 

To convert the csv files to json you will need to import the package json_To_csv

>from CSV_JSON import json_To_csv

>var = json_to_csv.json_to_csv ()

>var.input(“JSON file path”) 

>var.write_csv(“csv file path”) 
