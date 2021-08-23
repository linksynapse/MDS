# API 서버 Result 값 정의

|Code|Description|
|----|-----------|
|0|Transaction succeed|
|-1|No record|
|-2|Invalid parameter|
|-3|Internal server error|
|-4|Internal client error|


# API 서버 Message Code 값 정의

|MsgCode(Upper) 1byte|MsgCode(Lower) 1byte|
|--------------------|--------------------|
|ex) 0x00010002|

|MsgCode(Upper)|Description|
|-------|-----------|
|0x10|Account|
|0x20|History|

## History Message Parameter
|MsgCode (1Byte)|Applied Query (1Byte)|Description|
|-------|--------|--------|
|0x20|01|1개 쿼리 적용|
|0x20|FF|255개 쿼리 적용|