def GetErrorMsg(result, msgcode, msg):
    Temp = {
        'Result':result,
        'Data':[{
            'MsgCode':msgcode,
            'Message':msg
        }]
    }
    return Temp

def GetRowsMsg(result, msgcode, msg):
    Temp = {
        'Result':result,
        'Data':[{
            'MsgCode':msgcode,
            'Message':msg
        }]
    }
    return Temp

def GetRowsData(result, data):
    Temp = {
        'Result':result,
        'Data':data
    }
    return Temp