# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def squarenumber():
    if request.method == 'POST':
        if(request.form['num'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number = request.form['num']
            sq = int(number) * int(number)
            return render_template('answer.html', 
                            squareofnum=sq, num=number)
    
    if request.method == 'GET':
        return render_template("squarenum.html")
if(__name__ == "__main__"):
    app.run(debug=True)
