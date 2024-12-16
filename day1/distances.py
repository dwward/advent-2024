class Distances:

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            values = line.split("   ")
            self.list1.append(int(values[0]))
            self.list2.append(int(values[1]))
        f.close()

    def calculate(self):
        total = 0
        self.list1.sort()
        self.list2.sort()
        for i in range(0, len(self.list1)):
            distance = abs(self.list1[i] - self.list2[i])
            total = total + distance
        return total





