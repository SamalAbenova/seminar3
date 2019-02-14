from linked_list import MyList, ListNode

class MySet:
    def __init__(self):
        self.items = MyList()

    def length(self):
        return self.items.__len__()

    def contains(self, item):
        return self.items.__contains__(item)

    def isEmpty(self):
        return self.items.__len__() == 0

    def add(self, item):
        i = ListNode(item)
        self.items.add(i)

    def remove(self, item):
        i = ListNode(item)
        return self.items.remove(i)

    def equals(self, setB):                 
        if self.length() != setB.length() :
            return False
        else:
            return self.isSubsetOf( setB ) 

    def isSubsetOf(self, setB):           
        for element in self :
            if element not in setB:
                return False
        return True 

    def union( self, setB ):                 
        newSet = MySet()  
        for element in self.items:
            newSet.add(element)
        for element in setB :
            if element not in self :
                newSet.add(element)
        return newSet 

    def difference(self, setB):
        newSet = MySet()
        for element in self.items:
            newSet.add(element)
        for element in setB:
            if element in self :
                newSet.remove(element)
        return newSet


    def print_set(self):
        for i in self.items:
            print(i, end=', ')


    def __iter__( self ):
        return self.items.__iter__()