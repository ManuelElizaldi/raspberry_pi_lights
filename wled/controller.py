# http://192.168.0.131/
import requests

wled_ip = '192.168.0.131'

def send_command_to_wled(data):
    try:
        response = requests.post(f"{wled_ip}/json/state", json = data, timeout = 3)
        return {"status" : "Okay", "response": response.json()}
    
    except Exception as e:
        return {"status":"error", "response":str(e)}