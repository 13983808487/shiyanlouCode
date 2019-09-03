
import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    try:
        df = pd.read_json(file)
    except ValueError:
        print('file not found')
        return 0
    
    minutes = df[df['user_id']==user_id]['minutes'].sum()
    times = df[df['user_id']==user_id]['minutes'].__len__()
    return times, minutes
if __name__ == '__main__':
     a = analysis('user_study.json', 5348)
     print(a)


