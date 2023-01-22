from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/join/')
def join():
    return render_template('join.html')

@app.route('/officers/')
def officers():
    return render_template('officers.html')

@app.route('/character_sheet/')
def character_sheet():
    return render_template('character_sheet.html')

if __name__ == '__main__':
    app.run(debug=True)