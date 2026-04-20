a = float(input("첫 번째 숫자를 입력하세요: "))
b = float(input("두 번째 숫자를 입력하세요: "))

print("덧셈 결과:", a + b)
print("뺄셈 결과:", a - b)
print("곱셈 결과:", a * b)

if b != 0:
    print("나눗셈 결과:", a / b)
else:
    print("나눗셈 결과: 0으로 나눌 수 없습니다.")