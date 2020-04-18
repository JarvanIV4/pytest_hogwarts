# 列表练习
list_t = [1, 5, 6, 2, 7, 3, 0]

# 列表反转  [0, 3, 7, 2, 6, 5, 1]
print(list_t[::-1])  # 列表切片
print(list(reversed(list_t)))  # reversed()函数
list_new = []
for i in range(len(list_t)):
    list_new.append(list_t[-(i+1)])
print(list_new)

# 列表排序(升序)  [0, 1, 2, 3, 5, 6, 7]
print(sorted(list_t, reverse=False))  # list的sorted函数
# 冒泡排序
for i in range(len(list_t)-1):
    for j in range(len(list_t)-i-1):
        if list_t[j] > list_t[j+1]:
            list_t[j], list_t[j+1] = list_t[j+1], list_t[j]
print(list_t)