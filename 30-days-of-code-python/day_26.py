dA, mA, yA = map(int, input().split())
dE, mE, yE = map(int, input().split())

if yA > yE:
    print(10000)
elif yA == yE:
    if mA > mE:
        print(500 * (mA-mE))
    elif mA == mE:
        print(15 * (dA-dE))
    else:
        print(0)
else:
    print(0)