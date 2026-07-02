import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "TV": [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 120.2, 199.8, 66.1],
    "Radio": [37.8, 39.3, 45.9, 41.3, 10.8, 48.9, 32.8, 19.6, 2.6, 5.8],
    "Sales": [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 11.8, 13.2, 10.6, 8.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["TV", "Radio"]]
y = df["Sales"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict sales for new advertising values
tv_budget = 150
radio_budget = 25

predicted_sales = model.predict([[tv_budget, radio_budget]])

print("TV Advertising Budget:", tv_budget)
print("Radio Advertising Budget:", radio_budget)
print("Predicted Sales:", predicted_sales[0])

# Plot TV advertising vs Sales
plt.scatter(df["TV"], df["Sales"])
plt.xlabel("TV Advertising")
plt.ylabel("Sales")
plt.title("TV Advertising vs Sales")
plt.show()