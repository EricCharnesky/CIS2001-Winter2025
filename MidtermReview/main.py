import math
from multiprocessing.managers import Value


def _reverse(some_list, start_index, back_index):
    if start_index >= back_index:
        return some_list
    temp = some_list[start_index]
    some_list[start_index] = some_list[back_index]
    some_list[back_index] = temp
    return _reverse(some_list, start_index +1, back_index-1)

def reverse(some_list):
    return _reverse(some_list, 0, len(some_list)-1)

# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_of_prime_values_or_prime_indexes(some_2d_list):
    total = 0
    current_index = 0
    for row_index in range(len(some_2d_list)):
        for column_index in range(len(some_2d_list[row_index])):
            if is_prime(some_2d_list[row_index][column_index]) or is_prime(current_index):
                total += some_2d_list[row_index][column_index]
            current_index += 1
    return total

some_2d_list = [
    [1,2,3,4],
    [5,6,7,8],
    [2,5,7,9]
]

print(sum_of_prime_values_or_prime_indexes(some_2d_list))


def _recursive_jumble(original_string, jumbled_string, start_index, end_index):
    if start_index == end_index:
        return jumbled_string + original_string[start_index]
    elif start_index > end_index:
        return jumbled_string
    return _recursive_jumble(original_string, jumbled_string + original_string[start_index] + original_string[end_index], start_index+1, end_index-1)

def recursive_jumble(some_string):
    return _recursive_jumble(some_string, "",0, len(some_string)-1)



def jumble(some_string):
    jumbled_string = ""
    start_index = 0
    end_index = len(some_string)-1
    while start_index < end_index:
        jumbled_string += some_string[start_index] + some_string[end_index]
        start_index += 1
        end_index -= 1
    if start_index == end_index:
        jumbled_string += some_string[start_index]
    return jumbled_string

print(recursive_jumble("ABCDEFGH"))
#AHBGCFDE

print(jumble("ABCDEFGH"))



class Burger:

    def __init__(self, base_cost, base_weight_in_grams, cost_in_cents_per_gram):
        self._actual_weight_in_grams = 0
        self._cost_in_cents_per_gram = cost_in_cents_per_gram
        self.toppings = []
        self._base_cost = base_cost
        self._base_weight_in_grams = base_weight_in_grams

    def add_topping(self, topping):
        self.toppings.append(topping)

    def get_total_cost(self):
        cost = self._base_cost
        if self._actual_weight_in_grams > self._base_weight_in_grams:
            cost += (self._actual_weight_in_grams - self._base_weight_in_grams) \
                * ( self._cost_in_cents_per_gram / 100 )
        return cost

    def set_actual_weight_in_grams(self, weight_in_grams):
        if weight_in_grams < 0 or weight_in_grams > 1000:
            raise ValueError
        self._actual_weight_in_grams = weight_in_grams

    def get_weight_in_grams(self):
        return self._actual_weight_in_grams

