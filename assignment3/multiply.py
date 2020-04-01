import MapReduce
import sys

N = 5

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix == 'a':
        for k in range(N):
            mr.emit_intermediate((i, k), (matrix, j, value))
    else:
        for k in range(N):
            mr.emit_intermediate((k, j), (matrix, i, value))

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # print key, list_of_values
    vec_a = [(item[1], item[2]) for item in list_of_values if item[0] == 'a']
    vec_b = [(item[1], item[2]) for item in list_of_values if item[0] == 'b']
    total = 0
    for a in vec_a:
        for b in vec_b:
            if a[0] == b[0]:
                total += a[1]*b[1]
    mr.emit((key[0], key[1], total))


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)