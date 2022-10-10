## Hash Table

- 一些特殊情况需要考虑: int[] array: array.length == 0 or array == null or target numbers = 0

- Python Implmentation for pq:

  ```python
  class Pair:
      def __init__(self, word, freq):
          self.word = word
          self.freq = freq
  
      #这里其实可以通过define__lt__来实现minheap的implementation
      def __lt__(self, p):
          # if the alphabetic oreder: self.word > p.word, then it has less ordering number for minheap
          return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)
  
   cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
  # cnt可以得到一个dict with key as word, value as freq
  
  ```

#### Q1 Find the common numbers between two sorted arrays, a[M], B[N]

- 重要！！！需要 clarify：
  - 是 ascending sorted 还是 descending sorted
  - 是否有 duplicated element
  - how large are M and N
- 几种方法：
  1. binary search: 把每个 a[M]的元素设为目标，在 B[N]中执行 binary search
     1. Time Complexity: O(n log m) if m > n or O(m log n) if n > m
  2. two pointer: 用两个 pointer 分别指向 a[M]与 B[N]的元素，比较 i 和 j 指向的元素，谁小移动谁，直到找到相等的元素
     1. Time Complexity: O(m + n)
  3. hash set: 过一遍 a[M]将每个元素 push 进 set 中，再过一遍 b[N], 检查 b[N]的每一个元素是否在 a[M]中
     1. Time complexity:
        1. insetion for hash set: O(m) in avarage if no collision, O(m^2) if collision for worse case
        2. find element in b[N]: O(n) in average, O(m \* n) if collision for worse case

## String I

逻辑层面的数据结构：an array of characters (in ascii code)

#### 五类常考的问题（和 array 的有些问题相似，往往需要用 2 个 pointer 来完成操作）：

1. Char Removal

   1. remove some particular chars from a string
   2. remove all leading/trailing/duplicated empty spaces from a string

2. De-duplication: aaaabbbccc => abc

3. Substring

   1. regular method
   2. Robin-Carp & KMP

4. reversal (Swap): e.g i love yahoo => yahoo love i

5. replace empty space: " " with "%20"

#### 常见错误

- 在用 for 循环删除 char array 之中的 element 时，剩下的 elements 会左移，需要注意 index。
- 不能盲目调用 string api，在不知道 api 的复杂度

#### Char Removal, depulication: 常见 technique: fast and slow pointers

- fast pointer 用于 traverse 整个 array，每一次 while loop, increase one
- slow pointer 用于 track 需要保留的 index
- fast 和 slow 的物理意义：
  - j = 0 (fast) the letter being processed. in other words, all letters to the left side of j (not including j) are processed letters
  - i = 0 (slow) all the letters to the left-side of i (not including i) are all processed letters that should be kept
  - all letters in [i, j - 1] are all area that we don't care
  - [j, size - 1] unknow area to explore
- 如果要找到 the latest element that we visited, use stack

#### Find Substring

- 基本方法：

```python
# 注意 index i 用于iterate large str， 范围是i <= len(large) - len(small)
# j 用于iterate small str
for i in range (0, len(large) - len(small) + 1):
  j = 0
  while j < len(small) and large[i + j] == small[j]:
    j += 1
    if j == len(small):
    return i
```

#### String Reversal

