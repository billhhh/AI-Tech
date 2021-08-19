
def main():

    f = []
    cur_money = 15
    f.append(0)  # f[0] == 0

    for i in range(1, cur_money + 1):
        cost = 99999
        if i - 1 >= 0:
            cost = min(cost, f[i-1] + 1)

        if i - 5 >= 0:
            cost = min(cost, f[i-5] + 1)

        if i - 11 >= 0:
            cost = min(cost, f[i-11] + 1)

        f.append(cost)
        print("f[%d]=%d" % (i, f[i]))


if __name__ == "__main__":
    main()
