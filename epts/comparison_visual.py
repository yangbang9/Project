import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

## 경고 메세지 무시
import warnings
import pandas as pd
from pandas.errors import SettingWithCopyWarning
warnings.simplefilter(action='ignore', category=(SettingWithCopyWarning))


## 코사인 유사도 분석 함수 호출
from cosine_similarity import cosine_similarity
## 시각화 함수 호출
from plot_radar_chart import plot_radar_chart as vis1
from plot_radar_chart2 import compare_radar_chart as vis2
from stat_select import stat

## 전처리된 프로 선수 데이터 불러오기
df = pd.read_csv('./data/processed_data.csv', index_col = 0)

########## 이것만 함수 호출해서 바로 불러오면됨
# 사용자 정보 입력
player = {
    # 'Name' : 'Yang',
    # 'Position' : 'FW',
    'Acceleration' : 79,
    'SprintSpeed' : 84,
    'Agility' : 80,
    'Stamina' : 82,
    'Aggression' : 56
}
# player = stat()


## 변수 선언
features = ['Acceleration', 'SprintSpeed', 'Agility', 'Stamina', 'Aggression']
player = pd.DataFrame(player, index=[-1])
score = 0

target_player = player['Name'].values[0]
target_vector = player[features].values[0]


## 기존 df에 붙이기
df = pd.concat([player, df])
df['Total'] = df[features].sum(axis=1)
df = df.reset_index(drop=True)

vectors = df[features].values


## 코사인 유사도가 붙은 데이터프레임 선언
cosine_df = df


## 코사인 유사도 계산
similarities = []
for vector in vectors:
    similarity = cosine_similarity(target_vector, vector)
    similarities.append(similarity)


## 유사한 순서대로 정렬한 데이터프레임
cosine_df['cosine_similarity'] = similarities
sorted_df = cosine_df.sort_values(by='cosine_similarity', ascending=False)


## 시각화 대상 정의
target1 = target_player
target2 = sorted_df.iloc[1]['Name']


df = df.drop(['cosine_similarity'], axis=1)



## 시각화 대상 스탯 추출
player1_stats = df[df['Name'] == target1].iloc[0]
player2_stats = df[df['Name'] == target2].iloc[0]



## 개인별 시각화하고 이미지 파일 저장
vis1(player1_stats, target1)
vis1(player2_stats, target2)

## 비교 레이더차트 이미지 파일 저장 후 닮음 점수 출력
print(f"You are {vis2(df, target1, target2)} \"{target2}\".")
