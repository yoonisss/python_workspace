# 1 리스트 정의부분
aa = [0, 0, 0, 0]
hap = 0

# 2 리스트의 값 설정. set
aa[0] = int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))

#3 리스트의 값 가져오기. get
hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> %d" % hap)
