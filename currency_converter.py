# a simple currency_converter

running = True
option = ""
possible_inputs = ["1", "2", "3", "end"]
empty_input = True
initial_currency = ""

while running:
	if empty_input:
		option = input("Type in the index of the exchange medium you want to use"
						"\n1. Dollars -> Naira\n2. Naira -> Dollars\n3. Dollars -> Pounds"
						"\nType 'end' to quit the converter\n")
		option = option.strip()
		option = option.lower()
		if option in possible_inputs:
			if option == "end":
				running = False
			empty_input = False
		else:
			print("That is not a valid input, Pls enter a valid input!")

	if not empty_input:
		if option == "1":
			initial_currency = input("Pls enter the amount you want to convert to Naira\n")
			initial_currency = initial_currency.strip()
			try:
				initial_currency = int(initial_currency)
			except ValueError:
				print("That is not a valid input, Input must be an integer")
			else:
				new_currency = initial_currency * 388
				print(str(new_currency) + " Naira!")
				empty_input = True

		if option == "2":
			initial_currency = input("Pls enter the amount you want to convert to Naira\n")
			initial_currency = initial_currency.strip()
			try:
				initial_currency = int(initial_currency)
			except ValueError:
				print("That is not a valid input, Input must be an integer")
			else:
				new_currency = initial_currency * 388
				print(str(new_currency) + " Naira!")
				empty_input = True

		if option == "3":
			initial_currency = input("Pls enter the amount you want to convert to Naira\n")
			initial_currency = initial_currency.strip()
			try:
				initial_currency = int(initial_currency)
			except ValueError:
				print("That is not a valid input, Input must be an integer")
			else:
				new_currency = initial_currency * 388
				print(str(new_currency) + " Naira!")
				empty_input = True
