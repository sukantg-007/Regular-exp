class abc:
    def __init__(self,list):
        self.list = list
    def __sub__(self,other):
        return [x for x in self.list if x not in other.list]

list1 = ["1","2","3"]
list2 = ["1"]
a1 = abc(list1)
a2 = abc(list2)
print(a1 - a2)