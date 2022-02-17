import csv

# Now we'll create our three variables to hold the count of each
# type of Citi bike user, beginning the count for each at zero.

int_subcriber_count = 0
int_customer_count = 0
int_other_user_count = 0

fl_source_file = open('202009-citibike-tripdata.csv')

rd_citibike_reader = csv.DictReader(fl_source_file)
counter = 0
for a_row in rd_citibike_reader:

    if a_row["usertype"] == 'Subscriber':
        int_subcriber_count += 1

    elif a_row['usertype'] == 'Customer':
        int_customer_count += 1

    else:
        int_other_user_count += 1        
    counter += 1    

print('Number of subscribers: ' + str(int_subcriber_count))
print('Number of customers: ' + str(int_customer_count))
print('Number of other users: ' + str(int_other_user_count))
print(counter)