grapesEatingCount = list(map(int, input().split()))
grapesCount = list(map(int, input().split()))


def first():
    grapesCountAfterEaten = grapesCount[0] - grapesEatingCount[0]
    grapesCount[0] = grapesCountAfterEaten
    if grapesCountAfterEaten < 0:
        return False
    else:
        return True


def second():
    count = grapesEatingCount[2]
    grapesLeft = grapesCount[0] - count
    if grapesLeft < 0:
        grapesCount[0] = 0
        grapesLeft = grapesCount[1] + grapesLeft
        if grapesLeft < 0:
            return False
        else:
            grapesCount[1] = grapesLeft
            return True
    else:
        grapesCount[0] = grapesLeft
        return True


def third():
    count = grapesEatingCount[2]
    grapesLeft = grapesCount[0] - count
    if grapesLeft < 0:
        grapesCount[0] = 0
        grapesLeft = grapesCount[1] + grapesLeft
        if grapesLeft < 0:
            grapesCount[1] = 0
            grapesLeft = grapesCount[2] - grapesLeft
            if grapesLeft < 0:
                return False
            else:
                grapesCount[1] = grapesLeft
                return True
        else:
            grapesCount[1] = grapesLeft
            return True

    grapesCount[0] = grapesLeft
    return True


if first():
    if second():
        if third():
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")

print(grapesCount)
