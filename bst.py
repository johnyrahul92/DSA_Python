class BinaryTree:

    def __init__(self, key) -> None:
        self.key=key
        self.left=None
        self.right=None


node0=BinaryTree(4)
node1=BinaryTree(5)
node2=BinaryTree(6)

tree = node0
tree.left=node1
tree.right=node2

def parse_tuple(data):

    if isinstance(data,tuple) and len(data)==3:
        node=BinaryTree(data[1])
        node.left= parse_tuple(data[0])
        node.right= parse_tuple(data[2])
    elif data==None:
        node=None
    else:
        node = BinaryTree(data)
    return node


test_tuple=(1,2,(3,5,None))
tree=parse_tuple(test_tuple)

def parse_tree_to_tuple(tree: BinaryTree):
    if tree.key:


    pass

print(tree)