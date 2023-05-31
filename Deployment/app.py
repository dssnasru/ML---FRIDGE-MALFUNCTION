from flask import Flask, request ,render_template
from model import predictor

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")




@app.route('/fridge')
def fri():
    return "this is fridge page to take inputs"


@app.route('/output', methods=["POST","GET"])
def out():
    if request.method == "POST":
        dc=request.form["dev_cap"]
        dp=request.form["dev_pre"]
        d_tem=request.form["dev_tem"]
        cl=request.form["cur_loc"]
        yr=int(request.form["year"])
        mon=int(request.form["mon"])
        day=int(request.form["day"])
        o=predictor(cl=cl,day=day,month=mon,dc=dc,dt=d_tem,year=yr,dp=dp)

        return render_template("results.html",res = o)

    
    


if __name__ =="__main__":
    app.run(debug=True)