데이터 설명

* '한식리뷰데이터' 에는 각 한식 업체별 리뷰가 총 17개 저장되어 있습니다.
* '카페리뷰데이터' 에는 각 카페 업체별 리뷰가 총 17개 저장되어 있습니다.
* 'korean_concat' 은 각 한식 업체별 리뷰를 concatenate한 파일입니다.
* 'korean_neg' 는 'korean_concat'에서 별점 4점 이하 부정 리뷰만 추출한 파일입니다.
* 'korean_neg2' 는 'korean_concat'에서 별점 3점 이하 부정 리뷰만 추출한 파일입니다.
* 'cafe_concat' 은 각 카페 업체별 리뷰를 concatenate한 파일입니다.
* 'cafe_neg' 는 'cafe_concat'에서 별점 4점 이하 부정 리뷰만 추출한 파일입니다.
* 'cafe_neg2' 는 'cafe_concat'에서 별점 3점 이하 부정 리뷰만 추출한 파일입니다.
* preprocessing.ipynb는 전처리시 사용한 코드입니다. 업체별 리뷰 데이터를 concatenate하고, index를 초기화 하고, 날짜에 '하루 전', '일주일 전', '50분 전' 등이 포함되어 있는 경우 해당 행을 제거했습니다.
