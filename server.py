from flask import Flask, render_template
from flask_socketio import SocketIO
from satellite import *
import pandas as pd
import threading
import time
from datetime import datetime, timezone

app = Flask(__name__)
socketio = SocketIO(app)
should_shutdown = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_send_value(data):
    print('Client:', data)

@socketio.on('view_status')
def handle_view_status(data):
    print('Client:', data)
    socketio.emit('view_status', data)

@socketio.on('selected_status')
def handle_view_status(data):
    print('Client:', data)
    socketio.emit('selected_status', data)

@socketio.on('send_data')
def handle_send_data(data):
    data = pd.DataFrame(data)
    TLE_data = data.to_numpy()
    objects = {}
    objects["Names"] = TLE_data[0,:].tolist()
    objects["Colors"] = TLE_data[-4,:].tolist()
    for i in range(np.shape(TLE_data)[1]):   
        sat = Satellite(*TLE_data[:9,i], NB_ORBITS=1, TIME_SIMU_START=TLE_data[-2,:].tolist()[i], TIME_SIMU_END=TLE_data[-1,:].tolist()[i])
        sat.future_it()
        objects[sat.NAME] = sat.position.geoorbit.XYZ.tolist()
    socketio.emit('send_data', objects)

@socketio.on('send_data_live')
def handle_send_data(data):
    data = pd.DataFrame(data)
    TLE_data = data.to_numpy()
    objects = {}
    objects["Names"] = TLE_data[0,:].tolist()
    objects["Colors"] = TLE_data[-4,:].tolist()
    for i in range(np.shape(TLE_data)[1]):  
        sat = Satellite(*TLE_data[:9,i], NB_ORBITS=1, TIME_SIMU_START=TLE_data[-3,:].tolist()[i], TIME_SIMU_END=TLE_data[-3,:].tolist()[i])
        sat.future_it()
        objects[sat.NAME] = sat.position.geoorbit.XYZ.tolist()
    socketio.emit('send_data_live', objects)
    
@socketio.on('disconnect')
def handle_disconnect():
    global should_shutdown
    print("Server: Client disconnected")
    print("Server: Stoping server on http://127.0.0.1:5000")
    should_shutdown = True

def shutdown_server():
    socketio.stop() 

def check_shutdown():
    while True:
        if should_shutdown:
            shutdown_server()
            break
        time.sleep(1)

if __name__ == '__main__':
    shutdown_thread = threading.Thread(target=check_shutdown)
    shutdown_thread.start()
    print("Server: Starting server on http://127.0.0.1:5000")
    socketio.run(app, host='127.0.0.1', port=5000)
