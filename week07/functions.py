#self assesment questions
# question 1: the first bug i spotted was the colon. i found it from expalining the code, the format was worng. This tells me i know the format of the code which is helpful in debugging
# question 2: it calculates the discount prices based on the specific tiers, the inputs are the current price and the tier and it returns the discounted price. Yes i think a colleague use it without reading the body.
# question 3: only for question 5 where Ai usage was a part of the activity. 




#exercise 1
def calculate_tax(price,rate):
    return price*rate

tax1=calculate_tax(100,0.07)
tax2=calculate_tax(250,0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350,0.05):.2f}")

#exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price*0.85
    elif tier == "silver":
        return price*0.90
    elif tier == "bronze":
        return price*0.95
    else:
        return price

original_price=200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#exercise 3
def final_price(price, tax_rate, discount_tier):
    discounted_price=apply_discount(price, discount_tier)
    tax=calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200,0.07,'gold')=${final_price(200,0.07,'gold'):.2f}")

#exercise 4

orders=[(200,'gold'),(150,'silver'),(80,'bronze'),(500,'none')]

rate=0.07
for price, tier in orders:
    total=final_price(price,rate, tier)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")


#exercise 5
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale  # need to add +
print(f"Total: ${total}")

count = 0
for sale in sales:  # need to add :
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # change to <
    print(sales[i])
    i += 1


#exercise 6

x=100
def double_it():
    x=999
    return x*2

print(x)
print(double_it())
print(x)
