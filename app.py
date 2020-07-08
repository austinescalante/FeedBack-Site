from flask import Flask, render_template, request


#Data entered and redirection of site

#Initialize app
app = Flask(__name__)
#Create a route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method =='POST':
    #Form data into variables
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

    if customer == '' or dealer == '':
        #Message needs to output in template(index)
        return render_template('index.html', message ='Please enter required fields')
    #render into success page
    return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

