from singly_linked_list import SinglyLinkedList
from double_linked_list import DoublyLinkedList

single_linked_list = SinglyLinkedList()

for number in range(10):
    single_linked_list.append(number)

while not single_linked_list.is_empty():
    print(single_linked_list.remove_front())

double_linked_list = DoublyLinkedList()

for number in range(10):
    double_linked_list.add_back(number)

while not double_linked_list.is_empty():
    print(double_linked_list.remove_back())

