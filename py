def main_menu():
    os.system('clear')
    title(com_name)
    heading('MAIN MENU')
    print('''\
\t1       -->     Admin Portal
\t2       -->     Customer Portal
\t3       -->     Credits
\n\tEnter   -->     Exit
    ''')
    ch = input('\n\tEnter the choice: ')
    if ch == '1':
        admin_authentication()
    elif ch == '2':
        customer_portal()
    elif ch == '3':
        credit()
        main_menu()
    else:
        program_end()
    return
  def customer_portal():
    os.system('clear')
    title(com_name)
    heading('CUSTOMER PORTAL')
    print('''\
\t1       -->     View Cars
\t2       -->     Rent Cars
\t3       -->     Return Cars
\n\tEnter   -->     Back
    ''')
    ch = input('\tEnter the choice: ')
    if ch == '1':
        view_cars_customer()
    elif ch == '2':
        rent_cars()
    elif ch == '3':
        return_cars()
    else:
        main_menu()
    return
