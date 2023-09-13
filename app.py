from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Flask</h1>"



@app.route("/about<name>")
def about1(name):
    return f"<h1>Welcome Mr. {name}</h1>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/form', methods=['get','post'])
def form():
    # return render_template('home.html')
    if request.method == 'GET':
        return render_template('home.html')
    else:
        math = float(request.form['math'])
        phy = float(request.form['phy'])
        chem = float(request.form['chem'])
        avg = (math+phy+chem)/3
        return render_template('home.html',score=avg)



if __name__ == "__main__":
    app.run(debug=True)