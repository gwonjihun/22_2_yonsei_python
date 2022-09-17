default_pay = int(input("기본 통신비 : "))
datas = int(input("기본 데이터량 :"))
per_pay = int(input("1기가당 추가 통신비 :"))
use_per_month = int(input("한 달 기본 사용량 :"))

print(f"{datas}기가까지 {default_pay}원")
print(f"{use_per_month}기가 사용하면 {default_pay+(use_per_month-datas)*per_pay}원")