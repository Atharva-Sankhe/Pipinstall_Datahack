from flask import Flask, render_template, request
import csv

app = Flask(__name__ )

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result', methods=['POST'])
def result():
    import pandas as pd
    df = pd.read_csv('data0.csv')
    x = request.form['fname']
    print(x)
    ans = ''
    for i in range(len(df)):
        if df['Left Hand Side'][i]==x:
            ans = ans+df['Right Hand Side'][i] + ', '
    print(ans)
    
    print(f"x is {x}")
    print(f'y is {ans}')
    # return "something"
    return render_template("result.html", y=ans , x = x)
    

if __name__ == '__main__':
    app.run(debug=True)