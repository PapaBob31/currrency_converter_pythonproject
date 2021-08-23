# a simple currency_converter
import json

exchange_names = ["dollars to naira", "naira to dollars", "dollars to pounds", "pounds to dollars", 
				   "naira to pounds", "pounds to naira"]

""""{"dollars to naira": 411, "naira to dollars": 0.0024, "dollars to pounds": 0.73,
 "pounds to dollars": 1.36,"naira to pounds": 0.0018 , "pounds to naira": 560.84}"""

running = True
option = ""
menu = True
valid_option_input = False
convert = False
exchange_rates = ""
rate = ""
rate_name = ""
amount = ""
initial_currency = ""
converted_currency = ""
amount_input = False
pick_update_option = False
update_menu = False
new_rate_index = ""
first_input = True
input_update = False

while running:
	if menu:
		print("Type in the index of the exchange medium you want to use"
			  "\n1. Dollars -> Naira\n2. Naira -> Dollars\n3. Dollars -> Pounds\n4. Pounds -> Dollars"
			  "\n5. Naira -> Pounds\n6. Pounds -> Naira\n7. Update Converter\n"
			  "Type 'end' at any prompted input to quit the converter")
		with open("exchange_rate.json") as exchange_rates_file:
			exchange_rates = json.load(exchange_rates_file)
		menu = False

	if not valid_option_input:
		option = input()
		option = option.strip()
		option = option.lower()
		if option == "end":
			break
		elif option == "7":
			print("ok")
			pick_update_option = True
			update_menu = True
			valid_option_input = True
		else:
			try:
				option = int(option)
			except:
				print("invalid input, pls enter a valid input")
			else:
				if option in range(1, 7):
					option = option - 1
					amount_input = True
					valid_option_input = True
				else:
					print("invalid input, pls enter a valid input")
					valid_option_input = False

	if amount_input:
		for conversion_name in exchange_names           :
			if exchange_names.index(conversion_name) == option:
				rate = exchange_rates[conversion_name]
				rate_name = conversion_name
				initial_currency = input("enter the amount you want to convert from " + rate_name + ": ")
				convert = True
				amount_input = False

	if convert:
		try:
			amount = float(initial_currency)
		except:
			initial_currency = input("invalid input, pls enter a number: ")
		else:
			converted_currency = rate * amount
			converted_currency = str(converted_currency)
			if converted_currency[-2:] == ".0":
				converted_currency = round(float(converted_currency))
				print(str(initial_currency) + " converted from " + rate_name + " is equals to " + str(converted_currency) + "\n")
				menu = True
				valid_option_input = False
				convert = False
			else:
				converted_currency = float(converted_currency)
				print(str(initial_currency) + " converted from " + rate_name + " is equals to " + str(converted_currency) + "\n")
				menu = True
				valid_option_input = False
				convert = False

	if pick_update_option:
		no = 0
		if update_menu:
			for exchange, value in exchange_rates.items():
				no += 1
				print(str(no) + ". " + exchange + ": " + str(value) + "\n")
			new_rate_index = input("the above are the exchange rates, enter the index of the one you want to change: ")
			update_menu = False
		new_rate_index = new_rate_index.strip()
		try:
			new_rate_index = int(new_rate_index)
		except:
			new_rate_index = input("invalid input, pls enter a valid inputs")
		else:
			if new_rate_index in range(1, 7):
				new_rate_index = new_rate_index - 1
				input_update = True
				pick_update_option = False

	if input_update:
		for conversion in exchange_names:
			if exchange_names.index(conversion) == new_rate_index:
				if first_input:
					new_rate = input("enter the new exchange rate for " + conversion + ", Note: this should be a number!\n")
					first_input = False
				try:
					new_rate = float(new_rate)
				except:
					new_rate = input("invalid input, pls enter a valid input")
				else:
					exchange_rates[conversion] = new_rate
					with open("exchange_rate.json", "w") as exchange_rates_file:
				 		json.dump(exchange_rates, exchange_rates_file)
					print("exchange rate updated sussecfully")
					menu = True
					valid_option_input = False
					input_update = False

# one dolllar is 0.73 pound sterling
# one pound is 1.36 us dollars
# one pound sterling equals 560.84 naira
# one naira equals 0.0018 pound sterling
