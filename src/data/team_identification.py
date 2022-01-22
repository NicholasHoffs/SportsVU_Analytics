import pandas as pd


#Takes dataset with all lists of team names, abbreviations, and ids over seasons and reduces it to just 2016 and the team names

df = pd.read_csv('../../data/raw/NBA_Team_IDs.csv')

df_2016 = df[df['Season']==2016]
df_2016 = df_2016[['Current_BBRef_Team_Name','NBA_Current_Link_ID']]

df_2016.rename(columns={"Current_BBRef_Team_Name": "Name", "NBA_Current_Link_ID": "ID"},inplace=True)

df_2016.to_csv('../../data/external/Team_Identification.csv',index=False)