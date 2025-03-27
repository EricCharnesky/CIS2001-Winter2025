class Polynomial:

    class TermNode:

        def __init__(self, coefficient, exponent, next = None):
            self.coefficient = coefficient
            self.exponent = exponent
            self.next = next

        def __eq__(self, other):
            return self.coefficient == other.coefficient and self.exponent == other.exponent

        def __ne__(self, other):
            return not self == other

    def __init__(self, coefficient, exponent):
        self._first_term = self.TermNode(coefficient, exponent)

    def _add_term_to_end(self, term):
        current_term = self._first_term

        while current_term.next is not None:
            current_term = current_term.next

        current_term.next = term

    def __add__(self, other):

        result_polynomial = Polynomial(0, 0)
        current_self_term = self._first_term
        current_other_term = other._first_term

        # add largest term or combine coefficients
        while current_self_term and current_other_term:
            if current_self_term.exponent == current_other_term.exponent:
                result_polynomial._add_term_to_end(
                    self.TermNode(
                        current_self_term.coefficient + current_other_term.coefficient,
                        current_self_term.exponent))
                current_self_term = current_other_term.next
                current_other_term = current_other_term.next
            elif current_self_term.exponent > current_other_term.exponent:
                result_polynomial._add_term_to_end(
                    self.TermNode(
                        current_self_term.coefficient,
                        current_self_term.exponent))
                current_self_term = current_self_term.next
            else:
                result_polynomial._add_term_to_end(
                    self.TermNode(
                        current_other_term.coefficient,
                        current_other_term.exponent))
                current_other_term = current_other_term.next

        # add any remaining terms from current
        while current_self_term:
            result_polynomial._add_term_to_end(
                self.TermNode(
                    current_self_term.coefficient,
                    current_self_term.exponent))
            current_self_term = current_self_term.next

        # add any remaining terms from other
        while current_other_term:
            result_polynomial._add_term_to_end(
                self.TermNode(
                    current_other_term.coefficient,
                    current_other_term.exponent))
            current_other_term = current_other_term.next

        result_polynomial._first_term = result_polynomial._first_term.next

        return result_polynomial

    def __mul__(self, other):
        result_polynomial = None
        current_self_term = self._first_term

        while current_self_term is not None:
            current_other_term = other._first_term

            while current_other_term is not None:
                if result_polynomial is None:
                    result_polynomial = Polynomial(
                        current_self_term.coefficient * current_other_term.coefficient,
                        current_self_term.exponent + current_other_term.exponent )
                else:
                    # TODO - make this fast?
                    result_polynomial = result_polynomial + Polynomial(
                        current_self_term.coefficient * current_other_term.coefficient,
                        current_self_term.exponent + current_other_term.exponent )

                current_other_term = current_other_term.next
            current_self_term = current_self_term.next
        return result_polynomial

    def differentiate(self):

        result_polynomial = Polynomial(
            self._first_term.coefficient * self._first_term.exponent,
            self._first_term.exponent - 1)

        current_term = self._first_term.next

        while current_term is not None:
            result_polynomial._add_term_to_end(
                self.TermNode(
                    current_term.coefficient * current_term.exponent,
                    current_term.exponent - 1) )
            current_term = current_term.next

        return result_polynomial



    def __str__(self):
        result = ""
        current_term = self._first_term

        while current_term is not None:
            if current_term.exponent == 1:
                result += f'{current_term.coefficient:.2f}x'
            elif current_term.exponent == 0:
                result += f'{current_term.coefficient:.2f}'
            else:
                result += f'{current_term.coefficient:.2f}x^{current_term.exponent}'
            current_term = current_term.next
            if current_term is not None:
                result += " + "

        return result

    def integrate(self):

        result_polynomial = Polynomial(
            self._first_term.coefficient / ( self._first_term.exponent + 1 ),
            self._first_term.exponent + 1)

        current_term = self._first_term.next

        while current_term is not None:
            result_polynomial._add_term_to_end(
                self.TermNode(
                    current_term.coefficient / ( current_term.exponent + 1 ),
                    current_term.exponent + 1))
            current_term = current_term.next

        return result_polynomial

    def __eq__(self, other):
        current_self_term = self._first_term
        current_other_term = other._first_term

        while current_self_term and current_other_term:
            if current_self_term != current_other_term:
                return False
            current_self_term = current_self_term.next
            current_other_term = current_other_term.next

        # if either have any left it's false
        return not (current_self_term and current_other_term)

    def __ne__(self, other):
        return not self == other