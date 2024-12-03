# Open the text file
def calc(line):
    last = int(line[1]) - int(line[0])
    for itr in range(len(line)-1):
        currDiff = int(line[itr+1]) - int(line[itr])
        if currDiff > 3 or currDiff == 0 or currDiff < -3 or (currDiff * last <= 0):
            return True,itr  
        last = currDiff
    return False,-1
def main():
    numberofSafeRows = 0
    with open('input.txt', 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into individual numbers, converting them to integers (or float if needed)
        
            line = line.split()
            # ['25', '26', '29', '30', '32', '35', '37', '35']
            unsafe = False
            ###
            # Call Function
            tries = 0
            unsafe,point = calc(line)
            ###
            if not unsafe:
                numberofSafeRows += 1
                continue
            else:
                newLine = line[0:point]+line[point+1:]
                print(newLine)
                unsafe,point = calc(newLine)
                tries += 1
                if not unsafe:
                    print("Damped")
                    numberofSafeRows += 1

            
    print(numberofSafeRows)
    
main()