my_list = [89, 1, 44, 55, 67, 99, 1000, 1]

def bubblesort(alist): # define function name and parameters

    '''The first for loop runs once, then the 2nd for loop executes
        until the condition has been met. Then the 1st loop runs again
        and i is now incremented by 1. When the second loop begins again,
        because the largest element has "bubbled" to the top, the second loop runs
        for the length of the list - 1 - i. Remember: once the inner loop has run
        completely, it is mathmatically impossible for the largest digit in the list
        to be in the incorrect place '''
    
    for i in range(0, len(alist) - 1): # first loop runs for length - 1
        for x in range(0, len(alist) - 1 - i): # loop runs length -

            if alist[x] > alist[x + 1]: # checks if the index value is larger
                alist[x], alist[x + 1] = alist[x + 1], alist[x] # switches values

    return alist # returns sorted list outside of both loops

def average(alist):
    result = 0 # result of the sum of thelist

    for i in range(0, len(alist)): # loop over every element in the list
        result += alist[i] # add each element to result
        print(result)

    return result / len(alist) #return the sum of list / length
    # this returns the same result as the code above: return sum(alist) / len(alist)









