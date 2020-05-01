# Ikon class
import pandas as pd
import numpy as np

class Ikon:
    def __init__(self, base=False, renew=True, insurance=False, college=False, base_plus=False):
        self.base = base
        self.base_plus = base_plus
        self.renew = renew
        self.insurance = insurance
        self.college = college
        self.perks = ['Season Deferal (decide between 9/10-12/10/2020)']
        self.price_hike = "5/27/20"

        self.get_price()
        self.set_blackouts()


    def get_price(self):
        #Check if in college
        if not self.college:
            # Check base/full and renewal
            if not self.base and not self.renew:
                self.price = 1000
            elif not self.base and self.renew:
                self.price = 799
            elif self.base and not self.renew:
                self.price = 700
            else:
                self.price = 600

        # If in college
        else:
            if self.base:
                self.price = 529
            else:
                self.price = 709

        # Add Perks
        if self.base:
            self.perks.append("25% off 8 buddy tickets (at participating mountains)")
        else:
            self.perks.append("25% off 10 buddy tickets (at participating mountains)")

        # Add insurance
        if self.insurance:
            if self.base:
                self.price += 42
            else:
                self.price += 60

        # Add for base plus
        if self.base_plus:
            self.price += 150


    def set_blackouts(self):
        # Set blackout dates
        if self.base:
            self.blackout_dates = "Dec 26, 2020 – Jan 2, 2021 \n\t\tJan 16-17, 2021 \n\t\tFeb 13-14, 2021\n"
        else:
            self.blackout_dates = "None\n"





    def make_days_grid(self):
        destinations = np.array(["Copper Mountain, CO",
                      "Squaw, CA", 'JUNE MOUNTAIN, CA',
                      "Solitude, UT", 'WINTER PARK, CO',
                      'ELDORA MOUNTAIN RESORT, CO', 'MAMMOTH MOUNTAIN, CA',
                      'BIG BEAR, CA', 'CRYSTAL MOUNTAIN, WA',"Steamboat, CO",
                      'Snoqualmie, WA', 'SKIBIG3, AB',
                      'Cypress Mountain, BC', 'Taos, NM', "Brighton, UT",
                      "Arapahoe Basin, CO", "Big Sky, MT", "MT Bachelor, OR",
                      "Revelstoke, BC", "Deer Valley (BOOOOOOOOOO!)",
                      "Alta Snowbird, UT",'Aspen, CO', 'Jackson Fuckin Hole'])

        if self.base and not self.base_plus:
            destinations = destinations[:-2]

        split = 10
        if self.base:
            split = 9

        limited_days = 7
        if self.base:
            limited_days = 5

        # Set blackouts for base pass destinations
        blackouts = np.full_like(destinations, "No")
        if self.base:
            blackouts = np.full_like(destinations, "Yes")
            elements = [0,4,5,7,8]
            for i in elements:
                blackouts[i] = Yes

        days = np.full_like(destinations, "Ultd")
        days[split:] = limited_days

        self.dates_pd = pd.DataFrame()
        self.dates_pd['Destinations'] = destinations
        self.dates_pd['Days'] = days
        self.dates_pd['Blackouts'] = blackouts

        return self.dates_pd
