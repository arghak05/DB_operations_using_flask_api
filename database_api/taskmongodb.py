from flask import Flask,request,jsonify
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@practice.cn7w0tt.mongodb.net/?retryWrites=true&w=majority")
database = client['apitaskdb']
collection = database['apitaskcollection']
@app.route("/insert/mongo",methods=['POST'])
def insert():
     if request.method=='POST':
         name=request.json['name']
         number=request.json['number']
         collection.insert_one({name:number})
         return jsonify(str("Sucessfully inserted"))


if __name__=='__main__':
    app.run(port=5001)