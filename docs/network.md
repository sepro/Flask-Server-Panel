# Network details **/api/network/external** and **/api/network/io**

Your exteral IP-address is determined using a third-party service 
[ipinfo.io](http://ipinfo.io/json) . It provides details about your IP,
the location associated with it and the provider.

```javascript
{
    "city": "",
    "country": "LU",
    "hostname": "provider",
    "ip": "127.0.0.1",
    "loc": "49.7500,6.1667",
    "org": "AS5577 root SA",
    "region": ""
}
```

The internal network returns the input and output from local adapters in your system.

```javascript
[
    {
        "address": "127.0.0.1",
        "device": "lo",
        "io": {
            "bytes_recv": 127141942,
            "bytes_sent": 127141942,
            "dropin": 0,
            "dropout": 0,
            "errin": 0,
            "errout": 0,
            "packets_recv": 331057,
            "packets_sent": 331057
        }
    },
    {
        "address": "unknown address",
        "device": "eth0",
        "io": {
            "bytes_recv": 0,
            "bytes_sent": 0,
            "dropin": 0,
            "dropout": 0,
            "errin": 0,
            "errout": 0,
            "packets_recv": 0,
            "packets_sent": 0
        }
    },
    {
        "address": "192.168.1.25",
        "device": "wlan0",
        "io": {
            "bytes_recv": 168206324,
            "bytes_sent": 1533878635,
            "dropin": 508579,
            "dropout": 1,
            "errin": 0,
            "errout": 0,
            "packets_recv": 1181401,
            "packets_sent": 4910834
        }
    }
]
```
