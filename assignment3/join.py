import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    #print key, value
    mr.emit_intermediate(key, value)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print key, list_of_values
    total = []
    for order in list_of_values:
        if order[0] == 'order':
            matches = (find_matches(order, list_of_values))
            for match in  matches:
                mr.emit(match)

def find_matches(order, line_items):
    order_matches = []
    for line_item in line_items:
        if line_item[0] == 'line_item' and order[1] == line_item[1]:
            order_matches.append(order + line_item)
    return order_matches

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)