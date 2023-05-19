#!/usr/bin/env python

import json

# Load datapackage template
with open("template.json") as f:
  dp = json.load(f)

# Populate template items from individual json subdirectories
def populate_items(dp, key):
    items = []
    for i in dp[key]:
        with open(key + "/" + i["name"] + ".json") as f:
            items.append(json.load(f))
    dp[key] = items

# TODO: Populate code in algorithms

for key in ["algorithms", "resources", "views", "displays"]:
    populate_items(dp, key)

# Write complete datapackage to single file
with open("datapackage.json", "w") as f:
    json.dump(dp, f, indent=2)

print("Datapackage written to datapackage.json")
