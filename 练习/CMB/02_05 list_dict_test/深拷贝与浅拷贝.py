import copy
aList1=[2,3,["23",32]]
aList2=aList1                #直接复制，aList2等同于aList1
aList3=copy.copy(aList1)     #浅拷贝，aList3的地址与aList1不同，但是里面的所有元素的地址也是一样的
aList4=copy.deepcopy(aList1) #深拷贝，aList4的地址与aList1不同，里面的可变元素地址也不一样，不可变元素的地址一样
print("列表内存地址：",id(aList1),id(aList2),id(aList3),id(aList4))
print("列表可变元素地址:")
print(id(aList1[2]))
print(id(aList2[2]))
print(id(aList3[2]))
print(id(aList4[2]))
print("列表不可变元素地址:")
print(id(aList1[1]))
print(id(aList2[1]))
print(id(aList3[1]))
print(id(aList4[1]))
#改变列表中元素值
aList3[1]=0       #aList3改变了不可变元素的值，产生新值，改变后aList3[1]指向新地址，与aList1[1]已经不同
aList3[2][1]=4    #aList3改变了可变元素的值，未产生新的列表，改变后aList3[2]还是指向旧地址，与aList1[2]地址一样
aList4[2][1]=5    #aList4改变了可变元素的值，未产生新的列表，但是经过深拷贝后aList4[2]本来就和aList1[2]地址不一样，所以aList4[2]的变化与aList1[2]无关系
print("变化后列表的值:")
print(aList1)
print(aList2)
print(aList3)
print(aList4)

