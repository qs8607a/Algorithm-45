# Introduction to Algorithm - Chapter 12: Binary Search Trees
# BINARY-TREE

class BTreeNode:
    def __init__(self, value=None, parent = None, left=None, right=None): 
        self.value = value;
        self.parent = parent;
        self.left = left;
        self.right = right;

def printBTree(node, level):
    if node != None:
        printBTree(node.right, level + 1);
        print "\t" * level + str(node.value);
        printBTree(node.left, level + 1);

class BTree:
    def __init__(self, root):
        self.root = root;

    def __repr__(self):
        # printBTree(self.root, 0);
        pass;

def treeSearch(root, value):
    node = root;
    while node != None and value != node.value:
        if value < node.value:
            node = node.left;
        else:
            node = node.right;
    return node;

def treeMin(root):
    node = root;
    while node.left != None:
        node = node.left;
    return node;

def treeMax(root):
    node = root;
    while node.right != None:
        node = node.right;
    return node;

def treeSuccessor(node):
    if node.right != None:
        return treeMin(node);
    tmpParent = node.parent;
    tmpNode = node;
    while tmpParent != None and tmpNode == tmpParent.right:
        tmpNode = tmpParent;
        tmpParent = tmpParent.parent;
    return tmpParent;

def treeInsert(tree, value):
    node = BTreeNode(value, None, None, None);
    resParent = None;
    tmp = tree.root;
    while tmp != None:
        resParent = tmp;
        if value < tmp.value:
            tmp = tmp.left;
        else:
            tmp = tmp.right;
    node.parent = resParent;
    if resParent == None:
        tree.root = node;
    elif value < resParent.value:
        resParent.left = node;
    else:
        resParent.right = node;

def transplant(tree, u, v):
    if u.parent == None:
        tree.root = v;
    elif u == u.parent.left:
        u.parent.left = v;
    else:
        u.parent.right = v;
    if v != None:
        v.parent = u.parent;


def treeDelete(tree, node):
    if node.left == None:
        transplant(tree, node, node.right);
    elif node.right == None:
        transplant(tree, node, node.left);
    else:
        m = treeMin(node.right);
        if m.parent != node:
            transplant(tree, node, node.right);
            m.right = node.right;
            m.right.parent = m;
        transplant(tree, node, m);
        m.left = node.left;
        m.left.parent = m;


