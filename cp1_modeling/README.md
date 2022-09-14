# cp1_modeling

df_real_final.csv는 전처리 전 데이터  
real_real_final.csv는 전처리후 최종 데이터 

데이터분석 & 모델링은 Data_Analysis.ipynb  
+추가 데이터분석 & 모델링 및 튜닝 Modeling.ipynb

model : 애플워치, 갤럭시워치  
series : 시리즈별  
size : 사이즈별  
gps/cell : (애플)gps, cell, (번개장터)bluetooth, LTE  
edition : 일반, 에르메스, 골프  
material : aluminium, stainless, titanum  
quality :  상, 중, 하 
unused : 0(개봉), 1(미개봉)     
location : 지역별   
price: 가격   
attention  :  like 95% + view 5%

머신러닝 특성값으로 사용할 컬럼들 :  
price, location, unused, model, series, size, gps/cell, edition, material, quality, attention
