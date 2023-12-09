# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

import os
import time

def solution(age):
    if age <= 1000:
        age_str = str(age)
        answer = ''

        for char in age_str:
            digit = int(char)
            planet_age = chr(ord('a') + digit)
            answer += planet_age

        return answer
    
age_programmer_857 = 824
result = solution(age_programmer_857)
print(result)