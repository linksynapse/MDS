# API 서버 인터페이스 목록


## 단말기 정보 요청
Address :
    
    GET /gda

Params :
### 요청

    {
        'DeviceId':'[CPUID]',
        'version':'1.210810.01'
    }

### 응답
    
    {
        'DeviceId':'[CPUID]',
        'Serial':'B21A001',
        'NeedUpdate':false,
        'TFTPUpdateRoot':'/'
    }


## 단말기 초기화 정보 요청
Address :

    GET /gd2i

Params :
### 요청

    {
        'Serial':'BB21A001'
    }

### 응답

    {
        'ProjectSiteName':'WBS A',
        'ProjectSiteCode':'PJT_001'
    }