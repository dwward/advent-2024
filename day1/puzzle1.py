list1 = []
list2 = []

with open('puzzle1.input', 'r') as f:
    lines = f.readlines()

for line in lines:
    values = line.split("   ")
    list1.append(values[0])
    list2.append(values[1])

print(list2)

f.close()
