from module import mongo
from pymongo.cursor import CursorType

def find_serial(cpu_id):
    result = []
    data = mongo["acs"]["gantries"].find({"cpu_id":cpu_id}, {"_id":False, "gant_id":False, "proj_id":False, "status":False},no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)

    for x in data:
        x["NeedUpdate"] = False
        x["TFTPUpdateRoot"] = "/"
        result.append(x)

    return result

def find_gentry_information(serial):
    result = []
    data = mongo["acs"]["gantries"].find({"serial":serial}, {"_id":False, "gant_id":False},no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)

    for x in data:
        result.append(x)

    return result