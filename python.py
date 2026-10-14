
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [75, 90, 65, 85, 95]
}

df = pd.DataFrame(data)

print(df)

print("\nStudents scoring more than 80:")
print(df[df["Marks"] > 80])
