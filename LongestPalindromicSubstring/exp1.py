

class Solution:

    def c(self, a):
        if not a:
            return 0
        a = list(a)
        a = "#" + "#".join(a) + "#"
        maxe = 0
        va = ""
        for index, value in enumerate(a):
            c = 0
            n = 0
            v = value
            while -1 < index - n and index + n < len(a):
                pre = a[index - n]
                nex = a[index + n]
                if pre == nex:
                    c += 1
                    if index - n == index + n:
                        pass
                    else:
                        v = pre + v + nex
                    n += 1
                else:
                    break
            maxe = max(maxe, c)
            if maxe == c:
                va = v
        # return maxe // 2
        return va.replace("#", "")

if __name__ == '__main__':
    a = Solution()
    print(a.c("tattarrattat"))
    print(a.c("abba"))
    print(a.c("aba"))
    print(a.c("a"))
    print(a.c("abcd"))