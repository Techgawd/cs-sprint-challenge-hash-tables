def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create dictionary
    items = {}
    # walk through each index and the value for each index
    for i, weight in enumerate(weights):
        # retrieve target value, limit minus amount
        weight_index = limit - weights[i]
        # populate the dictionary if target not found
        if weight_index not in items:
            items[weight] = i
        else:
            return (i, items[weight_index])

