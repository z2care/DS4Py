'''
Created on 2014.9.8

@author: zarey
'''

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, newNode):
        if self.leftChild:
            tmp = BinaryTree(newNode)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp
        else:
            new = BinaryTree(newNode)
            self.leftChild = new

    def insertRight(self, newNode):
        if self.rightChild:
            tmp = BinaryTree(newNode)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp
        else:
            new = BinaryTree(newNode)
            self.rightChild = new

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

    def preOrder(self):
        print self.key
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

    def inOrder(self):
        if self.leftChild:
            self.leftChild.preOrder()
        print self.key
        if self.rightChild:
            self.rightChild.preOrder()

    def postOrder(self):
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()
        print self.key

if __name__ == "__main__":
    root = BinaryTree('1')
    root.insertLeft('2')
    root.insertRight('3')
    root.preOrder()
    root.postOrder()
    root.inOrder()
        