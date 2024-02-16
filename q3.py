import string

def wordCount(t):

    data = []
    # open file for reading as f, and close it 
    with open(t, 'r') as f: 
        # create a list of lines using comprehensive list, replacing new line characters  
        data = [line.replace('\n', '') for line in f]; 

    # create a dictionary and  a counter 
    res = {}
    cnt = 0
    for i in data:
        # counter represents the line number 
        cnt += 1
        # string.punctuation includes all ASCII punctuation characters
        # strip method removes specified characters from beginning and end 
        words = [word.strip(string.punctuation) for word in i.split()]
        # unqiue will hold each line's unique words
        unique = set()
        unique.update(words)
        for j in unique: 
            # check if the word is already in dictionary 
            if j not in res: 
                res[j] = [cnt]
            else:
                res[j].append(cnt)
            
wordCount("myFile3.txt")
