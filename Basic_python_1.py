data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
        ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
        ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
        ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
        ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
        ['D5', 98], ['D6', 32]]

# How many sites are there? 
print "1. Ans:{}".format(len(data))
print "2. Ans:{}".format(data[6][1])
print "3. Ans:{}".format(data[-1][1])
print "4. Ans:{}".format(sum([i[1] for i in data]))
print "5. Ans:{}".format(sum([i[1] for i in data])/len(data))
print "6. Ans:{}".format(len([i for i in data if "C" in i[0]]))
