import sys
import time

print("=" * 30)
print("파이썬 실행 테스트를 시작합니다.")
print("=" * 30)

# 1. 단순 텍스트 출력
print(f"현재 파이썬 버전: {sys.version}")

# 2. 간단한 반복문과 계산 출력
print("\n[계산 테스트]")
for i in range(1, 4):
    result = i * 10
    print(f"{i}단계: {i} 곱하기 10은 {result}입니다.")
    time.sleep(0.5)  # 0.5초씩 쉬면서 출력

# 3. 사용자 입력 테스트 (프로그램이 바로 꺼지는지 확인용)
print("\n" + "=" * 30)
input("프로그램이 정상 작동합니다! 엔터를 누르면 종료됩니다.")