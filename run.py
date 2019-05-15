# 인터파크 투어 사이트에서 여행지를 입력후 검색 -> 잠시후 -> 결과
# 로그인시 PC 웹 사이트에서 처리가 어려울 경우 -> 모비일 로그인 진입
# 모듈 가져오기
# pip install selenium
from selenium import webdriver as wd

# 사전에 필요한 정보를 로드 => db or shell or batch 파일에서 인자로 받아서 세팅
main_url = 'http://tour.interpark.com/'

# 드라이버 로드
#driver = wd.Chrome(executable_path='./chromedriver')
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 -> 옵션 부여하여(프록시, 에이전트 조작, 이미지를 배제)
# 크롤링을 오래돌리면 => 임시파일들이 쌓인다!! -> 템프 파일 삭제

# 사이트 접속(get)
driver.get(main_url)

# 검색창을 찾아서 검색어 입력

# 검색 버튼 클릭

# 잠시 대기 => 페이지가 로드되고 나서 즉각적으로 데이터를 획득 하는 행위는
# 자제 =>