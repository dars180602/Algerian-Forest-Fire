

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def cal_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def calculator_ops():
    ops=request.form['operation']
    first_num=int(request.form['num1'])
    second_num=int(request.form['num2'])

    if ops=='add':
        result=first_num+second_num
        return f"Addition of {first_num} and {second_num} is {result}"
    
    if ops=='substract':
        result=first_num-second_num
        return f"substraction of {first_num} and {second_num} is {result}"
    
    if ops=='multiply':
        result=first_num*second_num
        return f"Multiplication of {first_num} and {second_num} is {result}"
    
    if ops=='divide':
        result=first_num/second_num
        return f"Division of {first_num} and {second_num} is {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)