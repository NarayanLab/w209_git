from flask import Flask, render_template
app = Flask(__name__)
import pandas as pd

@app.route("/")
def w209():
    file="about9.jpg"
    return render_template("w209.html",file=file)

@app.route("/pandas-api/")
def api():
    d = pd.DataFrame([{"a":"b"}])
    return d.to_dict()

@app.route("/test_sn/")
def test():
    file = "REACT_summary.png"
    return render_template("test_sn.html", file = file), 344

if __name__ == "__main__":
    app.run()
