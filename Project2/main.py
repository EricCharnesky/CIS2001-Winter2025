from dock import Dock

items_per_train = [ 2, 7, 1]
items_per_plane = [ 3, 2 ]
train_items = [ 2, 2, 2, 1, 3, 2, 2, 2, 1, 2]
plane_items = [ 2, 1, 1, 2, 1 ]

dock = Dock(items_per_train, items_per_plane, train_items, plane_items)
dock.load_trains()
dock.load_planes()

print(dock)