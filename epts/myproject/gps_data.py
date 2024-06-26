import pandas as pd
import re
def gps_data():
    # 데이터를 저장할 리스트 초기화
    data = []

    # 텍스트 파일 읽기 (인코딩 지정)
    with open('./data/GPSDATA1.TXT', 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    # 데이터 파싱
    current_data = {}
    for line in lines:
        line = line.strip()
        if re.match(r'^시간:', line):
            if current_data:
                data.append(current_data)
            current_data = {}
            current_data['시간'] = re.search(r'\d+:\d+:\d+', line).group()
        elif re.match(r'^위도:', line):
            current_data['위도'] = float(re.search(r'[-+]?\d*\.\d+|\d+', line).group())
        elif re.match(r'^경도:', line):
            current_data['경도'] = float(re.search(r'[-+]?\d*\.\d+|\d+', line).group())
        elif re.match(r'^가속도:', line):
            current_data['가속도'] = tuple(map(float, re.findall(r'[-+]?\d*\.\d+|\d+', line)))
        elif re.match(r'^자이로:', line):
            current_data['자이로'] = tuple(map(float, re.findall(r'[-+]?\d*\.\d+|\d+', line)))
        elif re.match(r'^지자계:', line):
            current_data['지자계'] = tuple(map(float, re.findall(r'[-+]?\d*\.\d+|\d+', line)))
        elif re.match(r'^속도 \(km/h\):', line):
            current_data['속도 (km/h)'] = float(re.search(r'[-+]?\d*\.\d+|\d+', line).group())


    # 마지막 데이터 추가
    if current_data:
        data.append(current_data)
    
    # 데이터 프레임 생성
    df = pd.DataFrame(data)

    # 위도와 경도가 0인 행 제거
    df = df[(df['위도'] != 0) & (df['경도'] != 0)]

    # 인덱스 재설정
    df.reset_index(drop=True, inplace=True)

    # 열 이름 변경
    df.rename(columns={
        '시간': 'time',
        '위도': 'lat',
        '경도': 'long',
        '가속도': 'accel',
        '자이로': 'gyro',
        '지자계': 'mag',
        '속도 (km/h)': 'speed'
    }, inplace=True)

    # accel, gyro, mag 열의 데이터 형식을 리스트로 변경
    df['accel'] = df['accel'].apply(lambda x: list(x))
    df['gyro'] = df['gyro'].apply(lambda x: list(x))
    df['mag'] = df['mag'].apply(lambda x: list(x))

    
    return df

