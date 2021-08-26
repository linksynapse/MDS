# API 서버 인터페이스 목록


## 단말기 정보 요청 (사용안함)
Address :
    
    POST /2E1E9B5D6B3E378F81FB2706BDE8AE3D

Params :
### 요청

    {
        'DeviceId':'[CPUID]',
        'Version':'1.210810.01'
    }

### 응답
    
    {
        'Result':0,
        'Data':[{
            'DeviceId':'[CPUID]',
            'Serial':'B21A001',
            'NeedUpdate':false,
            'TFTPUpdateRoot':'/'
        }]
    }


## 단말기 초기화 정보 요청
Address :

    POST /4CF2C6704161CB5C3DCB0FFE9A52B4EC

Params :
### 요청

    {
        'cpu_id':'F0000002CPUID'
    }

### 응답

    {
        'Result':0,
        'Data':[{
            'cpu_id':'F0000002CPUID',
            'gant_id':'PJT_001',
            'gant_name':'BTS-200DR',
            'proj_id':'01',
            'proj_name':'WBS A',
            'status':'IN',
            'serial':'BB21A001'
        }]
        
    }


## 단말기 계정 정보 요청
Address:

    POST /C8CDC5F3D46143B664D72D039B5832FC

Params :
### 요청

    {
        'serial':'BB21A001'
    }

### 응답
    #### 쿼리 존재 시
    {
        'Result':0,
        'Data':[{
            'user_id':'01',
            'user_name':'USER_000',
            'card_id':'01',
            'card_name':'01234567',
            'com_id':'01',
            'com_name':'BLUZEN',
        }]
    }

    #### 쿼리 미존재 시
    {
        'Result':-1,
        'Data':[{
            'MsgCode':0x10FF,
            'Message':'No Record'
        }]
    }

## 단말기 히스토리 정보 전송
Address:

    POST /57C5A9EEA786CD47EE17D720420493FA

Params :

    {
        "gant_id":"01",
        "gant_name":"BTS-200DR",
        "serial":"BB21A001",
        "proj_id":"01",
        "proj_name":"WBS A",
        "status":"IN",
        "data":[{
            "user_id":"01",
            "user_name":"USR_000",
            "card_id":"08",
            "card_name":"01234567",
            "com_id":"01",
            "com_name":"BLUZEN",
            "created_on":"2021-08-12T:14:35:58.641Z"
        }]
    }

### 응답
    #### 쿼리 정상 입력 시
    {
        'Result':0,
        'Data':[{
            'MsgCode':0x2001,
            'Message':'Upload Succeed'
        }]
    }

## 단말기 생존 여부 파악
Address:

    POST /82D5984C2A2AD4C62CAF1DD073B1C91C

Params :

    {
        'Serial':'BB21A001'
        'Data':[{
            'status_Xdemon':[{
                'AcDSys':{
                    'KeepAlive':True,
                    'Uptime':'2016-10-27T17:13:40Z'
                },
                'HiUSys':{
                    'KeepAlive':True,
                    'Uptime':'2016-10-27T17:13:40Z'
                },
                'ReXec':{
                    'KeepAlive':True,
                    'Uptime':'2016-10-27T17:13:40Z'
                },
                'AlUSys':{
                    'KeepAlive':True,
                    'Uptime':'2016-10-27T17:13:40Z'
                }
            }]
        }]
    }

### 응답
    #### 정상 응답
    {
        'Result':0,
        'Data':[{
            'MsgCode':0x3000,
            'Message':'Update Succeed'
        }]
    }