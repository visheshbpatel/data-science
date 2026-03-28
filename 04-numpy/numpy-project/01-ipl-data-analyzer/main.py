import analyzer


while True:

    print("\n====IPL Data Analyzer====")
    print("1. Total Runs")
    print("2. Average Runs")
    print("3. Highest Score")
    print("4. Best Player")
    print("5. Most Fifties")
    print("6. Exit")
    print("==========================\n")


    choice = input("Enter your Choice: ")


    if choice=="1":

        print("\nYou choose Total Runs\n")
        
        result = analyzer.total_runs()

        print(f'{"Player":<15} {"Runs"}')
        print("-"*20)


        for player,run in result.items():
            print(f'{player:<15} {run}')

    

    elif choice=="2":

        print("\nYou choose Average Runs\n")

        result = analyzer.average_run()

        print(f'{"Player":<15}{"Avg Runs"}')
        print("-"*23)

        for player,run in result.items():
            print(f'{player:<17} {run:.2f}')



    elif choice=="3":

        print("\nYou choose Highest Score\n")

        runs, player = analyzer.highest_score()

        print(f"Highest Score of {runs} by {player}")


    elif choice=="4":

        print("\nYou choose Best Player\n")

        result = analyzer.best_player()

        for i in result:
            print(i)


    elif choice=="5":

        result =analyzer.fifties()

        print(f'{"Player":<15} {"Fifties"}')
        print("-"*23)

        for player,run in result.items():
            print(f'{player:<15} {run}')



    elif choice=="6":

        print("\nThank you for using the Service")
        print("Exit.....\n")
        break


    else:
        print("\nInvalid choice")


    
    print("\nDo you want to continue")
    user_input = input("Press 'y' for Yes and 'n' for No: ").strip().lower()
    if user_input == 'y':
        continue
    
    elif user_input=='n':
        print("\nThank you for using the Service")
        print("Exit.....\n")
        break

    else:
        print("Wrong input")
        