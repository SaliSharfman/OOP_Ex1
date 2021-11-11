import json
from elavator import Elevators


class Building(object):
    def __init__(self, min_floor, max_floor, elvators):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elvators = elvators

    def load_json(self, file):
        elvator_list = []
        with open(file, "r")as f:
            d = json.load(fp=f)
            self.min_floor = d["_minFloor"]
            self.max_floor = d["_maxFloor"]
            for elev in d["_elevators"]:
                el = Elevators(_id=elev["_id"], speed=elev["_speed"], min_floor=elev["_minFloor"],
                               max_floor=elev["_maxFloor"],
                               close_time=elev["_closeTime"], open_time=elev["_openTime"],
                               start_time=elev["_startTime"],
                               stop_time=elev["_stopTime"])
                elvator_list.append(el)
            self.elvators = elvator_list

        return self

        p = Building()
        p = p.load_json("B1.json")
        x = p.elvators

