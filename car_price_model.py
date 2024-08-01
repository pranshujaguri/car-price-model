import pandas as pd

# Load the dataset
df = pd.read_csv('CarPrice.csv')

#Understanding the structure of the data

# Display the first few rows
print(df.head())

# Display basic information about the dataset
print(df.info())

# Summary statistics
print(df.describe())

#Data Cleaning and Preparation
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values or fill them as needed
df = df.dropna()  # Or use df.fillna() for imputation

# Check for duplicates
df = df.drop_duplicates()

# Ensure data types are correct
print(df.dtypes)

#Which 3 cars to have highest average price.
top_cars = df.groupby('CarName')['price'].mean().nlargest(3)
print(top_cars)

#Is diesel has higher average price than gas.
average_price_by_fuel = df.groupby('fueltype')['price'].mean()
print(average_price_by_fuel)

# Check if Diesel has a higher average price than Gas
print("Diesel vs Gas price comparison:")
print(f"Diesel average price: {average_price_by_fuel['diesel']}")
print(f"Gas average price: {average_price_by_fuel['gas']}")

#Which 2car type  have higher average price.
top_car_types = df.groupby('carbody')['price'].mean().nlargest(2)
print(top_car_types)

#Does doornumber variable affect the price much.
import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot to visualize the impact of door number on price
sns.boxplot(x='doornumber', y='price', data=df)
plt.title('Price by Door Number')
plt.show()

# Alternatively, you can use groupby
price_by_doornumber = df.groupby('doornumber')['price'].mean()
print(price_by_doornumber)

#Show that aspiration with turbo have higher price range than the std Which cylinder type have the highest price range.
aspiration_prices = df.groupby('aspiration')['price'].mean()
print(aspiration_prices)

# Boxplot for visual comparison
sns.boxplot(x='aspiration', y='price', data=df)
plt.title('Price by Aspiration')
plt.show()

# Probe that carwidth, carlength and curbweight seems to have a poitive correlation with price and carheight doesnot show any significant trend with price.
correlation_matrix = df[['price', 'carwidth', 'carlength', 'curbweight', 'carheight']].corr()
print(correlation_matrix)

# Visualization
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Is it correct that,citympg, highwaympg - seem to have a significant negative correlation with price.
# Correlation analysis
mpg_correlation = df[['price', 'citympg', 'highwaympg']].corr()
print(mpg_correlation)

# Visualization
sns.heatmap(mpg_correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix with MPG')
plt.show()
