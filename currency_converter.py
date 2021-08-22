# a simple currency_converter

running = True
option = ""
exchange_name = ["dollars to naira", "naira to dollars", "dollars to pounds", "pounds to dollars", 
				   "naira to pounds", "pounds to naira"]

exchange_rate = {"dollars to naira": 411, "naira to dollars": 0.0024, "dollars to pounds": 0.73, "pounds to dollars": 1.36,
				 "naira to pounds": 0.0018 , "pounds to naira": 560.84}
menu = True
menu_input = False
convert = False
rate = ""
amount = ""
initial_currency = ""
converted_currency = ""

while running:
	if menu:
		print("Type in the index of the exchange medium you want to use"
			  "\n1. Dollars -> Naira\n2. Naira -> Dollars\n3. Dollars -> Pounds\n4. Pounds -> Dollars"
			  "\n5. Naira -> Pounds\n6. Pounds -> Naira\n7. Update Converter\nType 'end' to quit the converter")
		menu = False
		menu_input = True

	if menu_input:
		option = input()
		option = option.strip()
		option = option.lower()
		if option == "end":
			break
		else:
			try:
				option = int(option)
			except:
				print("invalid input, pls enter a valid input")
			else:
				if option in range(1, 6):
					option = option - 1
					menu_input = False
					convert = True

	if convert:
		for name in exchange_name:
			if exchange_name.index(name) == option:
				rate = exchange_rate[name]
				initial_currency = input("enter the amount you want to convert from " + name + ": ")
				try:
					amount = float(initial_currency)
				except:
					print("invalid input, pls enter a number")
				else:
					converted_currency = rate * amount
					converted_currency = str(converted_currency)
					if converted_currency[-2:] == ".0":
						converted_currency = round(float(converted_currency))
					else:
						converted_currency = float(converted_currency)
					print(str(initial_currency) + " converted from " + name + " is equals to " + str(converted_currency) + "\n")
					menu = True
					menu_input = False
					convert = False

# one dolllar is 0.73 pound sterling
# one pound is 1.36 us dollars
# one pound sterling equals 560.84 naira
# one naira equals 0.0018 pound sterling
