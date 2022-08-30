hashmap apis:
``

    my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
    my_dict.keys()
    my_dict.values()
    my_dict.get('Dave')
    for x,y in my_dict.items():
        print(x, ":" , y)       #prints keys and values
``

## Binary Search
#### 特点：search space，input 通常是sorted的
#### 需要注意的点 
  - 退出while循环的条件：
    - left < right: 剩下两个元素进入循环, 剩一个出循环
    - left < right - 1， 剩下三个元素可以进入循环，两个则跳出，left neighbours right，通常情况下target有可能不在input中
      - left 和 right 移动时不一定是要去掉中位数 i.e left = mid; right = mid;
    - left <= right 剩下一个元素可以进入循环, 0个出循环 (没有找到合适的元素)
  - 是否需要post-processing，如果需要，退出while loop时候剩下多少数

#### Principles of Binary Search:
  - the search space should be decreased after each iteration
  - target (if exist) cannot be ruled out accidentally when we move the value of left or right (保证探索的区间一定有target)

#### 如何检验算法的正确性：
- 先代入 null、 0个、 1个、 2个，查看边界和结果的正确性
- 判断左右移动的时候，严格按照principles的检查

## Sorting with Areas
- 一点规律：一般unexplored area都是闭区间
- 给定数字的area，一般是半开半闭区间，开的部分需要留给即将探索的地方

## Sliding Window
- https://leetcode.com/tag/sliding-window/
- 特点：要求找到满足条件的最长/最短的子数组、多个sub elements、子字符串
  - 满足xxx条件：计算结果、出现次数、同时包含、最接近
  - 最长、最短 
  - 子串、子数组、子序列： 重要： 结果连续！！！
- 核心思路（最长）：
  - 左右双指针（L、R）在起始点，R向右逐位滑动循环
  - 每次滑动的过程中
    - 如果窗内元素满足条件，R向右扩大窗口，并更新最优解
    - 如果窗内元素不满足条件，L向右缩小窗口
  - R到达结尾
- 最长模板
```
初始化left, right, result, bestResult 
while (右指针没有到达结尾) {
    窗口扩大，加入right对应元素，更新当前result
    if (result不满足要求) {
        窗口缩小，移除left对应元素，left右移
    }
    更新最优结果bestResult
    right++;
}
return bestResult;

```
- 最短模板
- https://leetcode.com/problems/minimum-size-subarray-sum/
```
初始化 left, right, result, bestResult
while (右指针没有到达结尾) {
    窗口扩大，加入right对应元素，更新当前result
    if (result满足要求) {
        更新最优结果bestResult
        窗口缩小，移除left对应元素，left 右移
    }
    right++;
}
return bestResult;
```

## LinkedList
#### Key Points:
- when you want to dereference a ListNode, make sure it's not None/Null
- never lose the control of the head pointer of the linked list
#### 一些需要注意的点：
- 用快慢指针遍历linked list的时候，需要注意termination condition
  - (fast.next != null && fast.next.next != null) vs (fast != null && fast.next != null)
    - (fast.next != null && fast.next.next != null) : 当 list 的node为偶数时候返回中间两个nodes的前一个
    - (fast != null && fast.next != null)： 当 list 的node为偶数的时候返回中间两个nodes的后一个
- online algorithm vs offline algorithm
  - online algorithm: 过程中不断输出部分处理完毕的数据
  - offline algorithm: 全部运行完才能知道结果
- Dummy Head的使用
  - head node会在解题时改变、当linked list需要被修改时
    - when we want to append new element to an initially empty linked list, we do not have an initial head node.
  - 需要判断多种conner case中哪个node是head node
- Linked list常见的陷阱：
  - 需要判断操作在头尾节点上code是否能处理：头尾节点的取值、是否为空