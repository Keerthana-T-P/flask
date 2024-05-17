
from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/square',methods=['GET'])
def squarenumber():
    num=request.args.get('num')
    if num is None:
        return render_template('squarenum.html')
    elif num=='':
        return "<html><body><h1>Invalid number</h1></body></html>"
    else:
        try:
            number=int(num)
            sq=number*number
            return render_template('answer.html',squareofnum=sq,num=number)
        except ValueError:
            return "<html><body><h1>Invalid number</h1></body></html>"
if __name__=="__main__":
    app.run(debug=True)