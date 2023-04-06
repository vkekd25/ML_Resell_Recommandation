# Team_ML_Resell_Recommandation

## 부트캠프 ML 팀 프로젝트
<br>
- 코드스테이츠 AI 부트캠프 과정중에 ML 팀 프로젝트입니다. 


## Team_ML_Resell_Recommandation
- **프로젝트 주제**
  - 중고거래 사이트(당근마켓, 번개장터등)의 실시간 상품 정보(모델명, 상품상태, 가격등)들의 특성들을 바탕으로 ML을 이용한 상품 관심도 예측 및 가격 추천

- **프로젝트 개요**
  - 중고거래 사이트(당근마켓, 번개장터등)의 해당상품 정보 스크래핑
  - 스크래핑을 통해 정제되지않은 데이터들 전처리
  - Catboost ML모델을 통한 상품 관심도 예측
  - 관심도를 바탕으로 사용자의 예상가격을 추천

- **프로젝트 결과**  
rmse : 39 → 32  
r^2 : -0.1 -> 0.3


- **데이터**  
  - 당근마켓(https://www.daangn.com/) 스크레이핑
  - 번개장터(https://m.bunjang.co.kr/) 스크레이핑

- **코드참고**
  - Catboost 모델
    - 웹사이트명: Catboost 공식문서
    - URL: https://catboost.ai/en/docs/concepts/python-reference_catboostregressor
  - bs4 beautifulsoup 라이브러리
    - 웹사이트명: bs4 공식문서 
    - URL: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
     

- **발표영상 링크**    
<img src="http://img.youtube.com/vi/G7dGv7ONPPA/0.jpg" width="700" height="400"/> <br>
(https://youtu.be/G7dGv7ONPPA)

<br><br>

cp1_scarping - 데이터수집  
cp1_database - 데이터베이스  
cp1_preprocessing - 데이터전처리  
cp1_modeling - 데이터분석 및 모델링  
cp1_flask - 웹구축  
AI_13_3팀_프로젝트계획서.docx - 프로젝트 계획서    
AI_13_3team_cp1.pptx - 프로젝트 보고서 및 발표자료  
