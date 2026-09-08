def power (base,exponent):
    if exponent == 0: #base condition 2==0
        return 1
    return base* power (base,exponent -1)
print (power(2,0))
print (power(2,2))
print (power(2,4))