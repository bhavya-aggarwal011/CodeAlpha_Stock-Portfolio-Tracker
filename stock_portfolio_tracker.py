stock_price={
    "AAPL":180,
    "TSLA":250
}
n= int(input("Enter no of stocks: "))
for i in range(n):
    stock= input("Enter stock name ").upper()
    if stock in stock_price:
        
        quantity= int(input("How much this stock do you want? (quantity)"))
        total_invest= stock_price[stock]*quantity
        print("The total investment: ",total_invest)
        with open("portfolio.txt", "w") as file:
            file.write("The total Investment = " + str(total_invest))
    else:
        print("Stock not available")
    
