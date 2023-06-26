# 신나는 함수 실행, 9184번, 백준

# my thoughts :
# 1. By using Dynamic Programming, We can solve it..!!
# 2. 잉..??

import sys

input = sys.stdin.readline

d = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if(d[a][b][c] !=0 ):
        return d[a][b][c]
    elif a < b < c:
        d[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        d[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return d[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if (a == -1 and b == -1 and c == -1):
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
