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
## DFS and BFS
