str = '소문자abc 대문자ABC'
str1 = '1:2:3'

print("split >",str.split())
print("split >",str1.split(':'))
print("join >",':'.join(str))
print("replace >",str.replace(' ','*'))
print("upper >",str.upper())
print("lower >",str.lower())
print("swapcase >",str.swapcase())
print("title >",str.title())