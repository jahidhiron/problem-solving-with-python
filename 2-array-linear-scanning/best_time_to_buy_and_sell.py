"""
Module: stock_profit_calculator

This module provides a function to calculate the maximum profit that can be 
achieved from a list of daily stock prices. The strategy is to buy on one day 
and sell on another day after the buying day to maximize profit.

Functions:
- max_profit(prices): Computes the maximum possible profit from a list of prices.

Example:
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))  # Output: 5 (Buy at 1, sell at 6)
"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0
    buying_price = float('inf')

    for current_price in prices:
        buying_price = min(buying_price, current_price)
        profit_or_loss = current_price - buying_price
        profit = max(profit, profit_or_loss)

    return profit


if __name__ == "__main__":
    price_list = [7, 1, 5, 3, 6, 4]
    print(max_profit(price_list))  # Output: 5 (Buy on day 2 and sell on day 5)
