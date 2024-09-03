import random
class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1)

class SkipList:
    def __init__(self, max_lvl, P):
        self.MAXLVL = max_lvl
        self.P = P
        self.header = self.createNode(self.MAXLVL, -1)
        self.level = 0

    def createNode(self, lvl, key):
        n = Node(key, lvl)
        return n

    def randomLevel(self):
        lvl = 0
        while random.random()<self.P and lvl<self.MAXLVL:lvl += 1
        return lvl

    def insertElement(self, key):
        update = [None]*(self.MAXLVL+1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current == None or current.key != key:
            rlevel = self.randomLevel()

            if rlevel > self.level:
                for i in range(self.level+1, rlevel+1):
                    update[i] = self.header
                self.level = rlevel

            n = self.createNode(rlevel, key)

            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n
    
    def append(self, lst):
        current = lst.header.forward[0]
        while current:
            self.insertElement(current.key)
            current = current.forward[0]
        lst.header = lst.createNode(lst.MAXLVL, -1)
        lst.level = 0


    def displayList(self):
        print("\nSkip List -> ")
        head = self.header
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")

lst = SkipList(3, 0.5)
lst.insertElement('a')
lst.insertElement('b')
lst.insertElement('c')

lst2 = SkipList(3,0.5)
lst2.insertElement('d')
lst2.insertElement('e')
lst2.insertElement('f')
lst.displayList()
lst2.displayList()
lst.append(lst2)
lst.displayList()
lst2.displayList()
