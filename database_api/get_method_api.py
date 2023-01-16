from flask import Flask ,request,jsonify
import mysql.connector as conn
app=Flask(__name__)

@app.route("/get_data")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile_number")
    mail_id = request.args.get('mail_id')
    return "this is my 1st function for get {} {} {}".format(get_name,mobile_number,mail_id)

#if __name__=="__main__":
   # app.run(port=5002)


#by using get method fetching the data from database
@app.route('/fetch_data_from_db')
def get_data_from():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", password="admin", database=db)
        cur = con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__=="__main__":
    app.run(port= 5002)