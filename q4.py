def decorator(line):
    # split the sentence into words by space and convert them to integers 
    nums = [int(word) for word in line.split()] 

    # print all numbers 
    print("the numbers read: ", end='')
    for i in nums:
        print(i, end=' ')

    print(f"\nthe count of the numbers read: {len(nums)}") # count
    print(f"the average of the numbers: {round(sum(nums) / len(nums),2)}") # avg
    print(f"the maximum of the numbers: {max(nums)}") # max 
    print('\n')


def printStats(t):
    data = []
    # open file for reading, and ensure it is closed 
    with open(t, 'r') as f: 
        # use comprehensive list for iterating over lines of a file, and replacing new line characters 
        data = [line.replace('\n', '') for line in f]

    # for each line apply function
    for i in data: 
        decorator(i)

printStats("myFile4.txt")
