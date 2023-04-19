# Bikes and cars are being parked
# I charge 10 per hour for bikes
# I charge 50 per hour for Cars
# Need to audit on the money I am receiving at the end of the day
# user inputs : no of cars, 
# total no of hours the cars were in the parking
# no of bikes, total no of hours the bikes are there
# can we print the total money he will get at the end of the day


#inputs for car
cost_per_hour_car=50
total_cars_count=int(input("Total no. of cars"))
cars_total_hours=int(input("Total hours for cars"))

# input for bikes
cost_per_hour_bike=10
total_bike_count=int(input("Total no. of Bikes"))
bike_total_hours=int(input("Total no of hours for bikes"))

#Car payment

Cars_total_payment=cost_per_hour_car*total_cars_count*cars_total_hours

#bike payment
bike_total_payment=cost_per_hour_bike*total_bike_count*total_bike_count

#Total Parking lot payment for the day

Total_Parking_Payment=Cars_total_payment+bike_total_payment
print(Total_Parking_Payment)

# user input on how much money that the owner received 
# if auditing is successful or ther is a difference and how much is 
# the difference
#if statement

total_money_received=int(input("Total_money_received"))

# if else
#Auditing Amount matches with the Amount Received by the Owner
if (total_money_received == Total_Parking_Payment):
    print("Everything is OK!!")

#Auditing Amount not matches with the Amount Received by the Owner    
else:
    differenceOfAmount = (Total_Parking_Payment - total_money_received)
    print("The Difference of the Amount is: ", differenceOfAmount) #The Amount Difference Received by the Owner