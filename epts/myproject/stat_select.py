import pandas as pd
import numpy as np
from gps_data import gps_data as gd
from myapp.models import UserProfile


def stat():   # 예제 데이터

    df = gd()
    # df['time'] = df['time'].dt.strftime('%H:%M:%S')

    # 데이터 프레임 코드
    # speed 단위 km/h
    # accel 단위 m/s²

    #주어진 네 개의 점을 이용하여 사각형의 경계를 정의합니다.
    # 네 개의 점을 정렬하여 경계 상하좌우의 경계값을 얻습니다.
    min_lat = min([37.629898330320025, 37.62896821245132, 37.62908585997369, 37.630013726859346])
    max_lat = max([37.629898330320025, 37.62896821245132, 37.62908585997369, 37.630013726859346])
    min_lon = min([127.07901992155236, 127.07879519947637, 127.07801365788048, 127.07823836821488])
    max_lon = max([127.07901992155236, 127.07879519947637, 127.07801365788048, 127.07823836821488])

    # 경계를 벗어나지 않는 데이터만 선택합니다.
    filtered_df = df[(df['lat'] >= min_lat) & (df['lat'] <= max_lat) & (df['long'] >= min_lon) & (df['long'] <= max_lon)]

    # 주어진 데이터 프레임
    # (이전에 제공한 데이터 프레임 filtered_df를 그대로 사용합니다)

    # 시간 문자열을 datetime 객체로 변환합니다.
    filtered_df['time'] = pd.to_datetime(filtered_df['time'], format='%H:%M:%S')

    # 시간 순으로 데이터프레임을 정렬합니다.
    filtered_df.sort_values(by='time', inplace=True)

    # 경계 상자 내부에 있었던 총 시간을 계산합니다.
    total_time_inside_boundary = filtered_df['time'].max() - filtered_df['time'].min()

    # 최고 속도
    max_speed = filtered_df['speed'].max()

    import numpy as np

    # x축 가속도와 y축 가속도를 사용하여 가속도의 크기 계산
    filtered_df['x_accel'] = [accel[0] for accel in filtered_df['accel']]
    filtered_df['y_accel'] = [accel[1] for accel in filtered_df['accel']]
    filtered_df['accel_magnitude'] = np.sqrt(filtered_df['x_accel'] ** 2 + filtered_df['y_accel'] ** 2)

    # 최고 가속도 출력
    max_acceleration = filtered_df['accel_magnitude'].max()
    

    # 최고 가속도 코드

    # 시간 간격을 계산하여 데이터프레임에 추가
    filtered_df['time_diff'] = filtered_df['time'].diff().dt.total_seconds()

    # 이동 거리를 계산하는 함수
    def calculate_distance(speed, time_diff):
        # 속도를 미터/초로 변환 (1 km/h = 1000/3600 m/s)
        speed_m_per_s = speed * 1000 / 3600
        # 이동 거리 계산 (거리 = 속도 * 시간)
        distance = speed_m_per_s * time_diff
        return distance

    # 각 행에 대한 이동 거리를 계산하여 데이터프레임에 추가
    filtered_df['distance'] = filtered_df.apply(lambda row: calculate_distance(row['speed'], row['time_diff']), axis=1)

    # 총 이동 거리를 계산
    total_distance = filtered_df['distance'].sum()

    # 주어진 데이터 프레임
    # (이전에 제공한 데이터 프레임 filtered_df를 그대로 사용합니다)

    # 'Section A'와 'Section B'를 정의하는 네 개의 점 좌표
    section_a = [(37.629898330320025, 127.07901992155236),
                (37.629432146173485, 127.07890614255425),
                (37.629549801926935, 127.07811326772533),
                (37.630013726859346, 127.07823836821488)]

    section_b = [(37.629432146173485, 127.07890614255425),
                (37.629549801926935, 127.07811326772533),
                (37.62908585997369, 127.07801365788048),
                (37.62896821245132, 127.07879519947637)]

    # 첫 데이터의 위도와 경도 (예시로 임의의 값 사용)
    initial_latitude = filtered_df.iloc[0]['lat']
    initial_longitude = filtered_df.iloc[0]['long']

    # 초기 위치가 어느 영역에 속하는지 판단
    def get_zone(initial_latitude, initial_longitude, section_a, section_b):
        if (initial_latitude >= min(section_a, key=lambda x: x[0])[0] and
            initial_latitude <= max(section_a, key=lambda x: x[0])[0] and
            initial_longitude >= min(section_a, key=lambda x: x[1])[1] and
            initial_longitude <= max(section_a, key=lambda x: x[1])[1]):
            return 'Section A'
        elif (initial_latitude >= min(section_b, key=lambda x: x[0])[0] and
            initial_latitude <= max(section_b, key=lambda x: x[0])[0] and
            initial_longitude >= min(section_b, key=lambda x: x[1])[1] and
            initial_longitude <= max(section_b, key=lambda x: x[1])[1]):
            return 'Section B'
        else:
            return '알 수 없음'

    # 초기 위치에 따라 공격 진영과 수비 진영을 정의
    initial_zone = get_zone(initial_latitude, initial_longitude, section_a, section_b)
    attack_zone = 'Section A' if initial_zone == 'Section B' else 'Section B'
    defense_zone = 'Section A' if initial_zone == 'Section A' else 'Section B'

    # 주어진 데이터 프레임
    # (이전에 제공한 데이터 프레임 filtered_df를 그대로 사용합니다)

    # 'Section A'와 'Section B'를 정의하는 네 개의 점 좌표
    section_a = [(37.629898330320025, 127.07901992155236),
                (37.629432146173485, 127.07890614255425),
                (37.629549801926935, 127.07811326772533),
                (37.630013726859346, 127.07823836821488)]

    section_b = [(37.629432146173485, 127.07890614255425),
                (37.629549801926935, 127.07811326772533),
                (37.62908585997369, 127.07801365788048),
                (37.62896821245132, 127.07879519947637)]

    # 첫 데이터의 위도와 경도 (예시로 임의의 값 사용)
    initial_latitude = filtered_df.iloc[0]['lat']
    initial_longitude = filtered_df.iloc[0]['long']

    # 초기 위치가 어느 영역에 속하는지 판단
    def get_zone(initial_latitude, initial_longitude, section_a, section_b):
        if (initial_latitude >= min(section_a, key=lambda x: x[0])[0] and
            initial_latitude <= max(section_a, key=lambda x: x[0])[0] and
            initial_longitude >= min(section_a, key=lambda x: x[1])[1] and
            initial_longitude <= max(section_a, key=lambda x: x[1])[1]):
            return 'Section A'
        elif (initial_latitude >= min(section_b, key=lambda x: x[0])[0] and
            initial_latitude <= max(section_b, key=lambda x: x[0])[0] and
            initial_longitude >= min(section_b, key=lambda x: x[1])[1] and
            initial_longitude <= max(section_b, key=lambda x: x[1])[1]):
            return 'Section B'
        else:
            return '알 수 없음'

    # 초기 위치에 따라 공격 진영과 수비 진영을 정의
    initial_zone = get_zone(initial_latitude, initial_longitude, section_a, section_b)
    attack_zone_a = 'Section A' if initial_zone == 'Section B' else 'Section B'
    defense_zone_a = 'Section A' if initial_zone == 'Section A' else 'Section B'
    attack_zone_b = 'Section B' if initial_zone == 'Section A' else 'Section A'
    defense_zone_b = 'Section B' if initial_zone == 'Section B' else 'Section A'

    # 'zone' 열 정의
    filtered_df['zone'] = initial_zone

    # 각 영역에 머문 총 시간 계산
    total_time_in_attack_zone_a = filtered_df[filtered_df['zone'] == attack_zone_a]['time'].count()
    total_time_in_defense_zone_a = filtered_df[filtered_df['zone'] == defense_zone_a]['time'].count()
    total_time_in_attack_zone_b = filtered_df[filtered_df['zone'] == attack_zone_b]['time'].count()
    total_time_in_defense_zone_b = filtered_df[filtered_df['zone'] == defense_zone_b]['time'].count()

    # Total Distance를 미터(m) 단위로 가져옵니다.
    total_distance = filtered_df['distance'].sum()

    # Playing Time을 분(min) 단위로 가져옵니다.
    total_time_inside_boundary = (filtered_df['time'].max() - filtered_df['time'].min()).total_seconds() / 60

    # Total Distance/Playing Time을 계산합니다.
    distance_per_minute = total_distance / total_time_inside_boundary

    # Distance per Minute 값을 기반으로 점수를 계산합니다.
    if distance_per_minute >= 135:
        score_stamina = 100
    elif distance_per_minute <= 60:
        score_stamina = 25
    else:
        score_stamina = 25 + int((distance_per_minute - 60))

    # 최고 속도
    max_speed = filtered_df['speed'].max()

    # 점수 계산
    if max_speed >= 35:
        score_sprint_speed = 100
    elif max_speed <= 5:
        score_sprint_speed = 25
    else:
        score_sprint_speed = 25 + int((max_speed - 5) / 0.4)

    # 최고 가속도 구하기
    max_acceleration = filtered_df['accel_magnitude'].max()

    # 점수 계산 함수
    def calculate_score(acceleration):
        if acceleration <= 2:
            score_acceleration = 25
        elif acceleration >= 9.5:
            score_acceleration = 100
        else:
            # 2에서 9.5 사이의 범위에서 0.1 단위로 점수 증가
            score_acceleration = 25 + int((acceleration - 2) / 0.1)
        return score_acceleration

    # 최고 가속도에 대한 점수 계산
    score_acceleration = calculate_score(max_acceleration)

    # 'attack_zone_a' 또는 'attack_zone_b'를 사용하여 해당 공격 진영에서 머문 시간을 구합니다.
    if initial_zone == 'Section A':
        time_in_attack_zone = total_time_in_attack_zone_a
    else:
        time_in_attack_zone = total_time_in_attack_zone_b

    # 'time_in_attack_zone'를 'total_time_inside_boundary'로 나누어 공격 진영에서 머문 시간의 비율을 계산합니다.
    attack_zone_time_ratio = time_in_attack_zone / total_time_inside_boundary

    # 비율에 따른 점수를 계산합니다.
    if attack_zone_time_ratio >= 0.9:
        score_aggression = 100
    elif attack_zone_time_ratio <= 0.15:
        score_aggression = 25
    else:
        score_aggression = 25 + int((attack_zone_time_ratio - 0.15) / 0.01)

    # 웹에서 입력받은 정보 불러오기
    user_profile = UserProfile.objects.first()
    name = user_profile.name
    position = user_profile.position


    # # 최종 player 스탯
    # player = {
    # 'Name' : name,
    # 'Position' : position,
    # 'Acceleration' : score_acceleration,
    # 'SprintSpeed' : score_sprint_speed,
    # 'Agility' : 30,
    # 'Stamina' : score_stamina,
    # 'Aggression' : score_aggression
    # }


    # 임의 player 스탯
    player = {
    'Name' : name,
    'Position' : position,
    'Acceleration' : 72,
    'SprintSpeed' : 74,
    'Agility' : 58,
    'Stamina' : 81,
    'Aggression' : 69
    }

    return player

print(stat())


