from flask import Flask



app=Flask(__name__) # this is your flask application


@app.route('/') #default route
def default(): # it is default function
    return "Hello Everyone" #i am returning the value

@app.route('/predict') # predict route
def predict():
    return "predicting result"


if __name__=='__main__':
    app.run() # to run your application
