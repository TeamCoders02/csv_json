# csv_json
A repository for converting csv files to json files and vice-versa
CSV_JSON:
A python package to convert the CSV (Comma Separated values) format files to the JSON (JavaScript
Object Notation) files and vice versa i.e. JSON files to CSV.
INSTALLATION
Before you can use CSV_JSON, you’ll need to get it installed.
conda install csv_json
Pandas can be installed via pip from PyPI.
pip install csv_json
USAGE
To convert the csv files to json you will need to import the package csv_To_json
from CSV_JSON import csv_To_json
var = csv_to_json.csv_to_json ()
var.input(“CSV file path”) #Input the path where the csv file is located
var.write_json(“JSON file path”) #Input the path where the Json file need to be stored
To convert the csv files to json you will need to import the package json_To_csv
from CSV_JSON import json_To_csv
var = json_to_csv.json_to_csv ()
var.input(“JSON file path”) #Input the path where the json file is located
var.write_csv(“csv file path”) #Input the path where the csv file need to be stored
