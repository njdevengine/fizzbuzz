def fun(a):
    n = 0
    i = 30
    while i>0:
        if n<30:
            print(" "*n,a*n)
            n+=1
        else:
            print(" "*i,a*i)
            i = i-1
import string
alpha = (string.ascii_lowercase)

for i in alpha:
    fun(i)
