#ScottJHW3B.pyw
#Jennifer Scott
#June 6, 2018
#Assignment 3B program written from pay scale flowchart.

#Global constant for hourly, commission, and witholding rates.
HOURLY_PAY_RATE=7.50
COMMISSION_RATE=0.05
WITHHOLDING_RATE=0.25

def main():
    display_message()
    name=input('Enter Name: ')
    sales_amount=float(input('Enter Sales Amount: '))
    hours_worked=float(input('Enter Hours Worked: '))
    hourly_pay=hours_worked * HOURLY_PAY_RATE
    commission=sales_amount * COMMISSION_RATE
    gross_pay=hourly_pay + commission
    withholding=gross_pay * WITHHOLDING_RATE
    net_pay=gross_pay - withholding
    display_results(hourly_pay, commission, gross_pay, withholding, net_pay)
    print()
    input('Press ENTER to continue...')

def display_message():
    print("This program calculates the salesperson's pay.")
    print()
    print('Five values are displayed.\n')
    print('Hourly Pay, Commission, Gross Pay, Withholding, and Net Pay.')
    print()

def display_results(hourly_pay, commission, gross_pay, withholding, net_pay):
    print('Hourly Pay: ',format(hourly_pay,'.2f'))
    print('Commission: ',format(commission, '.2f'))
    print('Gross Pay: ',format(gross_pay, '.2f'))
    print('Withholding: ',format(withholding, '.2f'))
    print('Net Pay: ',format(net_pay, '.2f'))

main()
