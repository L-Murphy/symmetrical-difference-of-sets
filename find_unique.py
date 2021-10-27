import pandas as pd

def make_set_from_column(column):
    new_set = set()
    for d in column.values.tolist():
        new_set.add(d[0])

    return new_set



data = pd.read_csv (r'./28000_Data.csv')

df_one = pd.DataFrame(data, columns = ['SpecID'])
df_two = pd.DataFrame(data, columns=['_SpecID'])

set_one = make_set_from_column(df_one)
set_two = make_set_from_column(df_two)


unique = (set_one.symmetric_difference(set_two))

print(unique)
