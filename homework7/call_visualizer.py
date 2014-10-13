"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

# Load the customers from the passed filename
# Return a dictionary containing the customer data
#    (key = customer_id)
def load_customers(filename):
	customers = {}
	#f = open(filename:
	print filename
    
	# First line of the file should be the header, 
	#   split that into a list
	header = "customer_id,first,last,email,telephone,called"
	#header = f.readline().rstrip().split(',')
	header = header.split(',')

	# Process each line in a file, create a new
	#   dict for each customer
	#for line in f:
	filename = filename.split('\n')

	for line in filename:
		data = line.rstrip().split(',')
		customer = {}

		# Loop through each column, adding the data
		#   to the dictionary using the header keys
		for i in range(len(header)):
			customer[header[i]] = data[i]

		# Add the customer to our dictionary by customer id
		customers[customer['customer_id']] = customer

	# Close the file
	#f.close()

	return customers

# Load the orders from the passed filename
# Return a list of all the orders
def load_orders(filename):
	orders = []
	#f = open(filename)
	print filename

	# First line of the file should be the header, 
	#   split that into a list
	header = "order_id,order_date,status,customer_id,email,address,city,state,postalcode,num_watermelons,num_othermelons,subtotal,tax,order_total"
	#header = f.readline().rstrip().split(',')
	header = header.split(',')

	# Process each line in a file, create a new
	#   dict for each order
	#for line in f:
	filename = filename.replace('\n',',').split(',')
	for line in filename:
		data = line.rstrip().split(',')

		# Create a dictionary for the order by combining
		#   the header list and the data list
		order = dict(zip(header, data))

		# Add the order to our list of orders to return
		orders.append(order)

	# Close the file
	#f.close()

	return orders

def display_customer(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print "Name: ", customer.get('first', ''), customer.get('last', '')
	print "Phone: ", customer.get('telephone')
	print "\n"

def main():
	# Load data from our csv files
	#customers = load_customers('customers.csv')
	#orders    = load_orders('orders.csv')
	customers = load_customers(filename1)
	orders    = load_orders(filename2)

	# Loop through each order
	for order in orders:
		# Is this order over 20 watermelon?
		if order.get('num_watermelons', 0) > 20:
			# Has this customer not been contacted yet?
			customer = customers.get(order.get('customer_id', 0), 0)
			if customer.get('called', '') == '':
				display_customer(customer)
				break

#if __name__ == '__main__':
#	main()
filename1 = """445,Denise,Hayes,christina@shufflester.org,3-(689)945-8228,04/16/2014
860,Lillian,Collins,teresa@thoughtstorm.edu,1-(889)291-8213,"""
filename2 = """2,05/10/2014,New,860,teresa@thoughtstorm.edu,91520 Spaight Street,San Francisco,KY,23769-1104,105,0,312.00,18.72,339.31
7,05/18/2014,Out for Delivery,445,christina@shufflester.org,4 Sullivan Road,Rio Vista,GA,59830,40,0,100.75,6.04,111.38"""
main()