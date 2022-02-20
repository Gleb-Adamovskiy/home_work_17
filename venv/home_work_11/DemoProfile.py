from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',)
def page_profile():
    return render_template("list.html")

app.run()
