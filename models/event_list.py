from models.event import *
import datetime

event1 = Event(datetime.date(2022, 5, 17), "Wedding", 100, "Main Hall", "Mr and Mrs Smith", False)
event2 = Event(datetime.date(2021, 6, 18), "Birthday Party", 30, "Annexe","15 year old's birthday party", True)
event3 = Event(datetime.date(2022, 7, 19), "Business Conference", 200, "Conference Room", "Software Developer Convention", True)

events = [event1, event2, event3]

#   def __init__(self, date, name, guest_num, location, description):

def save_event(new_event):
    events.append(new_event)