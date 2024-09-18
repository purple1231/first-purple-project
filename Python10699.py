from datetime import datetime

#datatime 모듈에 있는 datatime 클래스를 가져온다?
#datetime.now(): datetime 클래스의 now() 메서드를 호출하여 
#현재 시점의 날짜와 시간을 담은 datetime 객체를 반환합니다.

now = datetime.now()
dateNow = now.date()
print(dateNow)

