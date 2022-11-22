from extracing_color_info import *
from extracting_number_info import *


def print_total_output(min_number, max_number):
	print("Printing all outputs")
	#pair_number = get_pair_number_from_color(major_color, minor_color)
	for pair_number in range(min_number, max_number+1):
		major_color, minor_color = get_pairNumber_ofColor(pair_number)
		print (str(pair_number) +" " + major_color, minor_color)
	return f'{pair_number} {major_color} {minor_color}'
