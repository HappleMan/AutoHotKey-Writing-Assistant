from flask import Flask, request, jsonify, send_file
import requests

cloudflare_uid = ""
cloudflare_token = ""

apiBaseUrl = f"https://api.cloudflare.com/client/v4/accounts/{cloudflare_uid}/ai/run/"
headers = {"Authorization": cloudflare_token}
model = "@cf/meta/llama-2-7b-chat-int8"

app = Flask("Assistant")

def find_arg(req, argument):
    data = req.data
    args = req.args
    form = req.form
    for cont in [data, args, form]:
        try:
            if not cont is None and argument in cont:
                return cont[argument]
        except:
            print("rats!")

def llamaRequest(system, user):
    inputs = { 
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    }
    response = requests.post(f"{apiBaseUrl}{model}", headers=headers, json=inputs)
    return response.json()
    
@app.route("/llama", methods=["GET","POST"])
def run_llama():
    sys = find_arg(request, "system")
    usr = find_arg(request, "user")
    if not sys is None and not usr is None:
        try: 
            resp = llamaRequest(sys, usr)
            return resp["result"]["response"], 200
        except:
            return jsonify({
                "response": "Your request caused an error."
            }), 400
    return jsonify({
        "response": "There was an error. Check for missing payload."
    }), 400
    
if __name__ == "__main__":
    app.run()