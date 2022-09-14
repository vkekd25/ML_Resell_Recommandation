import pandas as pd

# 모든 당근마켓, 번개장터 데이터 불러오기
df_carrot_apple = pd.read_csv('Carrot_Applewatch.csv').drop(['Unnamed: 0'], axis =1)
df_carrot_galaxy = pd.read_csv('Carrot_Galaxywatch.csv').drop(['Unnamed: 0'], axis =1)
df_thunder_apple_one = pd.read_csv('Thunder_Applewatch_이유진.csv')
df_thunder_apple_two = pd.read_csv('Thunder_Applewatch_이창수.csv').drop(['Unnamed: 0'], axis =1)
df_thunder_apple_three = pd.read_csv('Thunder_Applewatch_이다정.csv').drop(['Unnamed: 0'], axis =1)
df_thunder_galaxy_one = pd.read_csv('Thunder_Galaxywatch_이유진.csv')
df_thunder_galaxy_two = pd.read_csv('Thunder_Galaxywatch_이창수.csv').drop(['Unnamed: 0'], axis =1)

# 당근, 번개장터 각 데이터 합침!
df_carrot = pd.concat([df_carrot_apple, df_carrot_galaxy])
df_thunder = pd.concat([df_thunder_apple_one, df_thunder_apple_two, df_thunder_apple_three, df_thunder_galaxy_one, df_thunder_galaxy_two])

import copy
df_carrot_revised = copy.deepcopy(df_carrot[['title', 'price', 'like', 'view', 'category', 'article','total_area_revised', 'time']])
# 컬럼 위치 및 이름 변경
df_carrot_revised.columns = ['title', 'price', 'like', 'view', 'category', 'article', 'location', 'time']
# 당근 타입은 0로 지정
df_carrot_revised['web_types'] = ['0'] * df_carrot_revised.shape[0]

import copy
df_thunder_revised = copy.deepcopy(df_thunder[['title', 'price', 'like', 'view', 'category', 'article', 'location']])
# 번개장터 시간은 없는 관계로 ? 지정
df_thunder_revised['time'] = ['?'] * df_thunder_revised.shape[0]
# 번개장터 타입은 1로 지정
df_thunder_revised['web_types'] = ['1'] * df_thunder_revised.shape[0]
# NaN 데이터 제거
df_thunder_revised = df_thunder_revised.dropna()

# 인덱스 초기화
df_thunder_revised.reset_index(drop =True, inplace = True)
df_carrot_revised.reset_index(drop =True, inplace = True)

df = pd.concat([df_carrot_revised, df_thunder_revised], axis = 0)
df.to_csv('concat_df.csv')