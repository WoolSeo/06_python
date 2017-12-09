#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:17:42 2017

@author: woolseo
"""
import pdairp

#따옴표 안에 들어간 긴 문자열은 키값으로 일종의 비밀번호와 같은거에요.
data = pdairp.PollutionData("nESF1DreNeshOI7Q6zdswaS7wzLtVFLILOfnpEs%2B2QIUSVhqQoZ6udu8Eil%2FNLlWOP4UfsTvE%2B4DJQaZyjekaA%3D%3D")

pm10 = data.station('인계동', "DAILY")['0']['pm10Value'] #수원시 정자동
pm25 = data.station('인계동', "DAILY")['0']['pm25Value'] #수원시 정자동

print("pm10 value " + pm10)
print("pm25 value " + pm25)

a = int(input("미세 먼지 수치를 입력하세요. :"))
if a > 151:
    print("매우 나쁨")
elif a > 81:
    print("나쁨")
elif a > 31:
    print("보통")
else:
    print("좋음")
    
    
b = input("민감군입니까?(y/n) : ")
if b == "y" and a > 151: 
    print("가급적 실내활동. 실외활동시 의사와 상의")
elif b == "y" and a > 81:
    print("장시간 또는 무리한 실외활동 제한. 특히 천식을 앓고 있는 사람이 실외에 있는 경우 흡입기를 더 자주 사용할 필요가 있음")
elif b == "y" and a > 31:
    print("장시간 또는 무리한 실외활동 제한. 특히 천식을 앓고 있는 사람이 실외에 있는 경우 흡입기를 더 자주 사용할 필요가 있음")
else:
    pass
if b == "n" and a > 151: 
    print("장시간 또는 무리한 실외활동 제한. 목의 통증과 기침 등의 증상이 있는 사람은 실외활동을 피해야 함")
elif b == "n" and a > 81:
    print("장시간 또는 무리한 실외활동 제한. 특히 눈이 아픈 증상이 있거나 기침이나 목의 통증으로 불편한 사람은 실외활동을 피해야 함")
elif b == "n" and a > 31:
    print("행동 요령이 없습니다.")
else:
    pass