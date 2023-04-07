i = input("문자열 입력 : ")

if i.isdigit() :
       print('숫자입니다.')
elif i.isalpha() :
   print('글자입니다.')
elif i.isalnum() :
   print('글자+숫자입니다.')
else :
     print('모르겠습니다.')

