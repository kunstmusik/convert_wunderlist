# convert_wunderlist.py

Python script to convert from Wunderlist's JSON format to CSV appropriate for Toodledo import.

## Usage

Run the python script with given Wunderlist backup file like so:

```python convert_wunderlist.py wunderlist_xxx.json```

This will generate a toodledo.csv file. 

## Notes

* This script is designed to only import non-completed Todos from Wunderlist.
