tt = ((1, 2, 3),
(4, 5, 6),
(7, 8, 9))

print(tt)
print(tt[0][0])
for i in range(0,3):
    for k in range(0,3):
        print (tt[i][k], end=" ")
    print()    