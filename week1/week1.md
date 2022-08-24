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
- 需要注意的点 
  - 退出while循环的条件：mid_index
  - 是否需要post-processing，如果需要，退出while loop时候剩下多少数