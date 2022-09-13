## Deque, Stack, Queue in Python


## Binary Tree
#### Trick: base case usually refers to the null ChildNode below the leaf node
- Recursion should be combined with binary trees
- why? 因为每层的node具备的性质，传递的值与下一层的性质一致（用于定于recursive rule）
- Complexity = length of tree from root node to leaf node * number of leaf nodes

#### BST 常见题型
- 把value  从上往下 传递然后再 从下往上
  - BST判定
- 只把value从下往上传递
  - getHeight
  - isBalanced
  - isSymmetric
  - assign the value of each node to be the otal number of nodes that belong to its left subtree
## Heap/Priority Queue

#### Insights:

- min heap: the top of heap is the minimal of the heap, and every subtree root is the minimal of that subtree
- 堆序性：不管任何操作，heap总是能够维持自己是最大堆/最小堆的性质
- parent = (child - 1)/ 2
- Leftchild = parent * 2 + 1
- rightchild = parent * 2 + 2

#### Python Implementation

https://docs.python.org/3/library/heapq.html

```python
import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!
heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap
```

#### Java Implementation 

https://docs.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html

Time Complexity of heap api:

- offer(E e): O(log n)
- peek(): O(1)
- poll(): O(logn)
- remove():O(logn), from AbstractQueue, remove(Object) - O(n)
  - remove(): remove the most prior element O(logn)
  - remove(Object): first need to find its position, O(n)
- size(): O(1)
- isEmpty(): O(1)

```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // 默认是min heap

// 定义PriorityQueue去比较objects
// method 1: Comparable interface 
// case 1：在utils的Object中实现Comparable Interface
interface Comparable<E> {
  int compareTo(E ele);
}

// part of Integer class implementation
class Integer implements Comparable<Integer> {
  private int value;
  public Integer(int value) {
    this.value = value;
  }
  
  @Override
  public int compareTo(Integer another) {
    if (this.value == another.value) {
      return 0;
    }
    return this.value < another.value ? -1 : 1;
    // 0 - this and another are of the same priority
    // -1 (<0) - this has higher priority than another
    // 1 (>0) this has less priority than another
    
    // CompareTo的return value(int)代表什么含义(this.compareTo(other))：
    // 0: this和other的优先级相同（大小一样）
    // -1: this优先于other，因为this小
    // 1: other优先于this，因为this大
  }
}

// declaration
PriorityQueue<Integer> pq = new PriorityQueue<>();

// method 2: Comparator
interface Comparator<E> {
  int compare(E o1, E o2);
}

class MyInteger {
  private int value;
  public MyInteger(int value) {
    this.value = value;
  }
}

class MyComparator implements Comparator<MyInteger> {
  @Override
  public int compare(MyInteger o1, MyInteger o2) {
    if (o1.value == o2.value) {
      return 0;
    }
    
    return c2.value < c1.value ? -1 : 1;
    // compare(o1, o2)的return value代表什么含义：
    // 0: o1和o2的优先级相同
    // -1: o1大于o2，因为o1小，所以o1优先
    // 1: o1大于o2，因为o2小，所以o2优先
  }
}

// declaration
PriorityQueue<MyInteger> pq = new PriorityQueue<>(size_of_heap, new Comparator());
```

- Collections.reverseOrder(): return a comparator that reverses the natural order

```java
PriorityQueue<MyInteger> maxHeap = new PriorityQueue<MyInteger>(Collections.reverseOrder());
```

##### 注意：the initial capacity of heap has to be > 0: be careful for the conner case

- Heapify a collection

```java
ArrayList<Cell> list = new ArrayList<>();
PriorityQueue<Cell> heap = new PriorityQueue<Cell>(list);
// 这是使用了Constructor PriorityQueue(Collection<? extends E > c)，因为它的实现内部有Heapify()
// 坑点，我们没有办法再传进Comparator的同时也用O(n)的heapify。所以如果想要自己定义Comparator，只能传进Comparator再一个个维持堆序性O(nlogn) 
```

#### Q1 Smallest k elements from an unsorted array of size n

- idea: use Max-heap, 不断地比较array里的值，如果新的元素比当前heap中最大的值小，则更新heap，从而优化max-heap中的元素。

类似的题目：https://leetcode.com/problems/kth-largest-element-in-an-array/

## BFS

https://www.youtube.com/watch?v=pV2kpPD66nE Number of Islands

#### Insights: 

- Data Structure: Queue
- Steps:
  - 1.initial state (start node)
  - 2.expand:for each node, exapnd parent node, eg. Visit, print its value
  - 3.generat:generate its child nodes, reach out to its neghbouring nodes
  - Termination condition: do a loop until the queue is empty

- When should we consider to use BFS1 to sovle a class of questions?

  - ##### Tree-related problem and in the meantime we need to address the relationship to the same level 同一张图的neighor的关系、或是同一棵树里同层亲戚关系。大多数问题中，同层关系需要flag或者map去indicate是否visit过一个node

  - 另一个规律：在generate neighours时，可以检查是否符合题目的要求

#### Question 1: Determine wether a binary tree is complete binary tree

- Key idea:
  - flag: 用一个boolean值indicate是否遇到null
  - 当generate一个element, 
    - case 1: 是否遇到null = false, 左孩子是null，右孩子不是 => return false
    - Case 2: 是否遇到null = false, 左孩子!= null, 右孩子 = null, set 是否遇到null = true
    - case 3：是否遇到null=true，element != null, return false 

#### Question 2: Bipartite

- Key idea:

  - 对每一个图的arraylist里的node进行bfs

  - Flag: 表示不同组的颜色: 0 or 1

  - HashMap<GraphNode, Integer> visited: 表示每一个node的颜色

  - initial state: 

    ```java
    queue.offer(node);
    // 注意：需要给第一次访问的node确定group
    visited.put(node, 0);
    ```

  - Expand: traverse图里的每一个node，expand 每一个queue里内容
  - generate：check一个node的neighor是否被generated过，如果否，则将它放入visited和queue中；如果是，检查它的颜色是否正确

#### Dijstra' Algorithm

##### Insight:

- Usage: find  <mark> **the shorest path cost ** </mark> from a single node (source node) to any other nodes in that graph (一个点到所有点的最短距离算法)
- Data Structure: PriorityQueue(MinHeap)
- 解题思路
  1. initial state(start node)
  2. node expansion/genration rule:
     1. when to expand a parent node
     2. when to generate child nodes (to queue)
  3. termination condition
- Properities of Dijsktra's algorithm:
  1. one node can be expanded once and only once
  2. **one node can be generated more than once (cost can be reduced over time) **
  3.  <mark>  *** all the cost of the nodes that are expanded are monotinically non-decreasing **  </mark> 所有从priority queue里面pop出来的元素的值都是单调非递减的 -> 单调递增
  4. time complexity: for a graph with n node the connectivity of the node is constant O(n log n). for a genral graph O(E log V)
  5. <mark>**when a node is popped out for expansion, its value is fixed which is equal to the shortest distance from the start node. ** </mark>

## Discussion of BFS and Dijstra

- General algorithm:
  1. initial state: root node, start node, min num
  2. expansion/genration rule:
     1. bfs: expand node, generate all neighbors => FIFO queue
     2. dijstra: expand node, generate all neighbors => PQ
  3. termination conditions:
     1. queue is empty
     2. when conflict is found
     3. when the target node is expanded
     4. when the k-th element is expanded
  4. **Deplication** 
- When should we consider BFS?
  - Tree-related problem and in the meantime we need to address the relationship to the same level 同一张图的neighor的关系、或是同一棵树里同层亲戚关系。大多数问题中，同层关系需要flag或者map去indicate是否visit过一个node
- When should we consider Dijstra
  - shortest path in a weighted graph 
  - K-th smallest/largest

## DFS

- 为什么permutation的问题不能用bfs而是要用dfs？
  - 如果输入input的size特别大，bfs每一层的queue的size都是exponentially grow的，很容易造成stack overflow。所以permutation则使用dfs

#### Time Complexity of Recursion:

- branch^level * 每个node需要的时间

#### DFS的基本方法

1. How many levels in the recursion tree? what does it store on each level? 每层代表什么意义？一般来讲解体之前就知道DFS要递归多少层
2. How many different states should we try to put on each level? 每层有多少个状态/case 需要try？

- 重要结论： <mark>**Number of add = number of delection 去其它分支之前一定要还原成原始状态**</mark>

#### Discussion

1. subset => 结果中每个元素的顺序无关，每一层的分支数是常数
2. () => 结果中每个元素的顺序有关，每一层的分支数仍旧是constant, 但是根据condition cut branches
   1. cutting branch可能需要每一层传递数值记录状态来判断
3. 99 cents => 考虑同一面值可以拿的数量 分支 => combination question => ways of selecting elements
4. permutation => 结果中每个元素的顺序有关 ways of ordering items => swap-swap 
   - whenever every single permutation contains all elements in the initial input and their only differnce is their order, you should consider swap-swap 
   - 如果每一层有多个不同的state，则用loop解决

## Hash Table and String I

#### Q1 Find the common numbers between two sorted arrays, a[M], B[N]

- 重要！！！需要clarify：

  - 是ascending sorted还是descending sorted
  - 是否有duplicated element
  - how large are M and N

  
