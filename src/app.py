from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])  
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Perform login authentication logic here
    # You can customize this part to match your specific requirements
    
    if username == 'admin' and password == 'password':
        return redirect('/')
    
    else:
        return 'Login failed!'
if __name__ == '__main__':
    app.run()