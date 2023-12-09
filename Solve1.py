# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

import os
import time


def solution(my_string, target):
    if len(my_string) in range(1, 101) and len(target) in range(1, 101):
        if all(c.islower() for c in my_string) and all(c.islower() for c in target):
            if target in my_string:
                return 1
    return 0

print(solution("asdfasdgasdga","asdga" ))