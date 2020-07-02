from csv_json.csv_to_json import csv_to_json
from csv_json.json_to_csv import json_to_csv


csj=csv_to_json()
jsc= json_to_csv()
def read_csv(path):
    csj.read_cs(path)
def write_json(path=None):
    csj.write_js(path)
def read_json(path):
    jsc.read_js(path)
def write_csv(path=None):
    jsc.write_cs(path)
