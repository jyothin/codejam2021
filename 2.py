#!python3

import sys

T = input()

m = sys.maxsize
x = 0
y = 0

def p(s, ):
    # print(s, )
    return

def cost(s):
    global m
    global x
    global y

    p("s = " + s)

    my_min_c = 0
    r_cj = [j for j in range(len(s)) if s.startswith("CJ", j)]
    p("r_cj = " + str(r_cj))
    my_min_c = my_min_c + len(r_cj) * int(x)
    p("my_min_c = " + str(my_min_c))

    my_min_j = 0
    r_jc = [j for j in range(len(s)) if s.startswith("JC", j)]
    p("r_jc = " + str(r_jc))
    my_min_j = my_min_j + len(r_jc) * int(y)
    p("my_min_j = " + str(my_min_j))

    new_m = my_min_c + my_min_j
    p("new_m = " + str(new_m))

    r = [j for j in range(len(s)) if s.startswith("?", j)]
    p("r = " + str(r))
    if (len(r) == 0):
        if (new_m < m):
            m = new_m
        return

    new_s_c = ""
    new_s_j = ""

    p("Replace with C in " + s)
    new_s_c = s[:r[0]] + "C" + s[r[0]+1:]
    p("new_s_c = " + new_s_c)
    cost(new_s_c)

    p("Replace with J in " + s)
    new_s_j = s[: r[0]] + "J" + s[r[0]+1:]
    p("new_s_c = " + new_s_c)
    cost(new_s_j)


for i in range(1, int(T)+1):
    l = input()
    m = sys.maxsize
    x, y, s = l.split(" ")
    p("m = " + str(m))

    cost(s)

    print("Case #" + str(i) +": "+ str(m))
