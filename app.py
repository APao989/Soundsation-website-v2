from flask import Flask, render_template, jsonify #imported flask 

app = Flask(__name__) #created flask application

JOBS= [
 {
   'id':1,
   'title':'Data Analyst',
   'location':'Guadalajara, Mexico',
   'salary':'Rs. 10,00,000'
 },
  {
    'id':2,
   'title':'Data Scientist',
   'location':'CDMX, Mexico',
   'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
   'title':'Fronter Engineer',
   'location':'Remote'
  },
  {
    'id':4,
   'title':'Backend Engineer',
   'location':'San Francisco, USA',
   'salary':'$120,000'
  }
]

@app.route("/") #register route to applicatiom
def hello_world():
  return render_template('home.html',
                            jobs=JOBS,
                          )
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__": #if it is running on app.py
  app.run(host='0.0.0.0', debug=True)#Start app