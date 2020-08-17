def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # example arrays
    # [
#     [1, 2, 3, 12, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]
    # create dictionary 
    dict_t = {}
    results = []
    for row in arrays:
        # loop through every value in the row
        for i in row:
            # populate dictionary 
            if i not in dict_t:
                dict_t[i] = 1
                # add 1 if appeared already in dict
            else:
                dict_t[i] += 1
            if dict_t[i] == len(arrays):
                results.append(i)

    return results

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
