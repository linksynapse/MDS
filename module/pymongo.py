from module import mongo
from pymongo.cursor import CursorType
import datetime

def find_gentry_information(cpu_id):
    result = []
    data = mongo["acs"]["gantries"].find({"cpu_id":cpu_id}, {"_id":False})

    for x in data:
        result.append(x)

    return result

def find_users_information(proj_id):
    result = []
    data = mongo["acs"]["users"].aggregate([{"$match":{
            'proj_id_perm':proj_id, 
            'access':'Allowed', 
            'card_status':'Used', 
            'expiry_date':{
                "$gte":datetime.datetime.now()
            }
        }
            },{
            "$project":{
                "_id":0,
                "card_id":"Not Used",
                "user_id":"$user_id",
                "user_name":"$name",
                "com_id":"$com_id_main",
                "com_name":"$com_name_main",
                "card_name":"$card_number"
            }
        }])

    for x in data:
        result.append(x)

    return result

def insert_history_information(values):
    result = mongo["acs"]["inout_records"].insert_many(values).inserted_ids
    return result