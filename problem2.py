# Ask the user for salary and performance score
annual_salary = float(input("Enter annual salary: $"))
performance_score = float(input("Enter performance score (0-100): "))

# Determine the bonus percentage based on performance
if performance_score >= 90:
    bonus_percentage = 20
elif performance_score >= 80:
    bonus_percentage = 10
elif performance_score >= 70:
    bonus_percentage = 5
else:
    bonus_percentage = 0

# Calculate the bonus amount
bonus_amount = annual_salary * (bonus_percentage / 100)

# Print the results
print(f"Performance Bonus: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount:.2f}")