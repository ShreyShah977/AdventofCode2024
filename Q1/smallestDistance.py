## Steps:
## Take in Input of left list into left heap
## Take in Input of right list into right heap
## Go down the heaps and calculate distance. (popping will reveal smallest number)




import heapq, numpy
from collections import Counter


## Import data from txt file
def main():
    filePath = "./Q1/input.txt"
    left,right = [],[]
    leftH,rightH = [],[]
    ## Create Heaps
    heapq.heapify(leftH)
    heapq.heapify(rightH)
    ## Push 'em 
    with open(filePath, 'r') as file:
        for line in file:
            num1,num2 = map(int,line.split())
            left.append(num1)
            right.append(num2)
            heapq.heappush(leftH,num1)
            heapq.heappush(rightH,num2)

    ## Init Counter for MinSum
    minSum = 0
    for i in range(len(leftH)):
        ## Add absolute distance between points (only positives)
        currSum = abs(heapq.heappop(leftH) - heapq.heappop(rightH))
        minSum += currSum
    ## Return
    print(minSum)
    ### End of Part 1

    ## Part 2
    C1,C2 = Counter(left),Counter(right)
    totalSum = 0
    for i in C1:
        number = i
        frequencyOfNumberonLeft = C1[i]
        frequencyOfNumberonRight = C2[i]
        curr = number * frequencyOfNumberonLeft * frequencyOfNumberonRight
        totalSum += curr
        
    print(totalSum)

main()

