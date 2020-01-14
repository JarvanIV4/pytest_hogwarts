class Practice:
    # 九九乘法表
    def cf(self):
        for i in range(1, 10):
            for j in range(1, i+1):
                print("%d×%d=%2d "%(j, i, j*i), end="")
            print()

    # 冒泡排序
    def bubble_sort(self, nums_list):
        for i in range(len(nums_list)-1):
            for j in range(len(nums_list)-i-1):
                if nums_list[j]>nums_list[j+1]:
                    nums_list[j],nums_list[j+1] = nums_list[j+1],nums_list[j]
        return nums_list

    """
    列表排序方法sort(),示例：
    1. nums_list.sort()  # 从大到小排序
    2. nums_list.sort(reverse=True) # 从大到小排序
    """



if __name__ == '__main__':
    t = Practice()
    t.cf()
    list_a = [7, 4, 1, 9, 3, 2, 6]
    print(t.bubble_sort(list_a))
    list_a.sort(reverse=True)
    print(list_a)
    str_ = "   et et  "
    print(str_.strip()) # 去除字符串开头和结尾的空格

