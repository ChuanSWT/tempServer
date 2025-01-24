from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if(request.method == 'GET'):
        data={
            'data':'helloQT'
                      }
        return jsonify(data)
    if(request.method == 'POST'):
        data=request.json
        print(data)
        num1=int(data['num1'])
        num2=int(data['num2'])
        return jsonify({'ans':num1+num2})



if __name__ == '__main__':
    app.run(debug=True,port=80)