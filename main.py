## 함수 선언부
def add_func(n1, n2):
    return n1+n2

def sub_func(n1, n2):
    return n1-n2

def ex_func(n1, n2):
    return n1**n2


## 전역 변수부
num1, num2, res = 100, 200, 0
num3, num4, res = 4, 3, 0


## 메인 코드부
res = add_func(num1, num2)
print(num1, "+", num2, "=", res)

res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)

res = ex_func(num3, num4)
print(num3, "**", num4, "=", res)
