piz1 = int(input("불고기 조각 수 :"))
piz2 = int(input("쉬림프 조각 수 :"))

print(f'불고기피자 {piz1}조각')
print(f'쉬림프피자 {piz2}조각')
print(f'조각 가능? : {(piz1+piz2) % 2 == 0}')