
#exe 1:

class Time(object):
    '''
    Time class , receive hour and minute
    '''
    def __init__(self, h, m):
        self.hour = h
        self.minute = m
    def __str__(self):
        if self.hour > 9:
            if self.minute < 9:
                return '{}:0{}'.format(self.hour,self.minute)
            else:
                return f'{self.hour}:{self.minute}'
        else:
            if self.minute > 9:
                return f'0{self.hour}:{self.minute}'
            else:
                 return f'0{self.hour}:0{self.minute}'

    def __repr__(self):
        return ('Time({},{})'.format(self.hour , self.minute))


class Event(object):
    """
    Event Class , receive Time object and name
    """
    def __init__(self, time, name):
        self.time = time
        self.name = name
    def __str__(self):
        return '{} - {}'.format(self.time,self.name)
    def __repr__(self):
        return "Event({},'{}')".format(self.time.__repr__(),self.name)


class MedicalRecord(object):
    """
    Medical Record Class , receive name and id ,can add events and view them with Class Methods
    """
    def __init__(self ,patientname ,id):
        self.patientname = patientname
        self.id = id
        self.data = {}

    def __repr__(self):
        return "MedicalRecord('{}',{},{})".format(self.patientname,self.id,self.data)

    def add(self,time , event):
        txt = time.split(":")
        first = int(txt[0])
        second = int(txt[1])
        self.data[time] = Event(Time(first,second),event)


    def view(self):
        sorted(self.data)
        print("name: ",self.patientname)
        print("ID: ",self.id)
        for key in self.data:
            print(self.data[key])



'''time1 = Time(8,2)
print(time1)
time2 = eval(repr(time1))
print(time2)
event1 = Event(time1, 'registration')
print(event1)
print(repr(event1))
event2 = eval(repr(event1))
print(event2)
record1 = MedicalRecord('David',1)
record1.add('08:02','registration')
print(record1)
record1.add('09:15','doctor checkup')
record1.add('08:45','doctor checkup')
record1.add('09:00','procedure')
record1.add('11:00','doctor checkup')
record1.add('09:25','radiography')
record1.add('11:30','hospital discharge')
record1.add('10:30','blood test')
record1.view()
print(record1)
'''


#exe 2:


