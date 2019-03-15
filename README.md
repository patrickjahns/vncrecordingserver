
📼💻  vncrecordingserver
========================

Provides a simple HTTP Api to remote control recording a vnc stream. 


## Installation

via pip/setuptools:

```
pip install git+git://github.com/patrickjahns/vncrecordingserver.git --process-dependency-links 
```

note: `--process-dependency-links` is required to install the correct version of [vnc2flv](https://github.com/patrickjahns/vnc2flv)

## Usage

### Start a recording

A recording can be started by issuing a `POST` to the endpoint `/recodring`.

Following options can be passed via the body:

- `filename`  
filename of the recording ( defaults to: `out%Y%m%d%H%M.flv`)

- `output_path`  
the path where the recording will be saved ( defaults to the current working directory of the server )

- `host`  
ip/dns of the vnc server ( default `localhost`)

- `port`  
port of the vnc server (default: `5900` )

- `password`  
password for connecting to the vnc server

- `framerate`  
framerate for the recording

- `keyframe`  
define after which amount of frames a keyframe will be inserted

- `clipping`  
specific the clipping rectangle in the form of `widthxheight+left+top` ( example: `400x300+120+0` )

- `debug`  
will output the debug information ( on the server ) provided by vnc2flv library

- example:  

```
curl -X POST \
  http://localhost:5000/recording \
  -H 'Content-Type: application/json' \
  -d '{
	"blocksize": 32,
	"clipping": null,
	"debug": false,
	"filename": "recording-name.flv",
	"framerate": 12,
	"host": "localhost",
	"keyframe": 120,
	"output_path": ".",
	"password": "secret",
	"port": 5900,
	"preferred_encoding": [
    	0,
    	-232,
    	-239
	]
}'
```



### Stop recording

A recording can be stopped by issuing a `DELETE` to the endpoint `/recodring`

- example:

```
curl -X DELETE http://localhost:5000/recording
```

### Get recording information

Information on the recording (server) can be fetched by issuing `GET` to the endpoint `/recodring`


Example:
```
curl -X GET http://localhost:5000/recording
```

The response contains information, wether or not a recording is currently running ( `active: true/false`) and the information on the recording ( `filename`, `host` ....)

```
{
    "active": false,
    "config": {
        "blocksize": 32,
        "clipping": null,
        "debug": false,
        "filename": "out201903152046.flv",
        "framerate": 12,
        "host": "localhost",
        "keyframe": 120,
        "output_path": ".",
        "password": null,
        "port": 5900,
        "preferred_encoding": [
            0,
            -232,
            -239
        ]
    }
}
```

## Testing



 - starting the recordingserver
```
python -m vncrecordingserver
```

- have a vnc server (example with selenium containers)
```
docker run --rm -p 5900:5900 selenium/standalone-chrome-debug
```
- start a recording
```
curl -X POST \
  http://localhost:5000/recording \
  -H 'Content-Type: application/json' \
  -d '{"password": "secret"}
```

- stop the recording
```
curl -X GET \
  http://localhost:5000/recording 
```


## Issues, Feedback and Ideas

Open an [Issue](https://github.com/patrickjahns/vncrecordingserver/issues)


## Contributing

Fork -> Patch -> Push -> Pull Request


## Authors

* [Patrick Jahns](https://github.com/patrickjahns)


## License

MIT


## Copyright
Copyright (c) 2018 Patrick Jahns <github@patrickjahns.de>

## Credits
Yusuke Shinyama - for the [original vnc2flv implementation](http://www.unixuser.org/~euske/python/vnc2flv/index.html)