from datetime import *

counter = 0
year = 1901
month = 0

while True:

	if month != 12:
		month += 1
		curr_date = date(year,month,1)
	else:
		year += 1
		month = 1
	
	if curr_date.weekday() == 6:
		counter += 1

	if year == 2000:
		break

print(counter)