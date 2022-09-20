#Xabien Loor
#stocks

#sharesPurchased = 2000
#pricePerShare = 40.00
#sharesSold = 2000
#priceSoldPerShare = 42.75

#inputs
sharesPurchased = float(input("Enter number of shares purchased: "))
pricePerShare = float(input("Enter price per share: "))
sharesSold = float(input("Enter number of shares sold: "))
priceSoldPerShare = float(input("Enter price sold per share: "))

#calculations
pricePaidFor = sharesPurchased * pricePerShare
commissionPurchase = pricePaidFor * .03
priceSoldFor = sharesSold * priceSoldPerShare
commissionSale = priceSoldFor * .03
profit = priceSoldFor - (pricePaidFor + commissionPurchase + commissionSale)

#print
print(f"Amount paid for the stock is, ${pricePaidFor:,.2f}")
print(f"Cmmission paid on the purchase: ${commissionPurchase:,.2f}")
print(f"Amount the stock sold for: ${priceSoldFor:,.2f}")
print(f"Comission paid on the sale: ${commissionSale:,.2f}")
print(f"Profit (or loss if negative): ${profit:,.2f}")
