from flask import Flask, render_template
from flask_socketio import SocketIO
from satellite import *
import pandas as pd
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_value(data):
    print("Message: ", data)

@socketio.on('view_status')
def handle_send_value(data):
    print("View status: ", data)
    socketio.emit('view_status', data)
    
@socketio.on('send_data')
def handle_send_value(data):
    data = pd.DataFrame(data)
    TLE_data = data.to_numpy()
    objects = {}
    objects["Names"] = TLE_data[0,:].tolist()
    objects["Colors"] = TLE_data[-1,:].tolist()
    print("Receive: ", objects)
    for i in range(np.shape(TLE_data)[1]):   
        sat = Satellite(*TLE_data[:9,i], NB_ORBITS=1, TIME_SIMU=1000)
        sat.future_it()
        print(sat.position.geografic.LON_LAT[:,0])
        objects[sat.NAME] = sat.position.inertial.XYZ.tolist()
    socketio.emit('receive_data', objects)
       
if __name__ == '__main__':
    print("Starting server on http://127.0.0.1:5000")
    socketio.run(app, host='127.0.0.1', port=5000)
