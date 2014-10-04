
def get_cust_data(cust_order_file, customer_ordered, customer_paid):
    "Read in orders from file and return tally the amount of the orders and amount paind by customer"

    cust_order_file = open(cust_order_file)

    for line in cust_order_file:
        line = line.rstrip()
        data = line.split(",")
#        print 0, data
        cust_name = data[1]

        amt_ordered = int(data[2])
        amt_cust_paid = float(data[3])

        customer = customer_ordered.get(cust_name)
        if not customer:
            customer_ordered[cust_name] = amt_ordered 
            customer_paid[cust_name] = amt_cust_paid
#            print ("1 cust", cust_name, amt_ordered, amt_cust_paid)
        else:
            customer_ordered[cust_name] += amt_ordered 
            customer_paid[cust_name] += amt_cust_paid

    cust_order_file.close()


def process_cust_orders():
    
    customer_ordered = {}
    customer_paid = {}
    
    get_cust_data("customer_orders.csv", customer_ordered, customer_paid)
    
    count_paid = 0
    count_not_paid = 0
    for cust_name in customer_ordered:
        if customer_ordered[cust_name] != customer_paid[cust_name]:
            print cust_name, "paid %.2f, expected %.2f"%(customer_ordered[cust_name], customer_paid[cust_name])
            count_not_paid += 1
        else:
            count_paid += 1
    print "%d customers have not paid in full." % count_not_paid
    print "%d customers paid in full." % count_paid 


def main():

    process_cust_orders()


if __name__ == "__main__":
    main()