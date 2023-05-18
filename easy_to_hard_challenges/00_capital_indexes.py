#Write a function named capital_indexes. The function takes a single parameter, which is a string. 
#Your function should return a list of all the indexes in the string that have capital letters.
def capital_indexes(theString):
    index_list = []
    idx = 0
    for char in theString:
        if char >= 'A' and char <= 'Z':
            index_list.append[idx]
    idx += 1
    return index_list
    print(capital_indexes("HeLlO"))