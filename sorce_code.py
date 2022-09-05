import random

x = random.randint(1,6)

adad = float(input("adad??"))

if adad > 6:
    print(f"error --> {adad} <--" , "postibani nemikonad")

else:
    if adad == x:
        print(f"hadset drost hast , {x}")
    else:
        print(f"hadset dorost nist , {x}")
exit()