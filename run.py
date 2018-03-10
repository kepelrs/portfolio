from flask import Flask, render_template, request, jsonify, redirect, url_for
import logging
from datetime import datetime as dt

# setup Flask app
app = Flask(__name__, static_path='', static_folder='', template_folder='')
app.config['SERVER_NAME'] = "arockhub.com"

# routing dictionary
routing = {"movie": "130.204.58.113:3127",
           "finance": "130.204.58.113:3126",
           "www": "arockhub.com"}


# Ensure responses aren't cached on your browser.
# Useful to see the changes you have made to your front end.
# You can delete this block once the project is finished.
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'max-age=300'
    return response


# When someone accesses "/" returns the index.html file in the teamplate folder
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/', subdomain='<target>')
def target_subdomain(target):
    return redirect("http://" + routing[target])


# Run the program
if __name__ == "__main__":
    logfile = 'access' + str(dt.now().day) + '.log'
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler(logfile)
    logger.addHandler(handler)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=3120, threaded=True, debug=False)
