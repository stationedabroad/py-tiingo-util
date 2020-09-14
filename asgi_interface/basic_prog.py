import uvicorn
from requests.status_codes import codes

# host info
PORT = 8000
HOST = "127.0.0.1"
OK = 200

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': codes.ALL_OK, # 200
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': bytes('programatic tiingo started ...\n', encoding='utf-8'),
    })

if __name__ == '__main__':
    uvicorn.run(f"basic_prog:app", host=HOST, port=PORT, log_level="info")    
