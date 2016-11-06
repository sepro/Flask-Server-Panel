# Flask-Server-Panel API 

The front-end constantly queries an API, you can have external apps
fetch details directly from there (in JSON). The api can be accessed at
<your_panel_url>/api/ . The whole API is read-only and only GET requests
are supported.

## API entry point **/api/**

```javascript
{
    "network": {
        "external": "/api/network/external",
        "io": "/api/network/io"
    },
    "pihole": {
        "stats": "/api/pihole/stats"
    },
    "server": {
        "hostname": "/api/server/hostname",
        "os": "/api/server/os",
        "uptime": "/api/server/uptime"
    },
    "system": {
        "disk_space": "/api/system/disk/space",
        "memory": "/api/system/memory",
        "processes": "/api/system/processes",
        "swap": "/api/system/swap",
        "temp": "/api/system/temp"
    },
    "version": "/api/version"
}
```

The entry point should be rather self-explanatory, it contains links to
more detailed sections of the API.

This documentation is valid for version 1.0 which can be checked at **/api/version/**

```javascript
{
    "name": "Flask-Sever-Panel",
    "version": "1.0"
}
```

## Details for subsections

  * [Network](./network.md)
  * [PiHole](./pihole.md)
  * [Server](./server.md)
  * [System](./system.md)
  
  
  
  
