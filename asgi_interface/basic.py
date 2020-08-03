

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    print(f" Scoep param details ==> {scope}")
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': b'tiingo started ...\n',
    })