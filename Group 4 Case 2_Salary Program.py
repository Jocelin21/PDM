def salary_program(hourly_overtime_rate = 110000, monthly_basic_salary = 3800000):
    while True:   
        try:
            overtime = float(input("Total overtime per month(hours): "))

            while overtime < 0:
                print("Please input a positive number.")
                overtime = float(input("Total overtime per month(hours): "))

        except ValueError: 
            print("Please input a positive number.")

        else:
            #Max overtime = 20 per month
            if overtime > 20:
                print("Maximum overtime is 20 hours per month.")
                overtime = 20

            while True:
                try:
                    allowance_level = int(input("Allowance level (1-3): "))

                    while allowance_level < 1 or allowance_level > 3:
                        print("Please choose the allowance level from 1-3.")
                        allowance_level = int(input("Allowance level (1-3): "))

                except ValueError: 
                    print("Please choose the allowance level from 1-3.")

                else:
                    #Allowance percentage = Level 1 = 5%, Level 2 = 1%, Level 3 = 15%}
                    allowance_list = [.05, .10, .15]

                    allowance = allowance_list[allowance_level-1] * monthly_basic_salary
                    overtime_salary = overtime * hourly_overtime_rate
                    total_salary = overtime_salary + monthly_basic_salary + allowance

                    print("-----------------------------------")
                    print(f"Total Overtime Counted: {overtime} hours")
                    print(f"Monthly Basic Salary: ${'{:,.2f}'.format(monthly_basic_salary)}")
                    print(f"Monthly Overtime Salary: ${'{:,.2f}'.format(overtime_salary)}")
                    print(f"Allowance Level: {allowance_level}")
                    print(f"Monthly Allowance: ${'{:,.2f}'.format(allowance)}")
                    print(f"Total Monthly Salary: ${'{:,.2f}'.format(total_salary)}")
                    break
            break


salary_program()