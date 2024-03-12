#You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit
def buy_sell_stock(a):

    i = len(a) - 2
    max_next = -1
    curr_profit = 0
    max_profit = 0
    while i>=0:
        if max_next > a[i]:                  # Greatest element on the right side which is greater than current element
            curr_profit = max_next - a[i]    # Find current profit
            if curr_profit > max_profit:
                max_profit = curr_profit
        elif max_next < a[i]:
            max_next = a[i]

        i -= 1

    print(max_profit)


prices = [7,1,5,3,6,4]
buy_sell_stock(prices)
