from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
import logging
import requests
from datetime import datetime as dt

# setup Flask app
app = Flask(__name__, static_path='', static_folder='', template_folder='')
app.config['SERVER_NAME'] = "arockhub.com"

# routing dictionary
routing = {"movie": "130.204.58.113:3127",
           "finance": "localhost:3126",
           "memory": "localhost:3122",
           "paint": "localhost:3121",
           "www": "arockhub.com"}  #  <- main ip


# Ensure responses aren't cached on your browser.
# Useful while still making changes to your front end.
# You can delete this block once the project is finished.
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'max-age=300'
    return response


# When someone accesses "/" returns the index.html file in the teamplate folder
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', defaults={'path': ''}, subdomain='<target>', methods = ['POST', 'GET'])
@app.route('/<path:path>', subdomain='<target>', methods = ['POST', 'GET'])
def target_subdomain(target, path):
    return _proxy(target, path)


#  from: https://stackoverflow.com/questions/6656363/
#        proxying-to-another-web-service-with-flask?utm_medium=organic&
#        utm_source=google_rich_qa&utm_campaign=google_rich_qa
def _proxy(*args, **kwargs):
    old_domain = args[0] + '.' + app.config['SERVER_NAME']
    new_domain = routing[args[0]]

    resp = requests.request(
        method=request.method,
        url=request.url.replace(old_domain, new_domain),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response


# Run the program
if __name__ == "__main__":
    logfile = 'access' + str(dt.now().day) + '.log'
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler(logfile)
    logger.addHandler(handler)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=3120, threaded=True, debug=False)
