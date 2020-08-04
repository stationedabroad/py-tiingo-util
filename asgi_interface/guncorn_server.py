

def app(env, start_response):
    data = b"Tiingo Gunicorn server started!\n"
    start_response("")