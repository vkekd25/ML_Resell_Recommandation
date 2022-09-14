# cp1_preprocessing

컬럼 'web_types'는 0은 당근마켓, 1은 번개장터  
시간 분, 시간, 일을 일 기준으로 통일  
concat_df는 총 당근마켓, 번개장터 합친 데이터  

스크래핑시 필요한 csv파일  
Carrot_Applewatch.csv  
Carrot_Galaxywatch.csv  
Thunder_Applewatch_One.csv  
Thunder_Applewatch_Two.csv  
Thunder_Applewatch_Three.csv  
Thunder_Galaxywatch_One.csv  
Thunder_Galaxywatch_Two.csv  


carrot_preprocessing.py는 당근마켓 스크래핑시 간단한 전처리  
carrot_thunder_concat.py는 본격적으로 당근마켓, 번개장터 데이터 합친후 간단한 전처리  


preprocessing_update.ipynb는 전처리 코드  
concat_df.csv는 전처리시 필요한 csv파일  
df_real_fanal.csv는 전처리 후 csv파일  

NanumBarunGothic.ttf는 월드클라우드 할때 font 파일
