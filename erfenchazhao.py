import time
import random
def cal_time(func): #装饰器
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("running time:",func.__name__, t2 - t1)
        return result
    return wrapper

@cal_time
def bin_search(data_set,val):
    #low 和high代表下标 最小下标，最大下标
    low=0
    high=len(data_set)-1
    while low <=high:# 只有当low小于High的时候证明中间有数
        mid=(low+high)//2
        if data_set[mid]==val:
            return mid  #返回他的下标
        elif data_set[mid]>val:
            high=mid-1
        else:
            low=mid+1
    return  # return null证明没有找到
data_set = list(range(100))
# random.shuffle(data_set)
print(data_set)
print(bin_search(data_set,6))