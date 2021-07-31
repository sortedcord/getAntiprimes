def getFactors(number):
    factors = []
    for y in range(1, number + 1):
        if number % y == 0:
            factors.append(y)
    return factors

endcap = int(input("Enter endcap (Starts with 4): "))
number = 1

anti = []

while number<=endcap:
    factors = getFactors(number)
    anti.append(len(factors))
    number = number + 1

print(max(anti), anti.index(max(anti))+1)