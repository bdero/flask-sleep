from flask import Flask
from time import sleep


app = Flask(__name__)

@app.route('/')
def instructions():
    return """
    <html><body>
    <h3>Go to `/[number]` to hang for `[number]` seconds.</h3>
    <p><a href="/5">5 Seconds</a></p>
    <p><a href="/15">15 Seconds</a></p>
    <p><a href="/30">30 Seconds</a></p>
    <p><a href="/60">60 Seconds</a></p>
    <p><a href="/120">120 Seconds</a></p>
    <p><a href="/300">300 Seconds</a></p>
    <p><a href="/600">600 Seconds</a></p>
    </body></html>
    """

@app.route('/<sleeptime>')
def do_sleep(sleeptime=None):
    try:
        sleep(float(sleeptime))
        return 'Successfully slept for {} seconds.'.format(sleeptime)
    except ValueError:
        return 'Error: Unable to convert "{}" into a float.'.format(sleeptime)

if __name__ == '__main__':
    app.run()
