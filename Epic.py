# Epic class
import pandas as pd
import numpy as np

class Epic:
    def __init__(self, base=False, college=False, youth=False):
        self.base = base
        self.college = college
        self.youth = youth
        self.perks = ['Free Pass Insurance', '16 Discount Tickets']
        self.price_hike = "9/7/20"

        self.get_price()
        self.set_blackouts()


    def get_price(self):
        if not self.youth:
            if self.base:
                self.price = 729
            if self.college:
                self.price = 659
            else:
                self.price = 979
                self.perks.append("No Blackout Dates")
                self.perks.append("Half off additional tickets when 7 days have been used.")

        else:
            self.price = 469 #nice
            self.perks.append("No Blackout Dates")


    def set_blackouts(self):
        # Set blackout dates
        if self.base:
            self.blackout_dates = "Nov 27-28, 2020,\n\t\t2020 Dec 26-31, 2020\n\t\tJan 16, 2021\n\t\tFeb 13-14, 2021\n"
        else:
            self.blackout_dates = "None\n"


    def make_days_grid(self):
        destinations = np.array(['Breckenridge, CO','Keystone, CO',
                                'Crested Butte, CO','Stevens Pass, WA',
                                'Heavenly, CA/NV', 'Northstar, CA',
                                'Kirkwood, CA', 'Park City, UT',
                                "Vail, CO", 'Beaver Creek, CO',
                                'Whistler Blackcomb, BC',
                                'Snowbasin, UT', 'Sun Valley ID',
                                'Telluride, CO'])

        if not self.youth:
            if self.base or self.college:
                destinations = destinations[:-1]
                split = 8
                days = np.full_like(destinations, "Ultd")
                days[split:] = 10
                days[-2:] = 2

            else:
                split = 11
                days = np.full_like(destinations, "Ultd")
                days[split:] = 7

        else:
            destinations = ['Park City, UT']
            days = ['Ultd']

        if self.base or self.college:
            blackouts = np.full_like(destinations, "NO")
            blackouts[4:] = 'Yes'
        else:
            blackouts = np.full_like(destinations, "NO")



        self.dates_pd = pd.DataFrame()
        self.dates_pd['Destinations'] = destinations
        self.dates_pd['Days'] = days
        self.dates_pd['Blackouts'] = blackouts

        return self.dates_pd
