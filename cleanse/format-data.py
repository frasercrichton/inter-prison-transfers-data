import pandas as pd

prison_locations_df = pd.read_json('../data/prison-locations.json')

# Original data format - From,To,Reason,Transfer Date,Status At Transfer
inter_prison_transfers_df = pd.read_csv('../data/inter-prison-transfers-original.csv')

def format_date(df):
    return pd.to_datetime(pd.to_datetime(df['Transfer Date']), format='%Y%m%d')

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

inter_prison_transfers_df['Transfer Date'] = format_date(inter_prison_transfers_df)

df = add_prison_locations(inter_prison_transfers_df, 'From')
df = add_prison_locations(df, 'To')

df.to_json('../output/inter-prison-transfers-formatted.json', orient="records", date_format='iso')
