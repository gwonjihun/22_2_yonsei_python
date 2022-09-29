pp = int(input("MT 인원수 : "))
wa = int(input("1인당 생수 개수 : "))


print(f'필요한 생수 개수 {pp*wa}')
print(f'생수 팩 구매량 {(pp*wa)//15}개, {(pp*wa)//15*10000}원')
print(f'생수 낱개 구매량{(pp*wa)%15}개, {(pp*wa)%15*900}')
print(f'생수 총 구매 비용 {(pp*wa)//15*10000+ (pp*wa)%15*900}원')