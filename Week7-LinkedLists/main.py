from singly_linked_list import SinglyLinkedList
from double_linked_list import DoublyLinkedList
from positional_doubly_linked_list import PositionalCircularDoublyLinkedList


positional_list = PositionalCircularDoublyLinkedList()

positional_list.add_first("Eric")

current_position = positional_list.first()

positional_list.add_after(current_position, "Jeb")
positional_list.add_before(current_position, "Adam")

current_position = positional_list.before(current_position)



name = input("Enter a name to add to the list")

while name != 'QUIT':

    current_position = positional_list.first()

    last_position = positional_list.last()

    if name > last_position.data():
        positional_list.add_last(name)
    else:
        while name > current_position.data():
            current_position = positional_list.after(current_position)
        positional_list.add_before(current_position, name)

    name = input("Enter a name to add to the list or QUIT")

for name in positional_list:
    print(name)





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

