class Order:

    def __init__(self):
        self.befores = dict()
        self.page_lists = []

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

            # section 1, build list map
            first_section = True
            for line in lines:
                if line == "\n":
                    first_section = False
                    continue

                if first_section:
                    order = line.strip().split('|')
                    self.befores.setdefault(int(order[1]), set())
                    self.befores[int(order[1])].add(int(order[0]))
                else:
                    self.page_lists.append([int(x) for x in line.strip().split(',')])
        f.close()

    def add_middle_column(self):
        total = 0
        sorted_total = 0
        for page_list in self.page_lists:

            violation = False
            # For each page element ask, should any right hand values be to my left?
            for page_index in range(0, len(page_list)):

                # get values to the right
                pages_right = set(page_list[page_index:])

                # check if values that come after and before intersect, thats a violation
                if page_list[page_index] not in self.befores:
                    continue

                must_be_to_left = set(self.befores[page_list[page_index]])
                if not pages_right.isdisjoint(must_be_to_left):
                    violation = True
                    break
            if not violation:
                total = total + page_list[len(page_list) // 2]
            else:
                page_list = self._sort(page_list)
                sorted_total = sorted_total + page_list[len(page_list) // 2]

        return total, sorted_total

    def topo_sort(a, b):
        if a < b:
            return -1  # a comes before b
        elif a > b:
            return 1  # a comes after b
        else:
            return 0  # a and b are equal


    # Sort using the custom comparator
    # sorted_list = sorted(my_list, key=cmp_to_key(custom_comparator))
    # print(sorted_list)  # Output: [1, 2, 3, 4, 5, 8]

    def _sort(self, page_list):

        # using a franken-bubble sort variation, data structure not optimal for kahns
        # so using this partial topology bubble sort
        for i in range(len(page_list)):
            matches = []
            for j in range(1, len(page_list)):
                curr = page_list[j]
                if page_list[0] not in self.befores: # no ordering specified
                    continue
                if curr in self.befores[page_list[0]]:
                    matches.append(curr)
                    page_list.remove(curr) # duplicates edge case to keep eye on
                page_list = matches + page_list
        return page_list




