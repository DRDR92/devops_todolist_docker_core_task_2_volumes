from flask import Flask, Response, send_file
import os

app = Flask(__name__)

# Access the environment variable
appEnv = os.environ.get("APP_ENV", "Development")

# Initialize the counter from a file or set it to 0 if the file doesn't exist
counter_file = "data/counter.txt"

def read_counter():
   try:
       with open(counter_file, "r") as file:
           return int(file.read())
   except FileNotFoundError:
       return 0

def write_counter(counter):
   with open(counter_file, "w") as file:
       file.write(str(counter))

counter = read_counter()

@app.route('/')
def hello():
   global counter
   counter += 1
   write_counter(counter)
   return f'''
   Docker is Awesome! My ENV var is: {appEnv}<br>
   Page reload count: {counter}<br>
<pre>                   ##        .</pre>
<pre>             ## ## ##       ==</pre>
<pre>          ## ## ## ##      ===</pre>
<pre>      /""""""""""""""""\___/ ===</pre>
<pre> ~~~ (~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===-- ~~~</pre>
<pre>      \______ o          __/</pre>
<pre>        \    \        __/</pre>
<pre>         \____\______/</pre>
   '''

@app.route('/logo')
def docker_logo():
   return send_file('docker-logo.png', mimetype='image/png')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
