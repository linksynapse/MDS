# API 서버 인터페이스 목록


## 단말기 정보 요청
Address :
    
    POST /2E1E9B5D6B3E378F81FB2706BDE8AE3D

Params :
### 요청

    {
        'DeviceId':'[CPUID]',
        'version':'1.210810.01'
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
        'Serial':'BB21A001'
    }

### 응답

    {
        'Result':0,
        'Data':[{
            'ProjectSiteName':'WBS A',
            'ProjectSiteCode':'PJT_001',
            'DeviceType':'IN',
            'Serial':'BB21A001'
        }]
        
    }


## 단말기 계정 정보 요청
Address:

    POST /C8CDC5F3D46143B664D72D039B5832FC

Params :
### 요청

    {
        'Serial':'BB21A001'
    }

### 응답
    #### 쿼리 존재 시
    {
        'Result':0,
        'Data':[{
            'CardNumber':'12345678',
            'UserId':'00001',
            'Name':'Eden'
        }]
    }

    #### 쿼리 미존재 시
    {
        'Result':-1,
        'Data':[{
            'Message':'No Record'
        }]
    }
    
    #### 서버 오류 시
    {
        'Result':-2,
        'Data':[{
            'MsgCode':0x1004,
            'Message':'Internel Server Error'
        }]
    }