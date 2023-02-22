# Given a binary tree, 
# connect the nodes that are at the same level. 
# The structure of the tree Node contains an addition nextRight pointer for this purpose.
# Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.
def connect(self, root):
        # code here
  q = [root]
  while q:
      temp=[]
      for _ in range(len(q)):
          node = q.pop(0)

          if len(q)>0:
              node.nextRight = q[0]
          if node.left:
              temp.append(node.left)
          if node.right:
              temp.append(node.right)
      q+=temp
      return root
