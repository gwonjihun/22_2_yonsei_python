pay = int(input("기계값 입력 : "))
months= int(input("사용 개월 수 : "))
per_months= pay/24
print(f"매달 내는 돈 = {per_months:.1f}원")
print(f"남은 약정 기간 = {24-months}개월")
print(f"위약금 = {(24-months)*per_months}")