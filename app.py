#note:if you want to clear data from database than just delete the file .db and run python and run db.create_all() in terminal
#for virtual environment typq env+tab+scr+tab+acti+tab+ps+tab
#than write python +app+tab
from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///dhruv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class reg_form(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    f_name=db.Column(db.String(200),nullable=False)
    l_name=db.Column(db.String(200),nullable=False)
    mob_no=db.Column(db.Integer,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.f_name}"
#for first page
@app.route("/")
def main_first():
    return render_template('index_for_firstpage.html')
#for login page
@app.route("/register",methods=['GET','POST'])
def first_login():
    #for making a working form
    if request.method=="POST":
        f_name=request.form['f_name']
        l_name=request.form['l_name']
        mob_no=request.form['mob_no']
        password=request.form['password']
    #this is a instance of class so you take any name from it 
        dhruv=reg_form(f_name=f_name,l_name=l_name,mob_no=mob_no,password=password)
        db.session.add(dhruv)
        db.session.commit()
    return render_template('index.html')
    # return "<p>Hello, World!</p>"
class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password
        
    def __repr__(self):
        return f'<user:{self.username}>'
    
users=[]
users.append(User(id=1,username="dhruv",password="pass"))
users.append(User(id=2,username="dhruvrajsinh",password="vaghela123"))
users.append(User(id=3,username="pqr",password="word"))
users.append(User(id=4,username="abc",password="word"))
users.append(User(id=5,username="xyz",password="word"))


# print(users)

# app=Flask(__name__)

app.secret_key="secretkey"

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        session.pop("user_id",None)

        username=request.form["username"]
        password=request.form["password"]

        user=[x for x in users if x.username==username][0]
        if user and user.password==password:
            session["user_id"]=user.id
            return redirect("profile")
        return redirect('login')



    return render_template('login.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
    

# for html
# .
# .
@app.route("/learn_html")
def learn_html():
    return render_template('index_for_learnhtml.html')

@app.route("/intro_html")
def intro_html():
    return render_template('intro_for_learnhtml.html')

@app.route("/editor_html")
def editor_html():
    return render_template('editor_for_learnhtml.html')

@app.route("/basic_html")
def basic_html():
    return render_template('basic_for_learnhtml.html')
    
@app.route("/attributes_html")
def attributes_html():
    return render_template('attributes_for_learnhtml.html')

@app.route("/heading_html")
def heading_html():
    return render_template('heading_for_learnhtml.html')   

# for css
# .
# 
@app.route("/learn_css")
def learn_css():
    return render_template('index_for_learncss.html')

@app.route("/intro_css")
def intro_css():
    return render_template('intro_for_learncss.html')

@app.route("/syntax_css")
def syntax_css():
    return render_template('syntax_for_learncss.html')

@app.route("/selector_css")
def selector_css():
    return render_template('selector_for_learncss.html')

@app.route("/howto_css")
def howto_css():
    return render_template('howto_for_learncss.html')

@app.route("/comments_css")
def comments_css():
    return render_template('comments_for_learncss.html')

# for javascrpit
# .
# .
@app.route("/learn_js")
def learn_js():
    return render_template('index_for_learnjs.html')

@app.route("/intro_js")
def intro_js():
    return render_template('intro_for_learnjs.html')

@app.route("/whereto_js")
def whereto_js():
    return render_template('whereto_for_learnjs.html')

@app.route("/output_js")
def output_js():
    return render_template('output_for_learnjs.html')
    
@app.route("/statement_js")
def statement_js():
    return render_template('statement_for_learnjs.html')
        
@app.route("/syntax_js")
def syntax_js():
    return render_template('syntax_for_learnjs.html')

# for sql
# .
# .

@app.route("/learn_sql")
def learn_sql():
    return render_template('index_for_learnsql.html')


@app.route("/intro_sql")
def intro_sql():
    return render_template('intro_for_learnsql.html')

@app.route("/syntax_sql")
def syntax_sql():
    return render_template('syntax_for_learnsql.html')

@app.route("/slct_statement_sql")
def slct_statement_sql():
    return render_template('slct_statement_for_learnsql.html')

@app.route("/distinct_statement_sql")
def distinct_statement_sql():
    return render_template('distinct_statement_for_learnsql.html')

@app.route("/operator_sql")
def operator_sql():
    return render_template('operator_for_learnsql.html')



# for run the app,debug is true for see errors in page while codeing otherwise debug is false
if __name__=="__main__":
    app.run(debug=True,port=2000)