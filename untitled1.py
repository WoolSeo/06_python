import pdairp
data = pdairp.PollutionData('nESF1DreNeshOI7Q6zdswaS7wzLtVFLILOfnpEs%2B2QIUSVhqQoZ6udu8Eil%2FNLlWOP4UfsTvE%2B4DJQaZyjekaA%3D%3D')
pm10 = int(data.station('대명동', 'DAILY')['0']['pm10Value'])
pm25 = int(data.station('대명동', 'DAILY')['0']['pm25Value'])

a = input('민감군입니까?(y/n)')

print('미세먼지 농도 : %d' %pm10)

if pm10 >= 151 :
    print('미세먼지 등급 : 매우 나쁨')
    if a == 'y' :
        print('행동 요령 : 가급적 실내활동. 실외활동시 의사와 상의')
    else :
        print('행동 요령 : 장시간 또는 무리한 실외활동 제한. 목의 통증과 기침 등의 증상이 있는 사람은 실외활동을 피해야 함')
elif pm10 >= 81:
    print('미세먼지 등급 : 나쁨')
    if a == 'y' :
        print('행동 요령 : 장시간 또는 무리한 실외활동 제한. 특히 천식을 앓고 있는 사람이 실외에 있는 경우 흡입기를 더 자주 사용할 필요가 있음')
    else :
        print('행동 요령 : 장시간 또는 무리한 실외활동 제한. 특히 눈이 아픈 증상이 있거나 기침이나 목의 통증으로 불편한 사람은 실외활동을 피해야 함')        
elif pm10 >= 31:
    print('미세먼지 등급 : 보통')
    if a == 'y' :
        print('행동 요령 : 장시간 또는 무리한 실외활동 제한. 특히 천식을 앓고 있는 사람이 실외에 있는 경우 흡입기를 더 자주 사용할 필요가 있음')
    else :
        print('별도의 행동 요령이 없습니다.')
else:
    print('미세먼지 등급 : 좋음')
    print('별도의 행동 요령이 없습니다.')