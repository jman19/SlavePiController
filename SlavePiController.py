from flask import Flask

app = Flask(__name__)


@app.route("/translate",methods=['POST'])
def translate():
	try:
		#put your translate service here
		return buildResponse(200,"sucess")
	except Exception as e:
		return buildResponse(500,str(e))

@app.route("/clear",methods=['POST'])
def clear():
	try:
		#put your clear service here
		return buildResponse(200,"sucess")
	except Exception as e:
		return buildResponse(500,str(e))


def buildResponse(code,message):
	return {"code":code,"message":message}

if __name__=='__main__':
	app.debug=True
	app.run(host='127.0.0.1',port=8181)