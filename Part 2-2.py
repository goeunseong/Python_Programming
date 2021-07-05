# TODO Part 2-3. n진법으로 표기된 string을 10진법 숫자로 변환하기

"""
* 문제 설명 *
base 진법으로 표기된 숫자를 10진법 숫자 출력.

* 입력 설명 *
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

* 출력 설명 *
base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.

* 제한 조건 *
base는 10 이하인 자연수입니다.
num은 3000 이하인 자연수입니다

예시
input	output
12 3	5
444 5	124.
"""


def solution_3():
    num, base = map(int, input().strip().split(' '))
    num_ = str(num)
    print(int(num_, base))

solution_3()
