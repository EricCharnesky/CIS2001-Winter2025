import random

class PowerBallTicket:

    def __init__(self, numbers = None):
        if numbers:
            self._numbers = numbers[:]
            # TODO - make sure these are good

        else:
            self._numbers = random.sample(range(1,70), 5)
            self._numbers.append(random.randint(1, 26))

    def __str__(self):
        return " ".join(str(number) for number in self._numbers)

    def get_numbers(self):
        return self._numbers[:]

    def get_winnings(self, winning_ticket):
        white_matches = 0
        red_matches = self._numbers[5] == winning_ticket.get_numbers()[5]

        for number in self._numbers[:5]:
            if number in winning_ticket.get_numbers()[:5]:
                white_matches += 1

        if red_matches and white_matches == 5:
            print("JACKPOT!")
            return 1_000_000_000
        if white_matches == 5:
            return 1_000_000
        if white_matches == 4 and red_matches:
            return 50_000
        if white_matches == 4 or ( white_matches == 3 and red_matches ):
            return 100
        if white_matches == 3 or ( white_matches == 2 and red_matches):
            return 7
        if red_matches:
            return 4
        return 0


tickets = int(input("How many tickets do you want to buy?"))
total_spent = tickets * 2
total_won = 0

winning_ticket = PowerBallTicket()

for ticket in range(tickets):
    my_ticket = PowerBallTicket()
    #print(my_ticket)
    total_won += my_ticket.get_winnings(winning_ticket)
    if ticket % 100_000 == 0:
        print(ticket)

print(f"Total Won: ${total_won:,d}")
print(f'Total Spent ${total_spent:,d}')
print(f'Net Loss ${total_won - total_spent:,d}')

