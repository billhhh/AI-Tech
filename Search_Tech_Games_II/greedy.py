
def main():

    ONECENT=1
    FIVECENT=5
    TENCENT=10
    TWENTYFINECENT=25

    cur_money = 41
    num_25 = 0
    num_10 = 0
    num_5 = 0
    num_1 = 0

    # Try different denominations
    while cur_money >= TWENTYFINECENT:
        num_25 += 1
        cur_money -= TWENTYFINECENT

    while cur_money >= TENCENT:
        num_10 += 1
        cur_money -= TENCENT

    while cur_money >= FIVECENT:
        num_5 += 1
        cur_money -= FIVECENT

    while cur_money >= ONECENT:
        num_1 += 1
        cur_money -= ONECENT

    # output
    print("25 cents：", num_25)
    print("10 cents：", num_10)
    print("5 cents：", num_5)
    print("1 cents：", num_1)


if __name__ == "__main__":
    main()
