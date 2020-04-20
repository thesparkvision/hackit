from flask import Flask,render_template
app =Flask(__name__)

@app.route('/home')
def login():
    return render_template('home.html')

app.run(debug=True)
