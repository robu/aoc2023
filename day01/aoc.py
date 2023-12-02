import os
filename = "./input.txt"

def line_calibration_value(line):
    # filter to keep digits in the line
    digits = list(filter(lambda char: char.isdigit(), line))
    # convert digits to ints
    digits = list(map(lambda char: int(char), digits))
    # if there is only one digit, keep it twice
    if len(digits) == 0:
        digits = [0, 0]
    if len(digits) == 1:
        digits.append(digits[0])
    digits = [digits[0], digits[-1]] # keep first and last digit
    
    return 10 * digits[0] + digits[1]

# def line_calibration_value_orig(line):
#     sum = 0
#     digits = []
#     for char in line:
#         if char.isdigit():
#             if len(digits) < 2:
#                 digits.append(int(char))
#             else:
#                 digits[1] = int(char)
#     if len(digits) == 1:
#         add_this = 10 * digits[0] + digits[0]
#         sum += add_this
#     elif len(digits) == 2:
#         add_this = 10 * digits[0] + digits[1]
#         sum += add_this
#     return sum

def clean_line(line):
    NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # find occurences of NUMBERS in the line, and replace each with the corresponding digit
    for i in range(len(line)):
        for number in NUMBERS:
            if line[i:].startswith(number):
                line = line[:i] + str(NUMBERS.index(number) + 1) + line[i + len(number):]
                i = i + len(number)
    return line

def part1():
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            sum += line_calibration_value(line)
    print(sum)

def part2():
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            print(f"line before clean: {line}")
            line = clean_line(line.strip())
            print(f"line after clean:  {line}")
            line_value = line_calibration_value(line)
            print(f"line value: {line_value}")
            sum += line_value
    print(sum)

if __name__ == "__main__":
    if os.environ.get("part") == "part2":
        part2()
    else:
        part1()
