# Epic class
import pandas as pd
import numpy as np

class Epic:
    def __init__(self, base=False, college=False):
        self.base = base
        self.college = college
        self.perks = ['Free Pass Insurance', '16 Discount Tickets']

        self.get_price()
        self.set_blackouts()


    def get_price(self):
        if not self.college:
            if self.base:
                self.price = 729
            else:
                self.price = 979
                self.perks.append("No Blackout Dates")
        else:
            self.price = 469 #nice
            self.perks.append("No Blackout Dates")


    def set_blackouts(self):
        # Set blackout dates
        if self.base:
            self.blackouts = "Nov 27-28, 2020,\n\t\t2020 Dec 26-31, 2020\n\t\tJan 16, 2021\n\t\tFeb 13-14, 2021\n"
        else:
            self.blackouts = "None\n"


    def make_days_grid(self):
        destinations = np.array(['Breckenridge, CO','Keystone, CO',
                                'Crested Butte, CO','Stevens Pass, WA',
                                'Heavenly, CA/NV', 'Northstar, CA',
                                'Kirkwood, CA', 'Park City, UT',
                                "Vail, CO", 'Beaver Creek, CO',
                                'Whistler Blackcomb, BC',
                                'Snowbasin, UT', 'Sun Valley ID',
                                'Telluride, CO'])

        if not self.college:
            if not self.base:
                split = 11
                days = np.full_like(destinations, "Ultd")
                days[split:] = 7


            if self.base:
                destinations = destinations[:-1]
                split = 8
                days = np.full_like(destinations, "Ultd")
                days[split:] = 10
                days[-2:] = 2

        else:
            destinations = ['Park City, UT']
            days = ['Ultd']


        self.dates_pd = pd.DataFrame()
        self.dates_pd['Destinations'] = destinations
        self.dates_pd['Days'] = days

        return self.dates_pd
