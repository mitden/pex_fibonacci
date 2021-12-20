from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>fibonacci calculator</p>"
@app.route("/fibonacci",methods=['GET', 'POST'])
def fibonacciCalc():

    if request.method == 'POST':
        num = request.form['num']
    else:    
        num = request.args.get('num')
    return {
        "num":num,
        "result": fibonacci(int(num)),      
    }

def  fibonacci(num):
    arr = [0,1]
    if num==1:
      arr = [0]
    elif num==2:
       arr = [0,1]
    else:
        while(len(arr)<num):
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,num):
                arr[i]=arr[i-1]+arr[i-2]
    return sum(arr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
         