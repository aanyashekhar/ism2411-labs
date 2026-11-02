#inventory = ["pen", "notebook"]
#inventory.append("tape")
#print(inventory)

# self assesment questions


#excercise 1
print("excercise 1")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#excercise 2
print("excercise 2")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

#excercise 3
print("excercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#excercise 4
print("excercise 4")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#excercise 5
print("excercise 5")
coords = (40.7128, -74.0060)

try:
    coords[0]=99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

#excercise 6
print("excercise 6")
sales = [100,250,75,480,200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Number of sales: {count}")
print(f"Average sale: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best=sales[0]
worst=sales[0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

#excercise 7
print("excercise 7")
prices = [9.99,14.99,4.99,24.99,1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

#excercise 8
print("excercise 8")
sales = [340,127,589,204,467,88,731,315,62,490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/len(high_sales):.2f}")
