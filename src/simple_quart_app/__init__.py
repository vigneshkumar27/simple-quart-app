from quart import Quart,request,Response,jsonify

app = Quart(__name__)

@app.route("/test",methods=['POST'])
async def test_handler():
    request_body = await request.json
    return jsonify(request_body)

app.run(host="127.0.0.1",port=5000)