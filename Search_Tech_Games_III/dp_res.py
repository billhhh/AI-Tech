
def main():

    f = []
    res = []
    cur_money = 15
    f.append(0)  # f[0] == 0
    res.append([])

    for i in range(1, cur_money + 1):
        cost = 99999
        tmp_res = []

        if i - 1 >= 0:
            cost = min(cost, f[i-1] + 1)
            tmp_res += res[i-1]
            tmp_res.append(1)

        if i - 5 >= 0:
            cost_copy = cost
            cost = min(cost, f[i-5] + 1)
            if cost < cost_copy:
                tmp_res = []
                tmp_res += res[i-5]
                tmp_res.append(5)

        if i - 11 >= 0:
            cost_copy = cost
            cost = min(cost, f[i-11] + 1)
            if cost < cost_copy:
                tmp_res = []
                tmp_res += res[i-11]
                tmp_res.append(11)

        f.append(cost)
        print("f[%d]=%d" % (i, f[i]))
        res.append(tmp_res)
        print("Solution:", tmp_res)


if __name__ == "__main__":
    main()
