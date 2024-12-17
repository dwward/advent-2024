class Levels:

    def __init__(self):
        self.level_list = []

    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            values = list(map(int, line.split(" ")))
            self.level_list.append(values)
        f.close()

    # The levels are either all increasing or all decreasing.  Any two adjacent levels differ by at least one and at
    # most three.
    def _is_safe(self, levels, dampen=False):
        is_increasing = self._is_strict_monotonic(levels.copy(), dampen, True)
        is_decreasing = self._is_strict_monotonic(levels.copy(), dampen, False)
        return is_increasing or is_decreasing

    def _is_step_valid(self, val1, val2, increasing=True):
        diff = val2 - val1
        if increasing:
            return 1 <= diff <= 3
        else:
            return -3 <= diff <= -1

    def _is_strict_monotonic(self, values, dampen=False, increasing=True):
        for i in range(0, len(values) - 1):

            # step check
            if not self._is_step_valid(values[i], values[i + 1], increasing):
                if dampen:

                    # Next to last item
                    if i == len(values) - 2:
                        values.pop(i + 1)

                    # At least two possibilities, compare (i, i+2) and (i+2, i+3).  If both are valid
                    # then choose the greater value (always i)
                    elif i < len(values) - 2:
                        comparison1 = self._is_step_valid(values[i], values[i + 2], increasing)
                        comparison2 = self._is_step_valid(values[i + 1], values[i + 2], increasing)

                        if comparison1 and comparison2:
                            values.pop(i + 1)
                        elif comparison1 and not comparison2:
                            values.pop(i + 1)
                        elif not comparison1 and comparison2:
                            values.pop(i)

                    return self._is_strict_monotonic(values, False, increasing)
                return False

        return True

    def count_safe(self, dampened=False):
        total = 0
        for lvl in self.level_list:
            if not lvl:
                exception = "Level is empty"
                raise Exception(exception)

            if self._is_safe(lvl, dampened):
                total = total + 1
        return total
