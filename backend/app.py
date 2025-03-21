from flask import Flask , render_template
app = Flask(__name__)

# sample ci/cd data

data = {
    "last_build_status": "Successful",
    "build_time":"45 sec",
    "deploy_status" :"deployed",
    "container_count": 4
}

@app.route ('/')
def dashboard ():
    return render_template ('dashboard.html',data=data )
if __name__=="__main__":
    app.run (debug=True)
