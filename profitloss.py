cost_price=float(input("enter actual price of a product"))
sellingprice=float(input("enter selling price of a product"))
if(sellingprice>cost_price):
 amount=sellingprice-cost_price 
 print("total profit={0}".format(amount))
else:
 print("no profit")
