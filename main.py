from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/user",methods=["GET"])
def user():
   args = request.args
   return jsonify(args=dict(args))

@app.route("/url",methods=["GET"])
def url():
   return jsonify(url=request.url)

@app.route("/url/<prmt>", methods=["GET"])
def parametre(prmt):
   return jsonify(prmt)

@app.route("/header",methods=["GET"])
def header():
   headers=request.headers
   return jsonify(header=dict(headers))

@app.route("/body", methods=["POST"])
def body():
    if(request.data):
        data=request.json
        return jsonify(data)
    else:
        return "The request hasn't data",405

if __name__=="__main__":
    app.run(debug=True)