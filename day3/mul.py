import re


class Mul:

    def __init__(self):
        # Each string line of the file
        self.mul_lines = []
        self.enabled = True


    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        for line in lines:
            self.mul_lines.append(line)
        f.close()

    def parse_mul(self, str):
        regex = r"[-]?\d{1,3}"
        matches = re.findall(regex, str)
        matches[0] = int(matches[0])
        matches[1] = int(matches[1])
        return matches

    # Returns a list of matches
    def parse_muls(self, str):
        regex = r"mul\([-]?\d{1,3},[-]?\d{1,3}\)"
        matches = re.findall(regex, str)
        return matches

    # Returns a list of matches
    def parse_muls_w_conditions(self, str):
        regex = r"mul\([-]?\d{1,3},[-]?\d{1,3}\)|do\(\)|don't\(\)"
        matches = re.findall(regex, str)

        for tok in matches[:]:
            if tok == "do()":
                self.enabled = True
                matches.remove(tok)
                continue
            elif tok == "don't()":
                self.enabled = False
                matches.remove(tok)
                continue
            else:
                if not self.enabled:
                    matches.remove(tok)

        return matches

    def process_muls(self, conditional=False):
        total = 0
        for line in self.mul_lines:
            if conditional:
                mul_list = self.parse_muls_w_conditions(line)
            else:
                mul_list = self.parse_muls(line)
            for mul in mul_list:
                mul_operands = self.parse_mul(mul)
                total = total + mul_operands[0] * mul_operands[1]
        return total