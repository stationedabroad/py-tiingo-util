from requests.status_codes import codes

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    print(f" Scoep param details ==> {scope}")
    await send({
        'type': 'http.response.start',
        'status': codes.ALL_OK,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': b'tiingo started ...\n',
    })