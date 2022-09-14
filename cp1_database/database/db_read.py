import pandas as pd
import psycopg2
import pickle
import numpy as np
from sklearn.model_selection import train_test_split


#연동하기
conn = psycopg2.connect(
    host='heffalump.db.elephantsql.com', 
    dbname='hezwfjbb',
    user='hezwfjbb',
    password='bwf3k0irq7kZDzoMrnUV2ZXxRD7fXkhZ',
    port=5432)

#커서 생성
cur=conn.cursor()

#조회하기
cur.execute('select * from applewatch_D;')

#조회한 데이터 저장하고 연결끊기
apples = cur.fetchall()

print(apples.types)

#데이터 데이터 프레임화 시키기
df = pd.DataFrame(apples, columns=['manner_degree','title','price','likes','chat','view','category','time','article','total_area_revised'])

print(df)
print(df.info())

cur.close()
conn.close()


###모델명을 알아야 하기때문에 title에서 모델 이름을 뽑아야함
##how?? -> 스트랩이 쓰여있는 로우 지우기.


df = df.copy()
print(df)


# #모델링 하기
# ### 조회수 좋아요 리뷰 기반으로 적정 중고가 추천###

# from sklearn.linear_model import LinearRegression
# from category_encoders import OrdinalEncoder
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import make_pipeline

# df['attention'] = [0] * df.shape[0]
# df['open_closed'] = [0] * df.shape[0]
# df['model'] = [0] * df.shape[0]
# df['discounted'] = [0] * df.shape[0]
# df['origin_price'] = [0] * df.shape[0]

# # 머신러닝 모델링에 필요없는 title, article 컴럼 제거
# df = df.drop(['title', 'article','category','total_area_revised'], axis = 1)

# print(df)

# # target이 attention일지 like 일지 미지정, 만약 둘중에 고르면 과적합 방지를 위해 하나를 제거할 예정!
# target = 'likes'
# X = df.drop(columns = target)
# y = df[target]
# # 훈련, 테스트 데이터로 크게 먼저 나눔
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, train_size = 0.8, random_state = 42)
# # 훈련데이터에서 훈련, 검증 데이터로 나눔
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 0.2, train_size = 0.8, random_state = 42)


# # pipe = make_pipeline(
# #     OrdinalEncoder(),
# #     SimpleImputer(),
# #     LinearRegression()
# # )

# # pipe.fit(X_train, y_train)
# # print('검증 정확도: ', pipe.score(X_val, y_val))

# # pipe.predict(X_test)

# #RandomForest Model

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import RandomizedSearchCV
# from scipy.stats import randint, uniform
# import warnings
# warnings.filterwarnings('ignore')

# # clf = make_pipeline(
# #     OrdinalEncoder(),  
# #     SimpleImputer(), 
# #     RandomForestRegressor(n_jobs=-1, random_state= 42)
# # )

# # dists = {
# #     # 'Targetencoder__smoothing': [2.,20.,50.,100.,500.,1000.], # int로 넣으면 error(bug)
# #     # 'Targetencoder__min_samples_leaf': randint(1, 10),     
# #     # 'iterativeimputer__max_iter': [5, 10, 15], 
# #     'randomforestregressor__n_estimators': randint(100, 120), 
# #     # 'randomforestregressor__max_depth': [5, 10, 13 ,15, 17, 20, 25], 
# #     # 'randomforestregressor__min_samples_leaf' : [1,3,6],
# #     # 'randomforestregressor__max_leaf_nodes' : [300, 600, 1000],
# #     # 'randomforestregressor__max_features': ['sqrt', 'log2', None, 'auto'], # max_features
# #     # 'randomforestregressor__class_weight' : ['balanced', 'balanced_subsample', {0:3, 1:1}, {0:0.657, 1:2.09}]
# # }

# # clf = RandomizedSearchCV(
# #     pipe, 
# #     param_distributions=dists, 
# #     n_iter=3, 
# #     cv=2, 
# #     scoring='r2',  
# #     verbose=1,
# #     n_jobs=-1
# # )

# clf = RandomForestRegressor()

# clf.fit(X_train, y_train)
# clf.predict(X_test)
# print('검증 정확도: ', clf.score(X_val, y_val))

# # random forest에 대한 학습된 모델결과 피클링 부호화
# with open('clf.pkl','wb') as pickle_file:
#     pickle.dump(clf, pickle_file)

