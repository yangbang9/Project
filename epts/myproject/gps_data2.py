import pandas as pd

def gps_data():
      
  # 빈 리스트를 생성하여 각 열의 데이터를 저장할 준비를 합니다.
  time_list = []
  pitch_list = []
  roll_list = []
  yaw_list = []
  dYaw_list = []
  latitude_list = []
  longitude_list = []
  gps_time_list = []
  accel_list = []
  gyro_list = []
  mag_list = []
  speed_list = []

  # 파일을 읽어옵니다.
  with open('./data/DATA6.txt', 'r') as file:
      for line in file:
          # 각 줄을 공백으로 분할합니다.
          parts = line.split()

          # for i in range(35, 45):
          #     print(parts[i])
          
      
          # 분할된 데이터를 각 열에 맞게 저장합니다.
          time_list.append(float(parts[2]))
          pitch_list.append(float(parts[5]))
          roll_list.append(float(parts[8]))
          yaw_list.append(float(parts[11]))
          dYaw_list.append(float(parts[14]))
          latitude_list.append(float(parts[17]))
          longitude_list.append(float(parts[20]))
          gps_time_list.append(parts[24])
          accel_data = parts[29:32]
          accel_data = [float(val.strip('(),')) for val in accel_data]
          accel_list.append(accel_data)

          gyro_data = parts[36:39]
          gyro_data = [float(val.strip('(),')) for val in gyro_data]
          gyro_list.append(gyro_data)

          mag_data = parts[43:46]
          mag_data = [float(val.strip('(),')) for val in mag_data]
          mag_list.append(mag_data)
          speed_list.append(float(parts[-1]))

  # 데이터 프레임을 생성합니다.
  data = pd.DataFrame({
      'time': time_list,
      'pitch': pitch_list,
      'roll': roll_list,
      'yaw': yaw_list,
      'dyaw': dYaw_list,
      'lat': latitude_list,
      'long': longitude_list,
      'GPS Time': gps_time_list,
      'accel': accel_list,
      'gyro': gyro_list,
      'mag': mag_list,
      'speed': speed_list
  })

  data['GPS Time'] = pd.to_datetime(data['GPS Time'], format='%H:%M:%S')
  
  return data

