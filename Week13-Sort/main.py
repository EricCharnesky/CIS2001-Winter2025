# always O(n^2)
def selection_sort(some_list):

    for index in range(len(some_list) - 1):
        smallest_index = index
        for index_to_check in range(index+1, len(some_list)):
            if some_list[index_to_check] < some_list[smallest_index]:
                smallest_index = index_to_check
        temp = some_list[index]
        some_list[index] = some_list[smallest_index]
        some_list[smallest_index] = temp

# best case O(n)
# average O(n^2)
# worst O(n^2)
def insertion_sort(some_list):
    for index in range(1, len(some_list)):
        for current_index in range(index, 0, -1):
            if some_list[current_index] < some_list[current_index-1]:
                temp = some_list[current_index]
                some_list[current_index] = some_list[current_index-1]
                some_list[current_index - 1] = temp
            else:
                break


some_list = [ 7, 8, 3, 22, 15]
insertion_sort(some_list)
print(some_list)