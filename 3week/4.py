a = input("주민등록번호를 123456-1234567과 같이 입력하세요 : ")

print(f'당신의 성별은 남자 입니까?{int(a[7]) ==1 or int(a[7]) ==3 }')
print(f'당신의 성별은 여자 입니까?{int(a[7])==2 or int(a[7]) ==4}')