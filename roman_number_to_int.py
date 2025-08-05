roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}
roman_number = "XIV"

roman_list = list(roman_number)
roman_interger = 0

for i in range(len(roman_list)):
	if i + 1 < len(roman_list) and roman_dict[roman_list[i]] < roman_dict[roman_list[i + 1]]:
		roman_interger -= roman_dict[roman_list[i]]
	else:
		roman_interger += roman_dict[roman_list[i]]

print(roman_interger)



