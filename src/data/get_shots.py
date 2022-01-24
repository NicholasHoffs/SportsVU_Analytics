import pandas as pd
import numpy as np

potential_baskets = pd.read_csv('./src/data/segmentor/screen_segmentation.csv')

list_to_df = []
for ix,file in enumerate(potential_baskets['Game_ID']):
    if ix<10:

        event_number = potential_baskets.iloc[ix]['Event_Number']
        event = pd.read_json(file,lines=True,orient='columns')['events'][0][event_number]
        
        list_to_df.append(event)
    else:
        continue

event_ids = []
moments = []
times = []
columns = ['Team_ID','Player_ID','LOC_X','LOC_Y', 'RADIUS']

for ix, event in enumerate(list_to_df):
    event_number = event['eventId']
    
    for moment in list_to_df[ix]['moments']:
        time = moment[3]
        for player in moment[5]:
            event_ids.append(event_number)
            times.append(time)
            moments.append(player)

df = pd.DataFrame(moments,columns=columns)
df['Event_ID'] = pd.Series(event_ids)
df['SHOT_CLOCK'] = pd.Series(times)

df = df[df['SHOT_CLOCK']<24]

df.dropna(axis=0,inplace=True)

df.to_csv('./baskets.csv',index=False)