from flask import  Flask,render_template,jsonify
# categories=[
#     {"1":"Food",
#     "2":"Transportation",
#     "3":"Entertainment"
#     }
# ]

app=Flask(__name__)
@app.route("/")
def helloapp():
    return render_template('home.html')

# @app.route("/expense")
# def list_expense():
#     return jsonify(categories)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)