# ### Integrate HTML With Flask
# ### HTTP verb GET And POST
# from flask import Flask,redirect,url_for,render_template,request

# app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return render_template('index.html')

# @app.route('/success/<int:score>')
# def success(score):
#     res=""
#     if score>=50:
#         res="PASS"
#     else:
#         res="FAIL"

#     return render_template('result.html',result=res)


# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The Person has failed and the marks is "+ str(score)

# ### Result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result=""
#     if marks<50:
#         result='fail'
#     else:
#         result='success'
#     return redirect(url_for(result,score=marks))

# ### Result checker submit html page
# @app.route('/submit',methods=['POST','GET'])
# def submit():
#     total_score=0
#     if request.method=='POST':
#         science=float(request.form['science'])
#         maths=float(request.form['maths'])
#         c=float(request.form['c'])
#         data_science=float(request.form['datascience'])
#         total_score=(science+maths+c+data_science)/4
#     res=""
#     return redirect(url_for('success',score=total_score))

    



# if __name__=='__main__':
#     app.run(debug=True)

"""

Important:

templates/ holds your HTML files.
static/ holds your CSS, JS, and images.
main.py is your Flask app.


"""


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, redirect, url_for, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return render_template('index.html')

# @app.route('/success/<int:score>')
# def success(score):
#     res = ""
#     if score >= 50:
#         res = "PASS"
#     else:
#         res = "FAIL"
#     return render_template('result.html', result=res)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The Person has failed and the marks is " + str(score)

# # Result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result = ""
#     if marks < 50:
#         result = 'fail'
#     else:
#         result = 'success'
#     return redirect(url_for(result, score=marks))

# # Result checker submit html page
# @app.route('/submit', methods=['POST', 'GET'])
# def submit():
#     total_score = 0
#     if request.method == 'POST':
#         science = float(request.form['science'])
#         maths = float(request.form['maths'])
#         c = float(request.form['c'])
#         data_science = float(request.form['datascience'])
#         total_score = (science + maths + c + data_science) / 4

#     return redirect(url_for('success', score=total_score))

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    # Decide pass/fail
    result_text = "PASS" if score >= 50 else "FAIL"
    return render_template('result.html', result=result_text)

@app.route('/fail/<int:score>')
def fail(score):
    return f"The Person has failed and the marks are {score}"

# Route to check result
@app.route('/results/<int:marks>')
def results(marks):
    # Based on marks, pick 'fail' or 'success' route
    outcome = 'fail' if marks < 50 else 'success'
    return redirect(url_for(outcome, score=marks))

# Handle form submission
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        # Calculate average
        total_score = (science + maths + c + data_science) / 4

        # Redirect to /success/<score> or /fail/<score>
        return redirect(url_for('success', score=total_score))

    # If GET (direct URL access), just show form again or handle differently
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
