from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')
def hello_world():
    return 'Hello, World!'


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7000)

