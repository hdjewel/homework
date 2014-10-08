"""
melon_info.py - Prints out all the melons in our inventory

"""

#from melons import melon_name, melon_seedless, melon_price
#from melons import melon_flesh_color, melon_rind_color, melon_weight
from new_melon_data import melon_data


def print_melon(name, seedless, price,
				flesh_color, rind_color, 
				weight):
	hashasnot = 'have'
	if seedless:
		hashasnot = 'do not have'
	
	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)
	print "\tThe flesh is %s color." % flesh_color
	print "\tThe rind is %s." % rind_color
	print "\tIt weights about %s." % weight


if __name__ == '__main__':
	# melon_data = {
	#     "Honeydew": (0.99, True, "Pale Green", "Yellow", "4.0 - 7.9"),
	#     "Crenshaw": (2.00, False, "Orange-Pink", "Yellow-Green", "5.0 - 6.0"),
	#     "Crane": (2.50, False, "Orange", "Fawn", "5.0 - 6.0"),
	#     "Casaba": (2.50, False, "Orange", "Yellow", "4.0 - 7.0"),
	#     "Cantaloupe": (0.99, False, "Grey", "Beige", "5.0 - 6.0")
	# }
    for name in melon_data.keys():
		(price, seedless, flesh_color, rind_color, weight) = melon_data[name]
		print_melon(name, seedless, price, 
					flesh_color, rind_color, weight)
#		print_melon(melon_name[i], melon_seedless[i], melon_price[i],
#        	melon_flesh_color[i], melon_rind_color[i], melon_weight[i])
#	print 1.1, melon_data
#	print 1.2, melon_data["Honeydew"][0]

    # for i in melon_name.keys():
    #     print_melon(melon_name[i], melon_seedless[i], melon_price[i])