#!/usr/bin/env python

import json

import pandas as pd


# Load datapackage.json
with open("datapackage.json") as f:
    dp = json.load(f)


# Load input file and pre-populate data resource
df = pd.read_csv("input.csv")

# Get input data resource to be modified
data_resource = next(i for i in dp["resources"] if i["name"] == "data")

# Generate fields based on data headers
headers = list(df.columns)
fields = []

for header in headers:
    fields.append({
        "name": header,
        "title": header,
        "unit": "",
        "type": "number",
    })

data_resource["fields"] = fields

# Populate data
data_resource["data"] = [ row.to_dict() for i, row in df.iterrows() ]

# Write input.json for testing local execution
with open("input.json", "w") as f:
    input_json = {
        "datapackage": dp,
        "algorithm": "bindfit",
    }

    json.dump(input_json, f, indent=2)
