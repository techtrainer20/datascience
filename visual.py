import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe
raw_data = {'first_name': ['Sam','Ziva','Kia','Robin'],
            'degree': ['PhD','MBA','','MS'],
            'age': [25, 29, 19, 21]}
df = pd.DataFrame(raw_data)

# Save the dataframe to a CSV file
df.to_csv('Example1.csv', index=False)

# Create a bar plot of the 'age' column
plt.bar(df['first_name'], df['age'])
plt.xlabel('First Name')
plt.ylabel('Age')
plt.title('Age Distribution')
plt.show()
