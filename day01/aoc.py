import os
filename = "./input.txt"

def part1():
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            digits = []
            for char in line:
                if char.isdigit():
                    if len(digits) < 2:
                        digits.append(int(char))
                    else:
                        digits[1] = int(char)
            if len(digits) == 1:
                add_this = 10 * digits[0] + digits[0]
                sum += add_this
            elif len(digits) == 2:
                add_this = 10 * digits[0] + digits[1]
                sum += add_this
    print(sum)

def part2():
    pass

if __name__ == "__main__":
    if os.environ.get("part") == "part2":
        part2()
    else:
        part1()
