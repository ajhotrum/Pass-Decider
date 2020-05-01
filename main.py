from Ikon import Ikon
from Epic import Epic

#########################################
# TODO:   Add perks
#         Sum total prices
#         Concantinate dataframes
#########################################

if __name__ == "__main__":
    college = None

    ikon = int(input("Do you want an Ikon Pass? (0 for no, 1 for yes) " ))
    if ikon:
        base_plus=0
        base = int(input("Full or Base pass? (0 for full, 1 for base) "))

        renew = int(input("Did you have an Ikon Pass last season? (0 for no, 1 for yes) "))

        if base != 0:
            base_plus = int(input("Would you like the Ikon Base Plus pass? (0 for no, 1 for yes) "))

        college = int(input("Are you a Nurse/Military/College person? (0 for no, 1 for yes) "))

        insurance = int(input("Do you want pass insurance? (0 for no, 1 for yes) "))

        ikon1 = Ikon(base, renew, insurance, college, base_plus)

        print(ikon1.make_days_grid())
        print(f"\nIkon Cost: ${ikon1.price}")
        print(f"\nIkon Blackout Dates: {ikon1.blackout_dates}")
        print(f"Ikon Perks: {ikon1.perks}\n")
        print(f"Ikon Price hike on {ikon1.price_hike}\n")


    epic = int(input("Do you want an Epic Pass? (0 for no, 1 for yes) "))
    if epic:
        choice = int(input('Which pass are you interested in? (Enter a number between 1-4)'\
                            '\n1: Epic Full\n2: Epic Local\n3: Epic Local College'\
                            '\n4: PC Youth (applies to students of all ages)\n'))

        if choice ==1:
            base = False
            college= False
            youth = False
        elif choice == 2:
            base = True
            college = False
            youth = False
        elif choice == 3:
            base = False
            college = True
            youth = False
        elif choice == 4:
            base = False
            college = False
            youth = True

        epic1 = Epic(base, college, youth)

        print(epic1.make_days_grid())
        print(f"\nEpic Cost: ${epic1.price}")
        print(f"\nEpic Blackout Dates: {epic1.blackout_dates}")
        print(f"Epic Perks: {epic1.perks}\n")
        print(f"Epic Price hike on {epic1.price_hike}\n")
