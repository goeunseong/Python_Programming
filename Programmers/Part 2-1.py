# TODO Part 2-1

"""
* 입력 설명 *
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.

* 출력 설명 *
a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

* 제한 조건 *
a와 b는 자연수입니다.
"""


def solution_2():
    a, b = map(int, input().strip().split(' '))
    print(*divmod(a, b))

solution_2()
# divmod를 사용하면 몫과 나머지를 함께 계산할 수 있음. 큰 숫자를 처리할 때 유용
