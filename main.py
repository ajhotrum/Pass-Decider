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
        base_plus=0d
        base = int(input("Full or Base pass? (0 for full, 1 for base) "))

        renew = int(input("Did you have an Ikon Pass last season? (0 for no, 1 for yes) "))

        if base != 0:
            base_plus = int(input("Would you like the Ikon Base Plus pass? (0 for no, 1 for yes) "))

        college = int(input("Are you a Nurse/Military/College person? (0 for no, 1 for yes) "))

        insurance = int(input("Do you want pass insurance? (0 for no, 1 for yes) "))

        ikon1 = Ikon(base, renew, insurance, college, base_plus)

        print(ikon1.make_days_grid())
        print(f"\nCost: ${ikon1.price}")
        print(f"\nBlackout Dates: {ikon1.blackouts}")
        print("\nPerks: ??????????????")


    epic = int(input("Do you want an Epic Pass? (0 for no, 1 for yes)"))
    if epic:
        base = 0
        if college == None:
            college = int(input("Are you a student interested in a PC youth pass (for students of all ages)? (0 for no, 1 for yes) "))
        elif college == 1:
            college = int(input("You said you are a college student. Are you interested in a PC youth pass? (0 for no, 1 for yes) "))

        if not college:
            base = int(input("Do you want an Epic Full or Local pass? (0 for full, 1 for local) "))

        epic1 = Epic(base, college)

        print(epic1.make_days_grid())
