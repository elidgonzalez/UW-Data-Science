import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    sequence_id = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[0:-10], sequence_id)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # print key, list_of_values
    mr.emit(key)


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)