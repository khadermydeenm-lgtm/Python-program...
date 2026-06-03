import pandas as pd

# Load Dataset
df = pd.read_csv("dataset.csv")

# Filter adults (Age >= 18) and Fare > 30
adults_fare = df[(df['Age'] >= 18) & (df['Fare'] > 30)]

print("Adults with Fare > 30:")
print(adults_fare)

# Create new feature: Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Create new feature: Fare Per Person
df['FarePerPerson'] = df['Fare'] / df['FamilySize']

# Average Fare based on Passenger Class and Gender
avg_fare = df.groupby(['Pclass', 'Sex'])['Fare'].mean()

print("\nAverage Fare by Passenger Class and Gender:")
print(avg_fare)

# Survival Rate based on Passenger Class and Gender
survival_rate = df.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100

print("\nSurvival Rate (%) by Passenger Class and Gender:")
print(survival_rate)

# Save output dataset
df.to_csv("titanic_task5_output.csv", index=False)

print("\nTask 5 Completed Successfully!")
print("Output saved as titanic_task5_output.csv")
