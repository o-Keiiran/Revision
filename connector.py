from flask import Flask, render_template, request, redirect, url_for, session

# create our web app
app = Flask(__name__, static_folder='static')


# landing page
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/page1')
def page_one():
    # You can add some content here if needed
    return render_template('page1.html')
# page 2 route
@app.route('/page2')
def page_two():
    # You can add some content here if needed
    return render_template('page2.html')
@app.route('/page3')
def page_three():
    # You can add some content here if needed
    return render_template('page3.html')
# page 2 route
@app.route('/page4')
def page_four():
    # You can add some content here if needed
    return render_template('page4.html')
@app.route('/chat')
def chat():
    # You can add some content here if needed
    return render_template('chat.html')
@app.route('/secret')
def secret():
    # You can add some content here if needed
    return render_template('secret.html')
# run the app
if __name__ == '__main__':
    app.run(debug=True)

