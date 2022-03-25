from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium.webdriver.common.by import By



chinese = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/232318/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/450579/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/388655/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/386894/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/482892/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/511898/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1052353/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/449385/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/420905/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1016508/']

korean = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/232899/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/224438/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/364216/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/254924/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/261695/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/447499/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/524436/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/54603/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/247216/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/215476/',]

western = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/56041/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/450128/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/442348/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/375222/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/445730/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/280344/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/293756/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/553158/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/484080/',
           'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/555610/']


desert = ['https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/505362/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1021611/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/452419/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/525247/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1001529/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/441376/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/490133/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/492680/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1005655/',
          'https://www.yogiyo.co.kr/mobile/?gclid=CjwKCAjwiuuRBhBvEiwAFXKaND8GP-OHrEaJ7ImxyEFNNV1eF0AFz6edwG1yJrYGgMzQMrC38RRFFRoCQyAQAvD_BwE#/1007287/']


categories = []
categories.append(chinese)
categories.append(korean)
categories.append(western)
categories.append(desert)

csv_num = 0

for category in categories:
    for url in category:
        driver = webdriver.Chrome('/Users/sungho/Downloads/chromedriver')  # 크롬드라이버 경로 설정
        driver.get(url)  # 사이트 오픈

        # 리뷰버튼 클릭
        review_xpath = '''//*[@id="content"]/div[2]/div[1]/ul/li[2]/a'''
        driver.find_element(by=By.XPATH, value=review_xpath).click()
        time.sleep(3)

        # 더보기
        while True:
            try:
                css_selector = '#review > li.list-group-item.btn-more > a'
                more_reviews = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
                more_reviews.click()
                time.sleep(2)
            except:
                break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
        time.sleep(2)
        pre_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤 위치 저장

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
            time.sleep(1)
            cur_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤을 저장한다.
            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            if pre_height == cur_height:
                break
            # pre_height == cur_height
            pre_height = cur_height

        time.sleep(3)

        # 페이지 소스 출력
        html = driver.page_source
        html_source = BeautifulSoup(html, 'html.parser')

        # print(html_source)

        # 데이터 추출
        restaurant_name = html_source.find("span", class_="restaurant-name ng-binding")  # 업체명
        review_taste = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                                "ng-show": "review.rating_taste > 0"})  # 별점-맛
        review_quantity = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                                "ng-show": "review.rating_quantity > 0"})  # 별점-양
        review_delivery = html_source.find_all("span", attrs={"class": "points ng-binding",
                                                                "ng-show": "review.rating_delivery > 0"})  # 별점-배달
        order_menu = html_source.find_all("div", class_="order-items default ng-binding")  # 주문 메뉴
        customer_review = html_source.find_all("p", attrs={"class": "ng-binding",
                                                                "ng-show": "review.comment"})  # 리뷰

        # csv 파일 만들기 위한 list 설정
        tastes = []
        quantitys = []
        deliverys = []
        menus = []
        reviews = []

        # 데이터 배열
        for i, j, l, m, n in zip(review_taste, review_quantity, review_delivery, order_menu, customer_review):
            tastes.append(i.string)
            quantitys.append(j.string)
            deliverys.append(l.string)
            menus.append(m.string)
            reviews.append(n.string)

        time.sleep(20) # 크롤링 소요시간 임의 설정
        # driver.close()  # 크롬드라이버 종료


        '''
        csv 파일로 저장하기
        '''
        reviews = pd.DataFrame({'업체명':restaurant_name, '맛':tastes,'양':quantitys,
                                '배달':deliverys,'주문메뉴':menus, '상세리뷰':reviews})
        print(reviews)

        # while True:
        #     try:
        #         reviews.to_csv("C:\pythonProject\crawl_data\review " + '.csv', encoding='cp949')
        #         break
        #     except Exception as e: # 인코딩 에러 예외처리
        #         error_character = str(e).split(' ')[5].replace('\'', '')
        #         reviews = reviews.replace(u'{}'.format(error_character), u'', regex=True)

        reviews.to_csv("/Users/sungho/PycharmProjects/python/reviews/detail_review{}.csv".format(csv_num), index=False, encoding="utf-8-sig")
        csv_num += 1


# 생성된 dataframe concatenate
lists_tmp=[]
concat_df_num=0

for i in range(40):
    globals()['df_{}'.format(i)] = pd.read_csv('/Users/sungho/PycharmProjects/python/reviews/detail_review{}.csv'.format(i))
    # csv파일 번호의 나머지가 9일때마다 카테고리가 바뀐다.
    lists_tmp.append(globals()['df_{}'.format(i)])
    if i % 10 == 9:
        globals()['concat_df{}'.format(concat_df_num)]=pd.concat(lists_tmp)
        lists_tmp.clear()
        concat_df_num+=1

# concatenate된 파일 저장
concat_df0.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_chinese.csv", index=False, encoding="utf-8-sig")
concat_df1.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_korean.csv", index=False, encoding="utf-8-sig")
concat_df2.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_western.csv", index=False, encoding="utf-8-sig")
concat_df3.to_csv("/Users/sungho/PycharmProjects/python/reviews/reviews_dessert.csv", index=False, encoding="utf-8-sig")
