from flask import Flask,jsonify,request
app = Flask(__name__)

tasks = [
    {
        "id":1 ,
        "name":u'Raju',
        "contact":u"371-552-5265",
        "done":False,
    },
    {
        "id":2 ,
        "name":u'Rahul',
        "contact":u"973-258-7409",
        "done":False,
    }
]

@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "Status:":"Error",
            "Message:":"Please provide the data"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json['name'],
        "contact":request.json.get('contact'),
        'done':False
    }

    tasks.append(task)

    return jsonify({
        "status":"success",
        "message":"task added successfully",
    },400)

@app.route('/get-data')

def get_task():
    return jsonify({
        "data":tasks
    })


if(__name__ == "__main__"):
    app.run()