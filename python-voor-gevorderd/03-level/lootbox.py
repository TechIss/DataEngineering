import rewards

def skin():

    COMMON = 0
    RARE = 0
    EPIC= 0
    LEGENDARY = 0

    for x in range(5):
        x = rewards.get_new_skin()

        if  x == "COMMON":
            COMMON += 1 
        elif x == "RARE":
            RARE += 1
        elif x == "EPIC":
            EPIC += 1
        else:
            LEGENDARY += 1

    if COMMON > 0:
        print(COMMON, "x Common")

    if RARE > 0:
        print(RARE, "x Rare")

    if EPIC > 0:
        print(EPIC, "x Epic")

    if LEGENDARY > 0:
        print(LEGENDARY, "x Legendary")

skin()
