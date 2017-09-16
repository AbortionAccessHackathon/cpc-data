# DEPENDENCIES:
# pip install fuzzywuzzy[speedup]

from fuzzywuzzy import process
from multiprocessing import Pool

DATA_FILE_NAME = "data.csv"
DATA_NAME_INDEX = 0

SEARCH_FILE_NAME = "search.csv"
SEARCH_NAME_INDEX = 0

SEPERATOR = ','

CORES = 4

# Parses data file and returns a dictionary from
# a lower case name to an array of all the log lines
# for that name
def read_file(filename, key_index):
    data = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            name = line.split(SEPERATOR)[key_index].lower()
            if name not in data:
                data[name] = []
            data[name].append(line)
    return data

def union_record(name):
    match = process.extractOne(name, data_file.keys())
    unioned_record = [str(match[1])] + search_file[name] + data_file[match[0]]
    return SEPERATOR.join(unioned_record)

data_file = read_file(DATA_FILE_NAME, DATA_NAME_INDEX)
search_file = read_file(SEARCH_FILE_NAME, SEARCH_NAME_INDEX)
unioned_records = Pool(CORES).map(union_record, search_file.keys())

# OUTPUT: CSV that results in a file with each line containing
# Match Confidence, Input Search Lines, All Matched Records
print '\n'.join(unioned_records)
