import os
import pandas as pd

import django
from django.conf import settings

# Django 프로젝트 설정을 설정 파일에서 불러옵니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import SelectedPlayer
## 경고 메세지 무시
import warnings
from pandas.errors import SettingWithCopyWarning
warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))


## 코사인 유사도 분석 함수 호출

## 시각화 함수 호출
from plot_radar_chart3 import compare_radar_chart as vis2
from stat_select import stat

def final1():
    ## 전처리된 프로 선수 데이터 불러오기
    df = pd.read_csv('./data/processed_data.csv', index_col = 0)

    ########## 이것만 함수 호출해서 바로 불러오면됨
    ## 사용자 정보 입력
    # player = {
    #     'Name' : 'Yang',
    #     'Position' : 'FW',
    #     'Acceleration' : 60,
    #     'SprintSpeed' : 60,
    #     'Agility' : 60,
    #     'Stamina' : 60,
    #     'Aggression' : 60
    # }
    player = stat()


    ## 변수 선언
    features = ['Acceleration', 'SprintSpeed', 'Agility', 'Stamina', 'Aggression']
    player = pd.DataFrame(player, index=[-1])
    

    target_player = player['Name'].values[0]


    ## 기존 df에 붙이기
    df = pd.concat([player, df])
    df['Total'] = df[features].sum(axis=1)
    df = df.reset_index(drop=True)


    # 선수 이름 불러오기
    # if len(sys.argv) >= 2:
    #     target2 = sys.argv[1]
    # else:
    #     target2 = None
    
    try:
        selected_player = SelectedPlayer.objects.last()
        if selected_player:
            target2 = selected_player.name
            print("target2 value", target2)
        else:
            target2 = None
            print("target2 is None")
    except SelectedPlayer.DoesNotExist:
        target2 = None
        print("target2 is None")

    
    ## 시각화 대상 정의
    target1 = target_player

    ## 시각화 대상 스탯 추출
    player1_stats = df[df['Name'] == target1].iloc[0]
    player2_stats = df[df['Name'] == target2].iloc[0]



    ## 개인별 시각화하고 이미지 파일 저장
    # vis1(player1_stats, target1)
    # vis1(player2_stats, target2)

    result_data1 = {
        'player1' : target1,
        'player1_stats': player1_stats,
        'player2' : target2,
        'player2_stats': player2_stats,
        
    }
    
    
    vis2(df, target1, target2)
    return(result_data1)

if __name__ == '__main__':
    result = final1()