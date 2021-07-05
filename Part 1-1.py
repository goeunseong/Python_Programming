# 프로그래머스 강의_파이썬을 파이썬답게

# TODO Part 1-1

"""
정수를 담은 이차원 리스트, my_list 가 solution 함수의 파라미터로 주어집니다.
my_list에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

* 제한 조건 *
my_list의 길이는 100 이하인 자연수입니다.
my_list 각 원소의 길이는 100 이하인 자연수입니다.

* 예시 *
input = [[1], [2]], output = [1,1]
input = [[1,2], [3,4], [5]] = [2,2,1]
"""


def solution(my_list):
    answer = []
    for i in range(len(my_list)):
        answer.append(len(my_list[i]))
    return answer


def main_1():
    my_list = [[1, 2], [2, 2], [5]]
    solution(my_list)


# num = int(input())
# my_list = [[int(x) for x in input().split()] for y in range(num)]

main_1()
