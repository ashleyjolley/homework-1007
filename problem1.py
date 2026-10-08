# Ask the user for purchase amount and membership status
purchase_amount = float(input("Enter purchase amount: $"))
membership_status = input("Are you a member? (yes or no): ").lower()

# Determine the discount based on membership and purchase amount
if membership_status == "yes":
    if purchase_amount >= 100:
        discount_percentage = 15
    else:
        discount_percentage = 5
else:
    if purchase_amount >= 150:
        discount_percentage = 10
    else:
        discount_percentage = 0

# Calculate the final price
discount_amount = purchase_amount * (discount_percentage / 100)
final_price = purchase_amount - discount_amount

# Print the results
print(f"Discount applied: {discount_percentage}%")
print(f"Final price: ${final_price:.2f}")