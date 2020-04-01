import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    mr.emit_intermediate((person, friend), 1)
    mr.emit_intermediate((friend, person), 0)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # print key, list_of_values
    if sum(list_of_values) == 0:
        mr.emit((key[0], key[1]))
        mr.emit((key[1], key[0]))


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)