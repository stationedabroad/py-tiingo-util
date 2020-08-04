import uvicorn

PORT = 8000
HOST = "127.0.0.1"

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': b'programatic tiingo started ...\n',
    })

if __name__ == '__main__':
    uvicorn.run(f"basic_prog:app", host=HOST, port=PORT, log_level="info")    