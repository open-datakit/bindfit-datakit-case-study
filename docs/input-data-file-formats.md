# Input data file formats

## NMR and UV 1:1, 1:2, 2:1

### Rows

* Row 1 - Headers (required)
* Rows 2-N - Data

### Columns

* Column 1 - Host concentration
* Column 2 - Guest concentration
* Columns 2-X - Measured (raw) data with X = n + 2, where n is the number of chemical shifts measured

### Example table

| Host     | Guest    | Variable 1 | Variable 2 | Variable N |
| -------- | -------- | ---------- | ---------- | ---------- |
| Required | Required | Required   | Optional   | ...        |
| ...      | ...      | ...        | ...        | ...        |

## NMR and UV Dimer/CoEK Aggregation

### Example table

| H total  | Variable 1 | Variable 2 | Variable N |
| -------- | ---------- | ---------- | ---------- |
| Required | Required   | Optional   | ...        |
| ...      | ...        | ...        | ...        |
