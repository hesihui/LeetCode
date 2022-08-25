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
  
#### Sliding Window
