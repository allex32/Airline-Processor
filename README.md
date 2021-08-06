# Installation

To install the dependencies, run the following (you'll need at least Python 3.7):

```
py -m venv myenv
pip install -r requirements.txt
```

# What the library does

The `schedule_data_processing` library connects to an Azure Blob Storage container and
downloads three files containing simplified schedule data for a fictitious airline.

It has two modes, depending on the parameters passed. 

In `lookup` mode it prints a string to the console containing information for a single flight.

In `merge` mode it joins together all three input files and outputs the result in CSV format.


# Usage

## Merge

To generate the merged schedule dataset provide the keyword `merge`:

```
python schedule_data_processing/app.py merge
```

The output will be saved as ```output.csv``` file

## Processing

To look up an individual flight record provide the keyword `lookup` 
followed by the flight number, e.g.:

```
python schedule_data_processing/app.py lookup ZG2362
```

To look up more than one flight record (the output JSON strings will be separated 
by newlines), provide a list of flights separated by commas, e.g.

```
python schedule_data_processing/app.py lookup ZG2361,ZG2362
```
