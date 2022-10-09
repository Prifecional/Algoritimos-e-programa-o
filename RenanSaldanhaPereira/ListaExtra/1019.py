n = int(input(""))


h = n / 3600
n = n % 3600

m = n / 60
n = n % 60



print("%i:%i:%i"% (h, m, n))