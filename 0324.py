a = int(input())
a *= int(input())
a *= int(input())

# list() : 각각의 문자들을 리스트로 만든다.
each = list(str(a))

for i in range(10):
    # count() : 리스트 안에 원하는 요소의 갯수를 구한다.
    print(each.count(str(i)))
