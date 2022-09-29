pay = int(input("시급을 입력하세요 :"))
time = int(input("근무 시간을 입력 하세요 : "))

print(f"하루에 {time}시간만큼 일했을 경우 일급은 {time*pay}입니다.")
print(f"일주일에 5일 근무하면 주급은 {5*time*pay}입니다.")
print(f"한달에 4주 근무하면 월급은 {5*4*time*pay}입니다.")