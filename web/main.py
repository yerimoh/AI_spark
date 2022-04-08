'''
실행환경
bootstrap 4.0.0
flask 2.1.1 (pip install flask로 설치)
jinja 3.1.1
keras 2.8.0
tensorflow 2.8.0
python 3.9.0
'''

'''
단순한 정적 웹 사이트를 만들기 위한 micro 웹 프레임워크 flask 사용
http://127.0.0.1:5000/ 로컬 환경에서 해당 웹 페이지 로드
'''

from flask import Flask, render_template, request
import tensorflow as tf
import pandas as pd
import pickle

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import json


'''
예측 모델 두 가지 load
1) model - pkl로 배포한 날씨에 따른 sale값 예측
2) model2 - h5로 배포한 날짜와 sale값 상관관계 예측
'''
# Flask 객체 인스턴스 생성
app = Flask(__name__)
model = pickle.load(open('C:\AI_spark\model\ols_model.pkl','rb'))
model2 = tf.keras.models.load_model('C:\AI_spark\model\predict_sale_model.h5')


'''
URL 방문을 위한 바인딩을 위해 route()로 데코레이터 설정
라우팅 경로 두 가지
1) / (main) - 초기 실행화면인 index.html 출력
2) /predict - 두 번째 실행화면인 예측 결과 출력
'''
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
  data_list = []
  if request.method == 'POST':
    result = request.form
    value = result['select_type'] # 기존 페이지에서 카테고리 선택

    # 1) 기상청 api 날씨값 받아오기
    CallBackURL = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa"
    params = '?' + urlencode({quote_plus("serviceKey"): # 인증키
                                  "Nz12OfSyLZYFTZXsCadoODmgjNCrsMZSVCH6LaESrBrhc%2B%2B3KXskEnz6FXSykKopv4Vr5yhiiAUj0uRXV44j2g%3D%3D",
                              quote_plus("numOfRows"): "10", # 한 페이지 결과 수
                              quote_plus("pageNo"): "1", # 페이지 번호 // default : 1
                              quote_plus("dataType"): "JSON", # 응답자료형식 : XML, JSON
                              quote_plus("stnId"): "108", # 지점번호
                              quote_plus("tmFc"): "202204150600", # 발표시각 // HHMM, 매 시각 40분 이후 호출
                              })

    # URL parsing
    req = urllib.request.Request(CallBackURL + unquote(params))
    # Get Data from API
    response_body = urlopen(req).read() # get bytes data
    # Convert bytes to json
    data = json.loads(response_body) # Result

    # print(data)
    res = pd.DataFrame(data['response']['body']['items']['item'])

    # 1) 2022-04-15 날씨 데이터
    low_temp = 6
    rain = 10
    high_wind = 12.5
    humudity = 56.6
    sunshine = 3.5

    # 2) sale 예측
    prediction = model.predict([low_temp, high_wind, humudity, sunshine])
    prediction = prediction[0]

    # 3) 평균매출대비 예측
    mean = 149090.675585

    pred_input = pd.DataFrame({'일시':['2022-04-15']*21,
                               'sale':[615110,296620,259900,248520,469800
                                   ,648900,373520,64270,286700,161140,106200
                                    ,249090,289100,223920,267200,181350,134600
                                   ,102800,213200,136680,362020]})
    pred_input = pred_input.set_index(keys=['일시'], inplace=False, drop=True)

    y_pred = model2.predict(pred_input)
    prediction2 = y_pred[1]


    '''
    웹 페이지에 예측값 전달
    1) category - 사용자가 선택한 카테고리 분류
    2) temp - 기온
    3) rain - 강수량
    4) sale - 날씨 데이터에 따른 sale 예측값
    5) sale2 - 날짜 데이터에 따른 sale 예측값
    '''
    data_list.append(
        {
            "category": value,
            "temp": low_temp,
            "rain": rain,
            "sale": prediction,
            "sale2" : prediction2
        }
    )

  return render_template('predict.html', result=data_list)

if __name__=="__main__":
  app.run(debug=True)
