def solution(stocks):
    """
    Finds the maximum profit possible from a single buy and sell operation.
    
    Parameters:
    stocks (List[int]): List of stock prices, where each element represents the price on a given day.
    
    Returns:
    int: The maximum profit possible. Returns 0 if no profit is possible.
    """

    # Initialize max_profit to 0 since no transaction has been made yet
    max_profit = 0

    # Initialize min_price to a very large value to ensure the first price replaces it
    min_price = float('inf')

    # Loop through each price in the list
    for stock in stocks:

        # If the current stock price is lower than the minimum price seen so far, update min_price
        if stock < min_price:
            min_price = stock

        # Calculate the profit if the stock were sold today
        profit = stock - min_price

        # Update max_profit if the current profit is higher than any seen before
        max_profit = max(max_profit, profit)

    # Return the best profit found
    return max_profit


# Example usage:
print(solution([7, 1, 2, 3, 7, 8]))  # Output: 7
