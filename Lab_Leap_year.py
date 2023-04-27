input_year = int(input())
 
if ((input_year % 100) == 0):
	if((input_year % 400) == 0):
		print(f'{input_year} - leap year')
	else:
		print(f'{input_year} - not a leap year')
elif ((input_year % 4) == 0):
	print(f'{input_year} - leap year')
else:
	print(f'{input_year} - not a leap year')
