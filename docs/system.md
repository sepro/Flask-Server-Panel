# System details

Disk space, swap space, available momory, the cpu temperature and running
processes can be found under the different sections of system.

## Disk space **/api/system/disk/space**
```javascript
[
    {
        "device": "/dev/root",
        "fstype": "ext4",
        "mountpoint": "/",
        "opts": "rw,noatime,data=ordered",
        "usage": {
            "free": 28488658944,
            "percent": 5.0,
            "total": 31341383680,
            "used": 1551548416
        }
    },
    {
        "device": "/dev/mmcblk0p1",
        "fstype": "vfat",
        "mountpoint": "/boot",
        "opts": "rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,errors=remount-ro",
        "usage": {
            "free": 41066496,
            "percent": 34.7,
            "total": 62857216,
            "used": 21790720
        }
    }
]
```

## Swap space **/api/system/swap/**
```javascript
{
    "free": 104853504,
    "percent": 0.0,
    "sin": 0,
    "sout": 0,
    "total": 104853504,
    "used": 0
}
```

## Memory (RAM) **/api/system/memory/**
```javascript
{
    "active": 232407040,
    "available": 855552000,
    "buffers": 52924416,
    "cached": 157040640,
    "free": 645586944,
    "inactive": 50503680,
    "percent": 11.8,
    "total": 970485760,
    "used": 324898816
}
```

## Temperature details **/api/system/temp/**
```javascript
{
    "cpu": 43.312
}
```

## Processes running **/api/system/processes**
```javascript
[
    {
        "cpu_percentage": 0.1,
        "name": "RTW_CMD_THREAD",
        "pid": 354
    },
    {
        "cpu_percentage": 0.1,
        "name": "php-cgi",
        "pid": 755
    },
    
    ...
    
    {
        "cpu_percentage": 0.0,
        "name": "kworker/0:0",
        "pid": 28136
    }
]    
```