#LAB4.23
class Node:
  def __init__(self,val,leftNote = None, rightNode = None):
    self.label = val
    self.left = leftNote
    self.right = rightNode
  def isLeaf(self):
      return self.left == None and self.right == None
  def __str__(self):
      if self.isLeaf():
        return "Node({})".format(self.label)
      else:
        return "Node({},{},{})".format(self.label, str(self.left), str(self.right))

  def linearize(self): # Recursive method that return a list of the tree branchs
    if self.isLeaf():
      return [[self]]
    else:
      if self.left != None:
        L1 = self.left.linearize() #recursive processing of the left child node
      else:
        L1 = []
      if self.right != None:
        L2 = self.right.linearize()
      else:
        L2 = []
    return [[self] + e for e in L1] + [[self] + e for e in L2]

#LAB4.26

  def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
      return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods

# Contributed By Harshit Agrawal