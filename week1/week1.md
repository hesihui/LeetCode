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

## Sorting
