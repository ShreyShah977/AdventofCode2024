# Open the text file
numberofSafeRows = 0
with open('input.txt', 'r') as file:
    # Read each line from the file
    for line in file:
        # Split the line into individual numbers, converting them to integers (or float if needed)
      
        line = line.split()
        # ['25', '26', '29', '30', '32', '35', '37', '35']
        unsafe = False
        last = int(line[1]) - int(line[0])
        for itr in range(len(line)-1):
            currDiff = int(line[itr+1]) - int(line[itr])
            if currDiff > 3 or currDiff == 0 or currDiff < -3 or (currDiff * last <= 0):
                unsafe = True
                break
            last = currDiff
        if not unsafe:
            numberofSafeRows += 1
        

print(numberofSafeRows)
