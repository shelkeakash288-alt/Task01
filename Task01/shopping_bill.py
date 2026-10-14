def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst

def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst

def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food



def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount

a = float(input("Enter first electronics item price: "))
b = float(input("Enter second electronics item price: "))
c = float(input("Enter first fashion item price: "))
d = float(input("Enter second fashion item price: "))
e = float(input("Enter food item price: "))

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("\n========== SHOPPING BILL ==========")
print(f"Electronics after GST: Rs. {electronics:.2f}")
print(f"Fashion after GST:     Rs. {fashion:.2f}")
print(f"Food after GST:        Rs. {food:.2f}")
print("-----------------------------------")
print(f"Total after GST:       Rs. {total:.2f}")
print(f"Discount (20%):        Rs. {discount:.2f}")
print("-----------------------------------")
print(f"Final payable amount:  Rs. {final_amount:.2f}")
print("===================================")
