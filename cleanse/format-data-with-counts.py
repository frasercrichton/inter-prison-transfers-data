import pandas as pd

prison_locations_df = pd.read_json('../data/prison-locations.json')

def clean_data(df):
    return  df.drop(columns=['Name', 'Prison', 'Official Name', 'Gender', 'Opened', 'Closed', 'Capacity',
                      'Classification'])

def add_prison_locations(df, to_from):
    df = pd.merge(df,
                  prison_locations_df,
                  left_on=to_from,
                  right_on='Abbreviated',
                  how='left')
    df['Transfer_' + to_from + '_Coordinates'] = df[['Longitude', 'Latitude']].values.tolist()
    df = df.drop(columns=['Latitude', 'Longitude', 'Abbreviated'])
    return df

prison_locations_df = clean_data(prison_locations_df)

inter_prison_transfers_df = pd.read_csv('../data/inter-prison-transfers-original.csv')

df = inter_prison_transfers_df.groupby(['From'])\
    .size() \
    .reset_index(name='transfer-count') \
    .sort_values(by=['From'])

df = add_prison_locations(df, 'From')

print(df)

df.to_json('../output/inter-prison-transfers-counts.json', orient="records")

df = inter_prison_transfers_df.groupby(['From', 'Reason'])\
    .size() \
    .reset_index(name='count') \
    .sort_values(by=['From'])

df = df[df['Reason']=='Population Management']
df = add_prison_locations(df, 'From')

print(df)

df.to_json('../output/inter-prison-transfers-population-management-counts.json', orient="records")
