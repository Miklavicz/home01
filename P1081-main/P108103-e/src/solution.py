# TODO
import sys
from typing import NamedTuple

Airport=NamedTuple("print_Airport",[
    ("name",str),
    ("city",str),
    ("runaways",int),
    ("time",int)
])
def from_line(line:str)->Airport:
    tokens=line.strip().split(";")
    return Airport(tokens[0],tokens[1],tokens[2],tokens[3])

def to_line(airport:Airport)->Airport:
    return f"{airport.name} {airport.city} {airport.time}"


def order(airports:list[Airport])->list[Airport]:
    return sorted(airports, key=lambda a:(-a.runaways,-a.time,a.name))

def main():
    airports=[]
    for line in sys.stdin:
        airports.append((from_line(line)))
    rendez=order(airports)
    for a in rendez:
        print(to_line(a))

if __name__=="__main__":
    main()