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

    # Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest
    # left number with the second-smallest right number, and so on.
    def distance(self):
        total = 0
        self.list1.sort()
        self.list2.sort()
        for i in range(0, len(self.list1)):
            distance = abs(self.list1[i] - self.list2[i])
            total = total + distance
        return total

    # Calculate a total similarity score by adding up each number in the left list after multiplying it by the number
    # of times that number appears in the right list.
    def similarity(self):
        total = 0
        self.list1.sort()
        self.list2.sort()
        for i in range(0, len(self.list1)):
            occurrences = self.list2.count(self.list1[i])
            similarity = occurrences * self.list1[i]
            total = total + similarity
        return total




