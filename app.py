# importing the Flask class from flask module ...> Flask class help to create server applications
from flask import Flask

# go inside this flask module and see inner content ...> ctrl and enter
# print (dir(flask))

# lets create the object of the flask class
# app = Flask(__name__)

# it will show that we r running code from this file only
app = Flask(__name__)

# lets create first route : index route:defoult route
@app.route("/")

def index():
    # returning the response
    return "this is index page"
    
    # pass means we write code letter
    # pass


# second route: contact us
@app.route("/contact")
def contact():
     return "this is contact page"
    
    # pass


# third route: about
@app.route("/about")
def about():
     return "this is about page"
    
    # pass
    
    # lets run the flask  application 
    
app.run()
    
    
    