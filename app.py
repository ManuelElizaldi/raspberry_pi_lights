from flask import Flask, render_template, request, jsonify
from wled.controller import send_command_to_wled

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/wled', methods = ['POST'])
def control_wled():
    data = request.json
    result = send_command_to_wled(data)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)