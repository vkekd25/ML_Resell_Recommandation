import pandas as pd
import copy

# 처음 당근마켓에서 크롤링시 
df_galaxy = pd.read_csv('data_galaxywatch.csv')
df_apple = pd.read_csv('Carrot_Applewatch.csv')
df = copy.deepcopy(df_apple)

# 모든 사이트 전처리 모으기전에 간단한 전처리 진행
def preprocessing(df):

    # 크게 도, 시로만 추출!
    total_area_list = df.total_area.tolist()
    article_list = df.article.tolist()

    # na 제거해서 스크래핑시 인덱스 밀린것 정리
    total_area_revised = [x for x in total_area_list if pd.isna(x) == False]
    article_revised = [x for x in article_list if pd.isna(x) == False]
    df['total_area_revised'] = pd.Series(total_area_revised)
    df['article'] = pd.Series(article_revised)

    # 'total_area', 'Unnamed: 0' 컬럼 제거
    df.drop(columns = ['total_area','Unnamed: 0'],inplace = True)
    df.dropna(axis = 0, inplace = True)
    return df

df = preprocessing(df)

# 'area' 컬럼 제거
df.drop(columns = 'area', inplace = True)
# 가격 컬럼 '가격없음' 카디널리티 제거!
df = copy.deepcopy(df[df.price != '가격없음'])
# price NaN Drop!
df.dropna(inplace = True)

# 가격안에 특수문자 제거!
def price_cleaning(x):
    x = str(x).replace(',', '')
    x = str(x).replace('원', '')
    x = str(x).replace('만', '0000') # ~만 -> ~0000
    x = str(x).replace(' ', '') # 145만 4000원  -> 1454000
    x = str(x).replace('억', '')
    return int(x)

# 크게 도, 시로만 추출!
def area_cleaning(x):
    x = str(x).split(' ')[0] # 도, 광역시로만 나눔
    return x

# like에 특수문자 제거
def like_cleaning(x):
    # 숫자만 남김
    x = str(x).replace('관심', '') 
    x = str(x).replace('∙', '')
    return int(x)

# chat에 특수문자 제거
def chat_cleaning(x):
    # 숫자만 남김
    x = str(x).replace('채팅', '')
    return int(x)

# view에 특수문자 제거
def view_cleaning(x):
    # 숫자만 남김
    x = str(x).replace('조회', '')
    return int(x)

# 카테고리에 특수문제 제거
def category_cleaning(x):
    # 카테고리 '∙' 제거
    x = str(x).replace(' ∙', '')
    return x

# 시간부분에 특수문자 제거
def time_cleaning(x):
    # 끌올, 전 단어 제거
    x = str(x).replace('끌올 ', '')
    x = str(x).replace(' 전', '')
    return x

# 각 해당 컬럼 함수 apply 적용
df['total_area_revised'] = df['total_area_revised'].apply(area_cleaning)
df['price'] = df['price'].apply(price_cleaning)
df['like'] = df['like'].apply(like_cleaning)
df['chat'] = df['chat'].apply(chat_cleaning)
df['view'] = df['view'].apply(view_cleaning)
df['category'] = df['category'].apply(category_cleaning)
df['time'] = df['time'].apply(time_cleaning)
df.head(3)