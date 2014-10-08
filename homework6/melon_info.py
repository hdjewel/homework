"""
melon_info.py - Prints out all the melons in our inventory

"""

#from melons import melon_name, melon_seedless, melon_price
#from melons import melon_flesh_color, melon_rind_color, melon_weight
from melons import melon_data

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
    for i in melon_name.keys():
        print_melon(melon_name[i], melon_seedless[i], melon_price[i],
        	melon_flesh_color[i], melon_rind_color[i], melon_weight[i])