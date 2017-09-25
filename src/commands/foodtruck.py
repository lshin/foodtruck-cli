from .base import Base
from src import api
from datetime import datetime, timedelta

class FoodTruck(Base):
    """FoodTruck command"""

    def run(self):
        """
        Main method to get a food truck data and print
        """
        self.now = datetime.now()
        limit = int(self.options['--limit'])

        foodtruck_api = api.FoodTruckApi()

        self.data = sorted([{ 'applicant' : item['applicant'], 'location' : item['location'] } for item in foodtruck_api.get()
            if self._is_open(item['start24'], item['end24'], item['dayofweekstr'])], key=lambda x:x['applicant'], reverse=False)[:limit]

        self._print()

    def _print(self):
        """
        Formatting based on a max string of food truck name and print pretty.
        """
        max_str_lengh = max(len(item['applicant']) for item in self.data)
        # print header
        print 'NAME'.ljust(max_str_lengh + 1) + 'ADDRESS'
        #print items
        for item in self.data:
            print item['applicant'].ljust(max_str_lengh + 1) + item['location']

    def _is_open(self, start, end, scheduled_weekday):
        """
        Check a given start time and end time is in current time
        """
        now = self.now
        start_time = start.replace(':', '')
        end_time = end.replace(':', '')

        start_date = self._get_time(start_time)
        end_date = self._get_time(end_time)

        # not same day
        if now.strftime('%A') != scheduled_weekday:
            return False

        if start_time > end_time:
            end_date = datetime.strptime((now + timedelta(days=1)).strftime('%Y%m%d') + end_time, '%Y%m%d%H%M')

        return ( start_date <= now and now <= end_date )

    def _get_time(self, time):
        """
        Convert a time string into a datetime and if it's a '24:00', then it has to change into a next day '00:00' for matching a time format
        """
        if time == '2400':
            time = '0000'
            now_date = (self.now + timedelta(days=1)).strftime('%Y%m%d')
        else:
            now_date = self.now.strftime('%Y%m%d')
        return datetime.strptime( now_date + time, '%Y%m%d%H%M')