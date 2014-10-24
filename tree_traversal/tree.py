from ete2 import Tree
#t = Tree()
#t = Tree( "(E(A,B).F(C,D));" )
#t.populate(15)
#t = Tree("(1(3,5),4(2));")
#t = Tree('((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C);', format=1)
#t = Tree("(((4,5)2,3)1);") # Creates an empty tree
t= Tree()
#R = t.add_child(name = "1")
t.name = "1"
A = t.add_child(name="2") # Adds a new child to the current tree root
                           # and returns it
B = t.add_child(name="3") # Adds a second child to the current tree
                           # root and returns it
C = A.add_child(name="5") # Adds a new child to one of the branches
D = A.add_child(name="4") # Adds a second child to same branch as
                             # before, but using a sister as the starting
                             # point
#R = A.add_child(name="R")

print t.get_descendants()
print t.get_ascii(show_internal=True)
#node = t.search_nodes(name="1")
#for n in node:
#print t.get_descendants()
#	print n.get_descendants(),n
