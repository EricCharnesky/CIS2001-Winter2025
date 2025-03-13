from collections import deque
from n_tree import Tree

import random

from priority_queue import MaxPriorityQueueList

max_queue = MaxPriorityQueueList()

for _ in range(100):
    max_queue.add(random.randint(1, 1000))

while len(max_queue):
    print(max_queue.remove())



classification_system = Tree('Animalia')
classification_system.add_child('Chordata')
chordata = classification_system.children[0]

chordata.add_child("Mammalia")

mammalia = chordata.children[0]

mammalia.add_child('Diprotodontia')
mammalia.add_child('Primates')

diprotodontia = mammalia.children[0]
primates = mammalia.children[1]

diprotodontia.add_child('Quokka')
primates.add_child('Lemur')

classification_system.print_tree_breadth_first()





