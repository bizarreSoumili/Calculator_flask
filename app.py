from flask import Flask, request, jsonify,render_template

app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def maths_ops():
    if request.method == 'POST':
        ops = request.form['operations']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        if ops == 'subtract':
            r = num1 - num2
            result = "The subtraction of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif ops == 'multiply':
            r = num1 * num2
            result = "The multiplication of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        elif ops == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)
            else:
                result = "Division by zero is not allowed."
        else:
            result = "Invalid operation selected."
        
        return render_template('results.html', results=result)

if __name__=="__main__":
    app.run(host="0.0.0.0")