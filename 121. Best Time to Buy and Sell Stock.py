def get_max(a):
    max_profit=0
    max_rest=max(a)
    for i in range(len(a)-1):
        if a[i]==max_rest:
            max_rest=max(a[i+1:])
            continue
        current_profit=max_rest-a[i]
        if current_profit>max_profit:
            max_profit=current_profit
    return max_profit

if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    print(get_max(prices))