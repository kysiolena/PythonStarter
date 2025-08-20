import uuid

employees = dict()

'''
    «Облік кадрів» 
    
    прізвище:

    посада: ...

    досвід роботи: …

    портфоліо: …

    коефіцієнт ефективності: …

    стек технологій: …

    зарплата: …
'''

while True:
    action = input(
        '1 - Add new employee \n'
        '2 - Edit employee \n'
        '3 - Remove employee \n'
        '4 - See list of employees \n'
        '5 - Exit \n'
        'Enter the number of the action you want to perform: \n'
    )

    try:
        action = int(action)
    except ValueError as e:
        print(e)
        print()

    match action:
        case 1:
            employee = dict.fromkeys(
                ['surname', 'position', 'experience', 'portfolio', 'efficiency_factor', 'tech_stack', 'wages'])

            for key in employee.keys():
                value = input(f'Enter {key} of employee: ')

                employee[key] = value if value else None

            employee_id = str(uuid.uuid4())
            employees[employee_id] = employee
        case 2:
            employee_id = input(f'Enter ID of employee for EDIT: ')

            if not len(employees):
                print('List of employees is empty yet')
            elif employee_id in employees.keys():
                employee = employees[employee_id]

                for key in employee.keys():
                    value = input(f'Enter new {key} of employee or press ENTER to skip this: ')

                    if value:
                        employee[key] = value
            else:
                print('Employee does not found')
        case 3:
            employee_id = input(f'Enter ID of employee for REMOVE: ')

            if not len(employees):
                print('List of employees is empty yet')
            elif employee_id in employees.keys():
                del employees[employee_id]
            else:
                print('Employee does not found')
        case 4:
            sort_by = input('Sort by (\'default\', \'surname\', \'efficiency_factor\'): ')

            if not len(employees):
                print('List of employees is empty yet')
            elif sort_by in ['surname', 'efficiency_factor']:
                print(dict(sorted(employees.items(), key=lambda el: el[1][sort_by].lower())))
            else:
                print(employees)
        case 5:
            break
