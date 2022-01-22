import os
import pandas as pd
import gc

path='./data/raw/motion/'
files=[]

for r,d,f in os.walk(path):
    print('Root: {}, Directory: {}, File: {}'.format(r,d,f))
    for file in f:
        if '.json' in file:
            files.append(file)

for num,file_name in enumerate(files):
    print("File name: {} File number: {}/{}".format(file_name, num, len(files)))
    df = pd.read_json(path + file_name)
    length = len(df)
    del df
    gc.collect()
    for i in range(length):
        cmd = 'python E:/Python/SportsVU_Analytics/src/data/Segmentor/main.py --path={}'.format(path) + file_name + ' --event=' + str(i)
        print(cmd)
        os.system(cmd)
