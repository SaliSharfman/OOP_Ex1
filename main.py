from building import Building
from elavator import Elevators
import json
p =Building(0,0,[])
p.load_json("B5.json")
x= p.max_floor
print(x)

