'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
这道题在算法导论中快速排序里面有类似的题目
'''


def index(arra, indx):
    if not arra:
        return None
    try:
        return arra[indx]
    except IndexError:
        return arra[-1]

class Solution:

    def __init__(self):
        pass

    @staticmethod
    def median(A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m # 这里确保A是短的那个数组
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    def media(self, arra, arrb):
        la = len(arra)
        lb = len(arrb)
        if la  > lb:
            arra, arrb = arrb, arra
            la, lb = lb, la
            # 这里确保a是两个数组中比较短的那个
        mid = 0
        ba=bb=0
        ma = mb = 0
        while mid <= (la+lb) / 2 + 1:
            print((la+lb) / 2, mid, ba, bb, ma, mb)
            if ba == la:
                ma = arrb[bb+1]
                mb = arrb[bb]
                bb += 1
                mid += 1

                continue
            if bb == lb:
                ma = arra[ba+1]
                mb = arrb[ba]
                ba +=1
                mid += 1

                continue
            if arra[ba] < arrb[bb]:
                mb = arrb[bb]
                ba += 1
                mid += 1
            else:
                ma = arra[ba]
                bb += 1
                mid += 1

        if (la+lb) % 2 == 1:
            print("..............")
            return mb
        else:
            print("-----------")
            return (ma+mb) / 2

    def merge(self, A, B):
        c = []
        la = len(A)
        lb = len(B)
        mid = (la + lb) // 2 + 1
        ba = bb = -1
        while ba < la-1 and bb < lb-1:
            ka = A[ba+1]
            kb = B[bb+1]
            if ka < kb:
                c.append(ka)
                ba += 1
            else:
                c.append(kb)
                bb += 1
            if len(c) == mid:
                break
        ba += 1
        bb += 1
        if len(c) < mid:
            print(mid, len(c), ba, bb)
            if ba == la:
                pp = B[bb:mid-ba]
                print(pp)
            else:
                print("......")
                pp = A[ba:mid-bb]
                print(pp)
            c.extend(pp)
        if (la+lb) % 2 == 1:
            return c[-1]
        else:
            return (c[-1] + c[-2]) / 2


if __name__ == '__main__':
    m = Solution()
    # b = [1, 2, 4, 5]
    # a = [1, 3]
    # a = [1, 3, 4, 5, 7, 9]
    # b = [2, 3, 4, 6, 7]
    # a =  [1, 3]
    # b = [2]
    # a = [1,2]
    # b = [3,4]
    a = [1,2]
    b = [1,1]
    print(m.merge(a, b))