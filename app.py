from flask import Flask, render_template #imported flask 

app = Flask(__name__) #created flask application

@app.route("/") #register route to applicatiom
def hello_world():
  return render_template('home.html')

if __name__ == "__main__": #if it is running on app.py
  app.run(host='0.0.0.0', debug=True)#Start app