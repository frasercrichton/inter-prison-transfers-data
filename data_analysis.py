import pandas as pd
import pydeck as pdk

def get_layers(data_frame):
    arc_layer = pdk.Layer(
        "ArcLayer",
        data=data_frame,
        get_width="2",
        get_source_position="Transfer_From_Coordinates",
        get_target_position="Transfer_To_Coordinates",
        get_tilt=75,

        get_source_color=RED_RGB,
        get_target_color=BLUE_RGB,
        pickable=True,
        auto_highlight=True,
    )

    layer = pdk.Layer(
        "GridLayer",
        data=data_frame,
        pickable=True,
        extruded=True,
        cell_size=20000,
        elevation_scale=400,
        get_position='Transfer_To_Coordinates',
        colorRange=[
            BLUE_RGB,
        ]
    )
    from_layer = pdk.Layer(
        "GridLayer",
        data=data_frame,
        pickable=True,
        extruded=True,
        cell_size=20000,
        elevation_scale=400,
        get_position='Transfer_From_Coordinates',
        colorRange=[
            RED_RGB,
        ]
    )
    return [arc_layer, from_layer]

def view(html_file_name, layers):
    view_state = pdk.ViewState(longitude=174.1886324, latitude=-40.6509396, bearing=0, pitch=45, zoom=5)
    TOOLTIP_TEXT = {
        "html": "From: {From} To: {To} Reason: {Reason} Transfer Date: {Transfer Date} Status At Transfer: {Status At Transfer} <br /> From in red; To in blue"}
    r = pdk.Deck(layers, map_style='light', initial_view_state=view_state, tooltip=TOOLTIP_TEXT)
    r.to_html(html_file_name)


prison_locations = 'data/prisons.json'
transfers = 'data/transfers.csv'


locations_df = pd.read_json(prison_locations)
transfers_df = pd.read_csv(transfers)

dict = pd.DataFrame([{
    'From': 'Rimutaka',
    'To': 'SHCF',
    'Reason': 'Judicial'
}])

df = pd.merge(transfers_df, locations_df, left_on='From',
              right_on='Abbreviated',
              how='left')

df['Transfer Date'] = pd.to_datetime(df['Transfer Date'])

print(df['Transfer Date'])

df['Transfer_From_Coordinates'] = df[['Longitude', 'Latitude']].values.tolist()
df['From_Coordinates'] = df[['Latitude', 'Longitude', ]].values.tolist()

df = df.drop(columns=['Name', 'Prison', 'Abbreviated', 'Official Name', 'Gender', 'Opened', 'Closed', 'Capacity',
                      'Classification', 'Latitude', 'Longitude'])

df = pd.merge(df, locations_df, left_on='To',
              right_on='Abbreviated',
              how='left')

df['Transfer_To_Coordinates'] = df[['Longitude', 'Latitude']].values.tolist()

df = df.drop(columns=['Name', 'Prison', 'Abbreviated', 'Official Name', 'Gender', 'Opened', 'Closed', 'Capacity',
                      'Classification', 'Latitude', 'Longitude'])



# print(df['Reason'].value_counts())

print(df['Status At Transfer'].value_counts())

print(df['Transfer Date'].value_counts())

print(df[['From']].value_counts())
print(df[['To']].value_counts())

print(df.describe())
print(df.columns)

BLUE_RGB = [0, 0, 255, 40]
RED_RGB = [240, 100, 0, 40]


# GET_COLOR_JS = [
#     "255 * (1 - (Transfer_From_Coordinates[2] / 10000) * 2)",
#     "128 * (Transfer_From_Coordinates[2] / 10000)",
#     "255 * (Transfer_From_Coordinates[2] / 10000)",
#     "255 * (1 - (Transfer_From_Coordinates[2] / 10000))",
# ]
# line_layer = pdk.Layer(
#     "LineLayer",
#     data=df,
#     get_source_position="Transfer_From_Coordinates",
#     get_target_position="Transfer_To_Coordinates",
#     get_color=GET_COLOR_JS,
#     get_width=2,
#     highlight_color=[255, 255, 0],
#     picking_radius=10,
#     auto_highlight=True,
#     pickable=True,
# )
#
#  mapboxApiAccessToken={MAP_BOX_ACCESS_TOKEN}
#           mapStyle={MAP_BOX_STYLE_ID}

df.to_json('./data/transfers.json', orient='records')
view("arc_layer.html", get_layers(df))
# 23 March 2020	Negative increase 3
# 26 March 2020	Negative increase 4
# 28 April 2020	Positive decrease 3
# 14 May 2020	Positive decrease 2
# 9 June 2020	Positive decrease 1
mask = (df['Transfer Date'] > '2020-03-26') & (df['Transfer Date'] <= '2020-04-28')
df = df.loc[mask]

# From,To,Reason,Transfer Date,Status At Transfer
print(df['Reason'].value_counts())
print(df[['From']].value_counts())
print(df[['To']].value_counts())

print(df['Transfer Date'].describe())

# print(df['To'].value_counts())
df.to_json('./data/covid-transfers.json', orient='records')
view("arc_layer_covid.html", get_layers(df))

# trace through In Transit/Multi-Site Move     832
# where os the place reviews end up
