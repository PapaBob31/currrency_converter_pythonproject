"""A simple currency_converter that runs from the command line... 
or any other application that can run python files correctly"""
import json

exchange_names = ["dollars to naira", "naira to dollars", "dollars to pounds", "pounds to dollars", 
				   "naira to pounds", "pounds to naira"]

running = True
option = ""
menu = True
valid_option_input = False
convert = False
exchange_rates = {}
rate = ""
rate_name = ""
amount = ""
initial_currency = ""
converted_currency = ""
exchange_medium = ""
amount_input = False
pick_update_option = False
update_menu = False
new_rate_index = ""
first_input = True
input_update = False
first_quit_msg = True
performing_tasks = True
quit_input = ""

def check_for_exitcommand(user_input):
	user_input.lower()
	if user_input == "end":
		exit()
	if user_input == "#":
		print(bool(pick_update_option))

def quit_converter_message():
	global menu, valid_option_input, convert, pick_update_option, first_quit_msg, quit_input, performing_tasks, input_update, update_menu
	if first_quit_msg:
		quit_input = input("would you like to run the converter again?\nType 'y' to return to main menu and 'n' to quit: ")
		quit_input = quit_input.strip()
		check_for_exitcommand(quit_input)
		first_quit_msg = False
	if quit_input == "y":
		first_quit_msg = True
		menu = True
		valid_option_input = False
		convert = False
		pick_update_option = False
		update_menu = True
		input_update = False
		performing_tasks = True
	elif quit_input == "n":
		exit()
	else:
		quit_input = input("Invalid input, pls enter a valid input: ")
		quit_input = quit_input.strip()
		check_for_exitcommand(quit_input)


while running:
	if performing_tasks:
		if menu:
			print("\nType in the index of the exchange medium you want to use"
				  "\n1. Dollars -> Naira\n2. Naira -> Dollars\n3. Dollars -> Pounds\n4. Pounds -> Dollars"
				  "\n5. Naira -> Pounds\n6. Pounds -> Naira\n7. Update Converter\n"
				  "Type 'end' at any prompted input to quit the converter")
			with open("exchange_rate.json") as exchange_rates_file:
				exchange_rates = json.load(exchange_rates_file)
			menu = False

		if not valid_option_input:
			option = input()
			option = option.strip()
			check_for_exitcommand(option)
			if option == "7":
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
					initial_currency = initial_currency.strip()
					check_for_exitcommand(initial_currency)
					convert = True
					amount_input = False

		if convert:
			try:
				amount = float(initial_currency)
			except:
				initial_currency = input("invalid input, pls enter a number: ")
				initial_currency = initial_currency.strip()
				check_for_exitcommand(initial_currency)
			else:
				converted_currency = rate * amount
				converted_currency = str(converted_currency)
				if converted_currency[-2:] == ".0":
					converted_currency = round(float(converted_currency))
					print(str(initial_currency) + " converted from " + rate_name + " is equals to " + str(converted_currency) + "\n")
					performing_tasks = False
				else:
					converted_currency = float(converted_currency)
					print(str(initial_currency) + " converted from " + rate_name + " is equals to " + str(converted_currency) + "\n")
					performing_tasks = False
					
		if pick_update_option:
			no = 0
			if update_menu:
				for exchange, value in exchange_rates.items():
					no += 1
					print(str(no) + ". " + exchange + ": " + str(value) + "\n")
				new_rate_index = input("the above are the exchange rates, enter the index of the one you want to change: ")
				update_menu = False
			new_rate_index = new_rate_index.strip()
			check_for_exitcommand(new_rate_index)
			try:
				new_rate_index = int(new_rate_index)
			except:
				new_rate_index = input("invalid input, pls enter a valid input: ")
				new_rate_index = new_rate_index.strip()
				check_for_exitcommand(new_rate_index)
			else:
				if new_rate_index in range(1, 7):
					new_rate_index = new_rate_index - 1
					first_input = True
					input_update = True
					pick_update_option = False
				else:
					new_rate_index = input("invalid input, pls enter a valid input: ")
					new_rate_index = new_rate_index.strip()
					check_for_exitcommand(new_rate_index)

		if input_update:
			if first_input:
				for conversion in exchange_names:
					if exchange_names.index(conversion) == new_rate_index:
						exchange_medium = conversion
						new_rate = input("Enter the new exchange rate for " + conversion + ", Note: this must be a number!\n")
						new_rate = new_rate.strip()
						check_for_exitcommand(new_rate)
						first_input = False
			try:
				new_rate = float(new_rate)
			except:
				new_rate = input("invalid input, pls enter a valid input: ")
				new_rate = new_rate.strip()
				check_for_exitcommand(new_rate)
			else:
				exchange_rates[exchange_medium] = new_rate
				with open("exchange_rate.json", "w") as exchange_rates_file:
			 		json.dump(exchange_rates, exchange_rates_file)
				print("exchange rate updated succesfully\n")
				performing_tasks = False

	if not performing_tasks:
		quit_converter_message()

"""At the time of writting this program, the exchange rates below were valid, don't know about now though"""
# one dolllar equals 0.73 pound sterling
# one pound equals 1.36 us dollars
# one pound sterling equals 560.84 naira
# one naira equals 0.0018 pound sterling
