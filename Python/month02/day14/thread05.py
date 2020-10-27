"""
    Event
"""
from threading import Event

e = Event()
print(e.wait(5))
e.set()
print(e.wait())
e.clear()
print(e.wait(5))