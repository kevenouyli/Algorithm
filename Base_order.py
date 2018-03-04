#冒泡排序
print("冒泡排序：将最大的数循环往右边冒泡")
list = [3,1,5,7,8,63,21,40,4,9]
print(list)
#函数
def bubble(list):
    high = len(list)-1      #定一个最高位
    for j in range(high,0,-1):
        print(j,list)
        exchange = False    #交换的标志，如果提前排好序可在完整遍历前结束
        for i in range(0,j):
            if list[i]>list[i+1]:   #如果比下一位大
                list[i],list[i+1] = list[i+1],list[i]   #交换位置
                exchange = True #设置交换标志
        if exchange == False:
            return list     # return list #返回列表
#打印
print(bubble(list))

#选择排序
print("选择排序：在往右缩小range的同时，选取range数列中最小的值与当前数交换位置")
list = [3, 1, 5, 7, 8, 6, 2, 40, 43, 98]
print(list)
#函数
def choice(list):
    for i in range(0,len(list)-1):
        print(i,list)
        min_loc = i
        for j in range(i+1,len(list)-1):
            if list[min_loc]>list[j]:   #最小值遍历比较
                min_loc = j
        list[i],list[min_loc] = list[min_loc],list[i]
    return list
#打印
print(choice(list))

#插入排序
print("插入排序：从左往右，发现数值小的就")
list = [3,1,50,7,8,6,2,0,10]
print(list)
#函数
def cut(list):
    for i in range(1,len(list)):
        print(i,list)
        temp = list[i]
        for j in range(i-1,-1,-1):  #从有序区最大值开始遍历
            if list[j]>temp:    #如果待插入值小于有序区的值
                list[j+1] = list[j] #向后挪一位
                list[j] = temp  #将temp放进去
    return list
#打印
print(cut(list))

##以上这三种排序方式时间复杂度都是O(n^2)，不太高效，所以下面介绍几种更高效的排序方式

#快速排序，步骤为  1、提取   2、 左右分开   3、 递归调用    ，快排的时间复杂度最佳情况是O(nlogn)，最差情况是O(n^2)
print("快速排序：")
List = [9,14,16,63,5,41,13,45,1,2]
print(List)
count=0
def QuickSort(myList,start,end):
    global count
    count+=1
    print(myList,'\t',count)
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]
        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):                   #从右往左找到第一个小于base的数
                j = j - 1
            myList[i] = myList[j]
            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):                   #从左往右找到第一个大于base的数
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        print(myList,'base:',base,'start:',start,'i:',i,'j:',j)
        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

QuickSort(List,0,len(List)-1)
print(List)


'''     堆排序：
        1、建立堆
        2、得到堆顶元素，为最值
        3、去掉堆顶，将最后一个元素放到堆顶，进行再一次堆排序（迭代）
        4、第二次的堆顶为第二最值
        5、重复3，4直到堆为空
        具体图解可参考：https://www.cnblogs.com/chengxiao/p/6129630.html
'''
print("堆排序：")
list = [3, 1, 5, 7, 8, 6, 2, 30, 44, 9,77]
print(list)

def sift(low, high, list):#low为父节点，high为最后的节点编号
    i = low
    j = 2 * i + 1       #子节点位置
    temp = list[i]      #存放临时变量
    while j <= high:    #遍历子节点到最后一个
        if j < high and list[j] < list[j + 1]:#如果第二子节点大于第一子节点
            j += 1
        if temp < list[j]:      #如果父节点小于子节点的值
            list[i] = list[j]   #父子交换位置
            i = j               #进行下一次编号
            j = 2 * i + 1
        else:
            break       #遍历完毕退出
    list[i] = temp      #归还临时变量

def heap_sort(list):
    n = len(list)
    for i in range(n // 2 - 1, -1, -1): #从最后一个父节点开始
        sift(i, n-1, list)#完成堆排序

    print(list)

    for i in range(n - 1, -1, -1):#开始排出数据
        list[0], list[i] = list[i], list[0]#首尾交换
        sift(0, i - 1, list)    #进行新一轮堆排序
    return list

print(heap_sort(list))


'''
归并排序： 递归将两个子列表合成为一个有序的列表
         图解参考： https://www.cnblogs.com/chengxiao/p/6194356.html            
'''
print("归并排序1：")
list=[5,7,2,5,9,12,56,43,2,4,56,7,89,90]
print(list)

def merg(low,high,mid,list):
    i = low
    j = mid +1
    list_temp = []      #定义临时列表
    while i <=mid and j <=high:
        if list[i]<=list[j]:        #分别比较有序子列表元素的大小
            list_temp.append(list[i])   #添加进临时列表中
            i +=1
        else:
            list_temp.append(list[j])
            j +=1
    while i <= mid:
        list_temp.append(list[i])
        i +=1
    while j <= high:
        list_temp.append(list[j])
        j +=1
    list[low:high+1]=list_temp  #将已完成排序的列表赋值给原列表相应位置

def merge_sort(low,high,list):
    if low < high:
        mid = (low+high)//2 #二分法
        merge_sort(low,mid,list)
        merge_sort(mid+1,high,list)#递归调用，
        merg(low,high,mid,list)
    return list

print(merge_sort(0,len(list)-1,list))

#归并排序Version2：
print("归并排序2：")
list=[5,88,22,51,9,12,56,43,27,4,56,7,89,90]
print(list)

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2)
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)

def Merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result

print(MergeSort(list))