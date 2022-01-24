import pandas as pd
import plotly.express as px

df = pd.read_csv('./src/data/baskets.csv')

teams = df[df['Event_ID']==366]['Team_ID'].astype(str)

print(df[df['Event_ID']==366]['RADIUS'].max())

fig = px.scatter(df[df['Event_ID']==366], x='LOC_X',y='LOC_Y',range_x=[0,100],range_y=[0,50],color=teams,animation_group='Player_ID',animation_frame='SHOT_CLOCK')

fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.show()