import plotly.express as px
import pandas as pd
import numpy as np
import os

def plot_event(json_path, event_number):
    df = pd.read_json(json_path,lines=True,orient='columns')

    columns=['team_id','player_id','loc_x','loc_y','ball_z','shot_clock']
    a_list = []
    moments = df['events'][0]['eventId'==1]['moments']

    for moment_num, moment in enumerate(moments):
        locations = moment[5]

        time = moment[3]
        
        time_array_length = np.shape(locations)[0]

        time_array = np.full((time_array_length,1),fill_value=time)

        np.hstack((locations,time_array))

        a_list.append(np.hstack((locations,time_array)))

    desired_shape = (np.shape(a_list)[0]*np.shape(a_list)[1],6)
    a_list = np.reshape(a_list,desired_shape)

    final_df = pd.DataFrame(a_list,columns=columns)

    final_df.to_csv(os.getcwd()+'/example.csv')

    teams = final_df['team_id'].astype(str)
    
    fig = px.scatter(final_df,x='loc_x',y='loc_y', range_x=[0,100],range_y=[0,50], color=teams, animation_frame=final_df['shot_clock'],animation_group='player_id')

    fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

    fig.show()

plot_event('./data/raw/motion/0021500001.json',15)