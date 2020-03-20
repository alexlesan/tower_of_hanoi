
TOTAL_MOVES = 0

def move(f, t):
    print('Move disc from {} to {}!'.format(f, t))

# increment total moves number
def increment_moves():
    global TOTAL_MOVES
    TOTAL_MOVES += 1

"""
	n - number of disks
	f - from position
	h - helper position
	t - target position
"""
def hanoi_moves(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi_moves(n - 1, f, t, h)
        move(f, t)
        increment_moves()
        hanoi_moves(n - 1, h, f, t)

print("\nGet solutions for minimum moves of 'Tower of Hanoi' game: ")
while True:
    number_of_discs = int(input("\nEnter the number of discs: "))
    if number_of_discs < 3 or number_of_discs > 8:
        print("\nPlease enter a valid number of discs. (min:3 , max: 8) ")
        continue
    else:
        break

hanoi_moves(number_of_discs, "A", "B", "C")
print("###### Minimum moves: " + str(TOTAL_MOVES) + " ######")
print()
