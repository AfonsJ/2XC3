import random
import bst
import lab6

#Using create random list function from sorting lab
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


hbst = []
hrbt = []
diffl = []

for i in range(1,1001):
    l = create_random_list(10000, 20000)
    bstree = bst.BSTTree()
    rbt = lab6.RBTree()

    for i in l:
        bstree.insert(i)
        rbt.insert(i)

    hbst.append(bstree.get_height())
    hrbt.append(rbt.get_height())


for i in range(0, len(hbst)):
    diff = hbst[i] - hrbt[i]
    diffl.append(diff)

def avg(l):
    return sum(l) / len(l)

print("Average height of BST")
print(avg(hbst))
print("Average height of RBT")
print(avg(hrbt))
print("Average height difference between BST and RBT (height of BST - height of RBT)")
print(avg(diffl))