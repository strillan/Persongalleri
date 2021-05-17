from datetime import date, datetime, time, timedelta
from pickle import Unpickler
from pickle import Pickler
import itertools

class Storage:
    def __init__(self):
        #self.path = '..\\___data___\\'
        self.FILE_NAME = 'persongalleri.p'
        self.today = date.today()

    def retrieve(self):
        data = []
        with open(self.FILE_NAME, 'rb') as file:
            try:
                while True:
                    line = Unpickler(file).load()
                    data.append(line)
            except EOFError:
                pass
        return data

    def insert(self, text):
        line = {'date': self.today, 'text': text}
        with open(self.FILE_NAME, 'ab') as file:
            Pickler(file).dump(line)
        print(self.retrieve())
        return line

    """ 
    def examples_sorting_and_grouping(self):
        data = self.retrieve()
        data.sort()
        clarity_week = []
        clarity = []
        clarity_week.sort(key=lambda i: (i['date'], i['category']))
        clarity_week.sort(key=lambda i: (i['date'], i['clarity']))
        clarity_groups = itertools.groupby(clarity_week, lambda j : (j['date'], j['clarity']))
        for line in clarity_groups:
            obj = {
                'date' : line[0][0],
                'clarity': line[0][1],
                'hours': sum([row['hours'] for row in line[1]])
            }
            clarity.append(obj)
        return clarity
    """ 
