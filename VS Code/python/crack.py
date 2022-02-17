from string import digits
from itertools import product

times = 0

for passcode in product(digits, repeat=11):
	print(*passcode)
	if passcode == 11232615184:
		break
			