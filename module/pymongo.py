from module import mongo
from pymongo.cursor import CursorType

def find_gentry_information(cpu_id):
    result = []
    data = mongo["acs"]["gantries"].find({"cpu_id":cpu_id}, {"_id":False},no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)

    for x in data:
        result.append(x)

    return result

def insert_history_information(values):
    result = mongo["acs"]["inout_records"].insert_many(values).inserted_ids
    return result