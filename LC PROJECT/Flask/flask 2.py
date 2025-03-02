
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')
def index():
    return render_template("index.html")


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    