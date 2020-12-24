from flask import Flask, jsonify, request, make_response, render_template

app = Flask(__name__)
Data = {'1': {
    'Name': 'Dhivya',
    'Dept': 'IT'
}, '2': {
    'Name': 'Priya',
    'Dept': 'CT'
}}


@app.route('/', methods=['GET'])
def home():
    return render_template('results.html')


@app.route('/all', methods=['GET'])
def display():
    return jsonify(Data)


@app.route('/data/<obj>', methods=['GET'])
def dis_part(obj):
    if obj in Data:
        res = make_response(jsonify(Data[obj]), 200)
        return res
    else:
        result = make_response(jsonify({"Error": "Object not found"}), 404)
        return result


@app.route('/update/<obj>', methods=['PATCH'])
def patch(obj):
    req = request.get_json()
    if obj in Data:
        for k, v in req.items():
            Data[obj][k] = v
        res = make_response(jsonify({"success": "updated"}), 200)
        return res
    else:
        Data[obj] = req
        res = make_response(jsonify({"created": "object"}), 200)
        return res


if __name__ == "__main__":
    app.run()
