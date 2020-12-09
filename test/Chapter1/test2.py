#数组操作
import numpy as np #导入numpy工具包

# array = np.array([2,3,4,5,6])   #定义一维数组array
# print(array[0])    #取出第一个元素
# print(array[1])
# array2 = np.array(
#     [[1,2,3],
#      [4,5,6],
#      [7,8,9]
#     ]
# )
# print(array2[1,0]) #打印第一行第0列
# print(array2[1,2])
array = np.array([2,3,4,5,6])   #定义一维数组array
print(array[0:3])
array2 = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]
    ]
)
print(array2[1:2,1:2])