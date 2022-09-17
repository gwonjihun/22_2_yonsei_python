price = int(input("물건값을 입력하시오 : "))
pr_1000 = int(input("1000원 지폐개수 : "))
pr_500 = int(input("500원 지폐개수 : "))
pr_100 = int(input("100원 지폐개수 : "))
as_500,as_100,as_10,as_1 = 0,0,0,0
return_pay = pr_1000*1000+pr_500*500+pr_100*100 - price
print(return_pay)
as_500 = return_pay//500
print(as_500)
return_pay = return_pay-(as_500*500)
as_100 = return_pay//100
return_pay = return_pay-(as_100*100)
as_10 = return_pay//10
return_pay = return_pay-(as_10*10)
print(f"500= {as_500},100= {as_100},10= {as_10},1= {return_pay}")