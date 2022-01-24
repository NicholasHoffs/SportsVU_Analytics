import pandas as pd
import csv
from game_objects import Moment
import os

class BasketFinder:
    def __init__(self,file_path):
        self.file_path = file_path
        self.frame = 0

    def _is_basket(self, moment):
        if (4 <= moment.ball.x <= 8 and 24 <= moment.ball.y <= 26 and moment.shot_clock != None):
            if(23 >= moment.shot_clock):
                return True
        else:
            return False

    def event_finder(self, event):
        for moment in event['moments']:
            _moment = Moment(moment)
            if self._is_basket(_moment)==True:
                return event
            else:
                return False

    def file_saver(self, game_id, index):
        row = [game_id,index]
        with open('./src/data/segmentor/screen_segmentation.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
    
    def compile(self):
        df = pd.read_json(self.file_path,lines=True,orient='columns')

        for event_index, event in enumerate(df['events'][0]):

            if self.event_finder(event):
                print('Shot at {}'.format(event_index))
                self.file_saver(str(self.file_path),event_index)
                
            else:
                pass

for file in os.listdir('./data/raw/motion'):
    shot = BasketFinder('./data/raw/motion/{}'.format(file))
    shot.compile()