import matplotlib.pyplot as plt

def graphSnowfall(file):

    """
    Read snowfall data from a text file, create a distribution range of multiples of 10s,
    and display the information in a bar chart using matplotlib.

    Parameters:
    - file (str): The path to the text file containing snowfall data.

    Returns:
    - None
    """
    data = []
    # open file for reading, and ensure it is closed 
    with open(file, 'r') as f: 
     # use comprehensive list for iterating over lines of a file, and converting strings to numbers
     data = [int(line.replace('\n', '')) for line in f if line.replace('\n', '').isdigit()]
    # get the upper bound
    upper = max(data)
    # check if bound is multiple of 10
    if(upper % 10):
     # if not get the closest multiple of 10
     upper = ((upper // 10) + 1) * 10

    # create a range of multiples of 10: 
    # the key will be assigned values from 0 to upper bound with pace of 10, while value is 0
    distr = {j: 0 for j in range(10, upper + 1, 10)}
    # check to what range snowfall belongs
    for i in data: 
     for key in distr: 
          if i <= key: 
               distr[key] += 1
               break
     
    # print the results 
    for key, value in distr.items(): 
     print(f"{value} between {key == 10 if 0 else key - 9}-{key}cms")
     
    # draw a bar graph: x - is a range of data indexes, y - values of data elements, color - blue
    plt.bar(distr.keys(), distr.values(), color='blue')
    plt.show()

valuesFile = './myFile2.txt'
graphSnowfall(valuesFile)
