import requests
import pandas as pd

def issues(repo):
    raw = requests.get(
            'https://api.github.com/repos/{}/issues'.format(repo))
    i_list = []
    for i in raw.json():
        i_dict = {'number':i['number'],
                'title':i['title'],
                'user_name':i['user']['login']
                }
        i_list.append(i_dict)

    issues_df = pd.DataFrame(i_list)

    return issues_df

if __name__ == '__main__':
    issues('numpy/numpy')
