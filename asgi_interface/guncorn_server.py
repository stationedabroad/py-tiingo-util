def app(env, start_response):
    data = b"Tiingo Gunicorn server started! - version One\n"
    start_response("")
