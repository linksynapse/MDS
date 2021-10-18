from module import mongo
from pymongo.cursor import CursorType
import datetime

def find_gentry_information(cpu_id, nataddr, pubaddr, mac):
    result = []
    data = mongo["acs"]["gantries"].find({"cpu_id":cpu_id}, {"_id":False,'last_pubaddr':False,'last_login':False,'last_mac':False})
    mongo["acs"]["gantries"].update_one({"cpu_id":cpu_id}, {"$set":{"last_login":datetime.datetime.now(), "last_pubaddr":pubaddr, "last_nataddr":nataddr, "last_mac":mac}})

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