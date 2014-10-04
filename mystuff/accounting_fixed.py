
def tally_orders(filename):
    "Read in orders from file and return tally of # orders by melon type."

    order_file = open(filename)
    
    melon_tallies = {
        "Musk": 0, 
        "Hybrid": 0, 
        "Watermelon": 0, 
        "Winter": 0,
    }
    
    for line in order_file:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    order_file.close()

    return melon_tallies


def print_orders_by_type(filename):
    "Print order summaries of type."
    
    melon_tallies = tally_orders(filename)

    MELON_PRICES = { 
        "Musk": 1.15, 
        "Hybrid": 1.30, 
        "Watermelon": 1.75, 
        "Winter": 4.00,
    }

    total_revenue = 0
    for melon_type in melon_tallies:
        price = MELON_PRICES[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (
            melon_tallies[melon_type], 
            melon_type, 
            price, 
            revenue
        )
    print "Total revenue: %0.2f" % total_revenue


def sum_orders_by_source(filename):
    "Sum up orders, grouped by online or by sales staff and report outcomes."
    
    sales_file = open(filename)

    sales_online = 0
    sales_staff = 0

    for line in sales_file:
        line = line.rstrip(\n)
        data = line.split(",")
        order_id, saleperson_id, name, amt_as_string = data
        amt = float(amt_as_string)
        
        if saleperson_id == "0":
            sales_online += amt
        else:
            sales_staff += amt

    print "Salespeople generated %0.2f in revenue." % sales_staff
    print "Internet sales generated %0.2f in revenue." % sales_online

    if sales_staff > sales_online:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


def main():
    print "******************************************"
    print_orders_by_type("orders_by_type.csv")
    print "******************************************"
    sum_orders_by_source("orders_with_sales.csv")
    print "******************************************"
    

if __name__ == "__main__":
    main()
