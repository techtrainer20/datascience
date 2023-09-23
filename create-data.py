import pandas as pd
# Create a dataframe
raw_data = {'first_name': ['Sam','Ziva','Kia','Robin'],
        'degree': ['PhD','MBA','','MS'],
        'age': [25, 29, 19, 21]}
df = pd.DataFrame(raw_data)
df
#Save the dataframe
df.to_csv(r'Example1.csv')