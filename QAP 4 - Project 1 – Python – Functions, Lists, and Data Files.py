# QAP 4 - Project 1 – Python – Functions, Lists, and Data Files 
# Software Development - SD12
# Date : July 26th, 2024
# Submitted by : Wayne Norman



# Import Databases
import datetime
import calendar
import json
import time

# A separate file created for constants. Labelled as Const.dat
# Place code to open the contents of Const.dat and then parse the data
with open('Const.dat.txt', 'r') as f:
    CONSTANTS = json.load(f)

# Program starts here


# Find initial policy number
policy_number = CONSTANTS['next_policy_number']

# Create a list to validate provinces
VALID_PROVINCES = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']

# Create a list to validate payment methods
VALID_PAYMENT_METHODS = ['Full', 'Monthly', 'Down Pay']

# Create a list to store all policies
all_policies = []

# Gather data from user
    
def get_customer_info():
    first_name = input("Enter customer's first name: ").title()
    last_name = input("Enter customer's last name: ").title()
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ").title()
    province = input("Enter customer's province: ").upper()

    # Validate provinces here

    while province not in VALID_PROVINCES:
        print("Invalid province. Please enter a valid province.")
        province = input("Enter customer's province: ").upper()
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")
    num_cars = int(input("Enter the number of cars being insured: "))

    # Input and validate Y or N for extra liability, glass coverage, and loaner car

    while True:
        extra_liability = input("Extra liability up to $1,000,000 (enter Y for Yes or N for No): ").upper()
        if extra_liability in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")

    while True:
        glass_coverage = input("Optional glass coverage (Y or N): ").upper()
        if glass_coverage in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")
    while True:
        loaner_car = input("Optional loaner car (Y or N): ").upper()
        if loaner_car in ['Y', 'N']:
            break
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")

    # Validate payment method here from list
    # If down payment chosen, create secondary input (as a float) for the payment value preferred

    payment_method = input("Enter payment method (Full, Monthly, Down Pay): ")
    while payment_method not in VALID_PAYMENT_METHODS:
        print("Invalid payment method. Please enter a valid payment method.")
        payment_method = input("Enter payment method (Full, Monthly, Down Pay): ")
    down_payment = 0
    if payment_method == 'Down Pay':
        down_payment = float(input("Enter the amount of the down payment: "))

    

    # Calcualtions for the individual premium costs to be displayed, and adjust for a Y or N answer
    if extra_liability == 'Y':
        extra_liabilitydsp = num_cars * CONSTANTS['cost_of_extra_liability_coverage']
    else:
        extra_liabilitydsp = 0
    
    if glass_coverage == "Y":
        glass_coveragedsp = num_cars * CONSTANTS['cost_of_glass_coverage']
    else:
        glass_coveragedsp = 0
    
    if loaner_car == "Y":
        loaner_cardsp = num_cars * CONSTANTS['cost_for_loaner_car_coverage']
    else:
        loaner_cardsp = 0

    # return all data collected
    return first_name, last_name, address, city, province, postal_code, phone_number, num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment, extra_liabilitydsp, glass_coveragedsp, loaner_cardsp

# Function to calculate the premiums added. Start with value = 0, then as premium selected, add to total 

def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    premium = CONSTANTS['basic_premium']
    if num_cars > 1:
        premium += (num_cars - 1) * CONSTANTS['basic_premium'] * (1 - CONSTANTS['discount_for_additional_cars'])
    extra_costs = 0
    if extra_liability == 'Y':
        extra_costs += num_cars * CONSTANTS['cost_of_extra_liability_coverage']
    if glass_coverage == 'Y':
        extra_costs += num_cars * CONSTANTS['cost_of_glass_coverage']
    if loaner_car == 'Y':
        extra_costs += num_cars * CONSTANTS['cost_for_loaner_car_coverage']

    total_premium = premium + extra_costs
    total_premiumdsp = premium + extra_liabilitydsp + glass_coveragedsp + loaner_cardsp
    HST = total_premiumdsp * CONSTANTS['HST_rate']
    total_cost = total_premium + HST

    
    return total_premium, HST, total_cost, premium, total_premiumdsp

# Function to calculate payments
# Payment may be full or in 8 monthly payments. (Add processing fee of $39.99 to the total cost and dividing the total cost by 8.) 
 
def calculate_payments(total_cost, payment_method, down_payment):
    if payment_method == 'Full':
        return total_cost, 1
    else:
        total_cost += CONSTANTS['processing_fee_for_monthly_payments']
        if payment_method == 'Down Pay':
            total_cost -= down_payment
        monthly_payment = total_cost / 8
        return monthly_payment, 8

# Main loop
while True:
    # Call the main function (get customer info) and store the return values
    first_name, last_name, address, city, province, postal_code, phone_number, num_cars, extra_liability, glass_coverage, loaner_car, payment_method, down_payment, extra_liabilitydsp, glass_coveragedsp, loaner_cardsp = get_customer_info()
    total_premium, HST, total_cost, premium, total_premiumdsp = calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car)
    payment_amount, num_payments = calculate_payments(total_cost, payment_method, down_payment)

    final_costdsp = total_cost - down_payment

    # Calculate the date of the first payment
    today = datetime.date.today()
    first_payment_date = datetime.date(today.year if today.month < 12 else today.year + 1, today.month % 12 + 1, 1)

    # Print the receipt
    print(f" --------------------------------------------")
    print(f"|         One Stop Insurance Company          |")
    print(f"| ------------------------------------------- |")
    print(f"| Customer Information:      Date: {today.strftime('%Y-%m-%d')} |")
    print(f"|                                             |")
    print(f"| Name: {first_name[:10]:<10s} {last_name[:10]:<10s}                 |")
    print(f"| Address: {address[:10]:<10s}, {city[:10]:<10s}, {province}, {postal_code[:6]:<6s} |")
    print(f"| Phone Number: {phone_number:<10s}                    |")
    print(f"| ------------------------------------------- |")
    print(f"| ------------------------------------------- |")
    print(f"| Policy Details                    Charge    |")
    print(f"|                                             |")
    print(f"| Number of Cars: {num_cars}                           |")
    print(f"| Standard Premium:                 ${premium:8.2f} |")    
    print(f"| Extra Liability: {'Yes' if extra_liability == 'Y' else 'No '}              ${extra_liabilitydsp:8.2f} |")
    print(f"| Glass Coverage: {'Yes' if glass_coverage == 'Y' else 'No '}               ${glass_coveragedsp:8.2f} |")
    print(f"| Loaner Car: {'Yes' if loaner_car == 'Y' else 'No '}                   ${loaner_cardsp:8.2f} |")
    print(f"| ------------------------------------------- |")
    print(f"| ------------------------------------------- |")
    print(f"| Financial Details:                          |")
    print(f"|                                             |")
    print(f"| Total Premiums:                   ${total_premiumdsp:8.2f} |")
    print(f"| HST:                              ${HST:8.2f} |")
    print(f"| ------------------------------------------- |")
    print(f"| Preliminary Total:                ${total_cost:8.2f} |")
    print(f"| ------------------------------------------- |")
    print(f"| Payment Information:                        |")
    print(f"|                                             |")
    print(f"| Payment Method:  {payment_method[:10]:<10s}                 |")
    print(f"| Down Payment:                     ${down_payment:8.2f} |")
    print(f"| ------------------------------------------- |")
    print(f"| Total Cost:                       ${final_costdsp:8.2f} |")
    print(f"| ------------------------------------------- |")
    print(f"| Payment Plan:                               |")
    print(f"|                                             |")
    print(f"| Payment Amount:                   ${payment_amount:8.2f} |")
    print(f"| Number of Payments: {num_payments}                       |")
    print(f"| ------------------------------------------- |")
    print(f"| Policy Number: {policy_number}                         |")
    print(f"| First Payment Date: {first_payment_date.strftime('%Y-%m-%d')}              |")
    print(f"|                                             |")
    print(f"|    ---  Thanks for Insuring with us!  ---   |")
    print(f" =============================================")

    # Save the policy
    all_policies.append({
        'Policy Number': policy_number,
        'Claim Date': today.strftime('%Y-%m-%d'),
        'Total Amount': total_cost
    })

    # Increase the policy number
    policy_number += 1

    print(f"")
    print(f"")

    # Show a progress bar to indicate that the information is being saved
    print("Saving information", end='', flush=True)
    for i in range(10):
        print('.', end='', flush=True)
        time.sleep(0.5)  # Wait for half a second
    print(" Done!")

    print(f"")
    print(f"")

    # Ask the user if they have completed their input
    repeat = input("Enter another customer? (Y/N): ").upper()
    if repeat != 'Y':
        break

# Print a table showing each policy number, claim date, and total amount
print(f"{'Policy Number':<15} {'Claim Date':<12} {'Total Amount':<12}")
print(f"--------------------------------------------------------------")
for policy in all_policies:
    
    
    print(f"{policy['Policy Number']:<15} {policy['Claim Date']:<12} ${policy['Total Amount']:.2f}")
