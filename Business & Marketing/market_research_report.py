import matplotlib.pyplot as plt

# Company name
company = "Apple"

# SWOT Analysis
strengths = 8
weaknesses = 4
opportunities = 7
threats = 5

categories = ["Strengths", "Weaknesses", "Opportunities", "Threats"]
values = [strengths, weaknesses, opportunities, threats]

# Display SWOT Analysis
print("\nMARKET RESEARCH REPORT")
print("Company:", company)

print("\nStrengths:")
print("- Strong brand value")
print("- Innovative products")

print("\nWeaknesses:")
print("- Premium pricing")

print("\nOpportunities:")
print("- Expansion into AI and services")

print("\nThreats:")
print("- Strong competition")

# Create bar chart
plt.bar(categories, values)
plt.xlabel("SWOT Categories")
plt.ylabel("Score")
plt.title("SWOT Analysis of Apple")

plt.show()