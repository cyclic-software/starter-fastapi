# FastAPI Starter

This is the simplest possible python FastAPI app that responds with: 
```
{"message": "Hello World"}
```

## Deploy to Cyclic in seconds 

[![Deploy to Cyclic](https://deploy.cyclic.app/button.svg)](https://deploy.cyclic.app/)

Set `server.py` as your entry point.

## Run Locally

Prerequisites:
- pyenv
- python 3.10.11

Install: `bin/install`
- creates virtual env
- installs dependencies from `requirements.txt`

Run: `bin/dev`
- runs a `uvicorn` server in reload mode

Run: `bin/start`
- runs a `uvicorn` server


## Try the server

Schema docs: [http://localhost:8181/docs](http://localhost:8181/docs)

Get an item:
`curl -i -XGET http://localhost:8181/item/1`

List items:
`curl -i -XGET http://localhost:8181/items/`

Post an item:
`curl -i -XPOST http://localhost:8181/items/ --data '{"item_id":1,"name":"Bob"}' -H 'content-type: application/json'`


## Questions / Help

Join us on Discord: [https://discord.cyclic.sh](https://discord.cyclic.sh)

Enjoy!
