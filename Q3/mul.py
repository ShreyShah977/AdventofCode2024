import re

def main():
    with open('input.txt', 'r') as file:
        text = file.read()

    ## Filter for mul(X,Y)
    # Define the regex patterns to match
    patterns = [
        r"\bdo\(\)",               # Match "do()"
        r"\bdon't\(\)",            # Match "don't()"
        r"\bmul\(\d+,\d+\)",       # Match "mul(x,y)" where x and y are numbers
    ]
    combined_pattern = re.compile("|".join(patterns))  # Combine patterns with OR operator

######## Part 2

    matches = re.findall(combined_pattern, text)
    
    # Regex pattern to capture x and y from MUL expression
    pattern2 = r"mul\((\d+),(\d+)\)"
    resultofInstructions = 0
    # Search for matches and extract x and y
    flag = True
    for m in matches:
        if m == "don't()":
            flag = False
        elif m == "do()":
            flag = True
        else:
            if flag:
                match = re.match(pattern2, m)
                x, y = match.groups()  # Extract the captured groups (x and y values)
                resultofInstructions += int(x)*int(y)
    print(resultofInstructions)
main()