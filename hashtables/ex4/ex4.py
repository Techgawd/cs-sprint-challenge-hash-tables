def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # creating dictionary
    dict_t = {}
    # if positive and negative, will append
    both = []
    # walking through given values
    for i in a:
        # abs function to flip positive to neg
        i = abs(i)  
        # if number is not in dictionary, create an index and assign value
        if i not in dict_t:
            dict_t[i] = 1
        else:
            both.append(i)

    return both


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
