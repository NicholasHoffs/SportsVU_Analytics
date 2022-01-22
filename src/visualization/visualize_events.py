import plotly.express as px

def plot_event(data, event_number):
    df = data[data['event_number']==event_number]

    fig = px.scatter(df,x='loc_x',y='loc_y', color=['team_id','is_ball'],animation_group='player_id',animation_frame='shot_clock')

    fig.show()