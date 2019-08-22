from random import randint

if __name__ == '__main__':
    a = [randint(1, 200) for _ in range(7)]
    a.sort()
    b = [randint(1, 200) for _ in range(7)]
    b.sort()
    print(a)
    print(b)
    a = [9, 29, 123, 139, 152, 163, 200]
    b = [25, 26, 28, 50, 104, 121, 171]
    for m in range(1, 100):
        a = [randint(1, 200) for _ in range(7)]
        a.sort()
        b = [randint(1, 200) for _ in range(7)]
        b.sort()
        c = a+b
        c.sort()
        print((a[3]+b[3])/2)
        print((c[6]+c[7])/2)
        print('..............')
        # print()