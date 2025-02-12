# from textbook

class Progression:

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for value in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        temp = self._prev
        self._prev = self._current
        self._current = temp + self._prev


r = float(input("Enter an r value between -1 and 1, excluding 0"))
start_value = float(input("Enter a starting value"))
expected_sum = start_value / ( 1 - r )

progression = GeometricProgression(r, start_value)

current_sum = 0
for value in progression:
    current_sum += value
    print(current_sum)
    if abs( current_sum - expected_sum ) <= .000001:
        break