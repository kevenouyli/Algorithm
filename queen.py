# def queen(A, cur=0):
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 print('A:',A)
#                 break
#
#         if flag:
#             queen(A, cur+1)
# queen([None]*8)


import itertools
#
# s = "['a', 'b'],['c', 'd']"
# print("eval(s):",eval(s))
# print("*eval(s):",*eval(s))
# for i in itertools.product(*eval(s)):
#     print(i)
# for i in itertools.product(eval(s)):
#     print(i)

i = 0
for item in itertools.count(100, 2):
    i += 1
    if i > 10: break

    print(item)