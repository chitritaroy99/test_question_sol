def stockMax(prices):
    max=float('-inf')
    profit=0
    for i in range(len(prices)-1, -1, -1):
        if prices[i]>max:
            max=prices[i]
        if max>=prices[i]:
            profit=profit+max-prices[i]
    return profit

#driver code
n=int(input())
prices=[]
for i in range(0,n):
    ele=int(input())
    prices.append(ele)
print(stockMax(prices))