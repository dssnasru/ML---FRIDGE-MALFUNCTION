import pickle
import numpy as np
import warnings
import datetime
warnings.filterwarnings("ignore")
model = pickle.load(open("Model.pkl","rb"))
loc_enc = pickle.load(open("loc_encoder.pkl","rb"))

def predictor(dc,dp,dt,cl,year,month,day):
    cl_dc=loc_enc.transform(np.array([cl]))[0]
    run_days=model.predict(np.array([[dc,dp,dt,cl_dc]]))[0]
    pur=datetime.datetime(year,month,day)
    end = pur + datetime.timedelta(days = run_days)
    return end


print(predictor(220,3,39,"Chennai",2020,10,29))