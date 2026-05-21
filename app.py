import pandas as pd
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "student_secret_key"

#Student Load CSV files
df = pd.read_csv("student_performance_dataset_1000.csv")
CSV_FILE = "student_performance_dataset_1000.csv"


# #Teacher Load CSV files
teachers_login_df = pd.read_csv("teachers.csv")
def val (ax):
      for container in ax.containers:
        ax.bar_label(container)
# .................WElcome............
@app.route("/")
def welcome():
    return render_template("welcome.html")

# ---------------- Aboutproject ----------------
@app.route("/aboutproject")
def aboutproject():
    return render_template("aboutproject.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        role = request.form.get("role")
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        # empty dataframe to avoid error
        student = pd.DataFrame()
        teacher = pd.DataFrame()

        # ---------- STUDENT LOGIN ----------
        if role == "student":

            student = df[
                (df["Roll_No"].astype(str) == str(user_id)) &
                (df["Name"] == password)
            ]

            if not student.empty:
                session["roll_no"] = user_id
                session["name"] = password
                session["role"] = "student"

                return redirect(url_for("dashboard"))

        # ---------- TEACHER LOGIN ----------
        elif role == "teacher":

            teacher = teachers_login_df[
                (teachers_login_df["teacher_id"].astype(str) == str(user_id)) &
                (teachers_login_df["teacher_name"] == password)
            ]

            if not teacher.empty:
                session["roll_no"] = user_id
                session["name"] = password
                session["role"] = "teacher"

                return redirect(url_for("teacherdashboard"))

        return "Invalid Login"

    return render_template("login.html")

# ---------------- DASHBOARD PAGE ----------------
@app.route("/dashboard")
def dashboard():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    roll = session["roll_no"]
    charts ={}
    student = df[df["Roll_No"].astype(str) == str(roll)]
    if student.empty:
        return "Student not found"
    branch=student["Branch"].values[0].strip()
    sub1=df.columns[6]
    sub2=df.columns[7]
    sub3=df.columns[8]
    sub4=df.columns[9]
    sub5=df.columns[10]
    attandance=student["Attandance"].values[0]
    maths =student["Maths"].values[0]
    ds =student["DS"].values[0]
    os =student["OS"].values[0]
    dbms =student["DBMS"].values[0]
    ai =student["AI"].values[0]
    mark1 =[maths,100-maths]
   


    plt.figure(figsize=(4,4))
    plt.pie(mark1, autopct="%0.1f",wedgeprops=dict(width=0.5),textprops={"fontsize":12})
    plt.legend([sub1,"Remaining"],loc=4)
    plt.title(sub1+" Marks!")
    plt.axis('equal')
    plt.tight_layout()

    img1 = io.BytesIO()
    plt.savefig(img1,format="png",transparent =True)
    img1.seek(0)

    charts["chart1"] =base64.b64encode(img1.getvalue()).decode()
    plt.clf()
    plt.close()

    mark2 =[ds,100-ds]
    plt.figure(figsize=(4,4))
    plt.pie(mark2, autopct="%0.1f",wedgeprops=dict(width=0.5),textprops={"fontsize":12})
    plt.legend([sub2,"Remaining"],loc=4)
    plt.title(sub2+" Marks!")
    plt.axis('equal')
    plt.tight_layout()

    img2 = io.BytesIO()
    plt.savefig(img2,format="png",transparent =True)
    img2.seek(0)
    charts["chart2"] =base64.b64encode(img2.getvalue()).decode()
    plt.clf()
    plt.close()

    mark3 =[os,100-os]
    plt.figure(figsize=(4,4))
    plt.pie(mark3, autopct="%0.1f",wedgeprops=dict(width=0.5),textprops={"fontsize":12})
    plt.legend([sub3,"Remaining"],loc=4)
    plt.title(sub3+" Marks!")
    plt.axis('equal')
    plt.tight_layout()

    img3 = io.BytesIO()
    plt.savefig(img3,format="png",transparent =True)
    img3.seek(0)

    charts["chart3"] =base64.b64encode(img3.getvalue()).decode()
    plt.clf()
    plt.close()

    mark4 =[dbms,100-dbms]
    plt.figure(figsize=(4,4))
    plt.pie(mark4, autopct="%0.1f",wedgeprops=dict(width=0.5),textprops={"fontsize":12})
    plt.legend([sub4,"Remaining"],loc=4)
    plt.title(sub4+" Marks!")
    plt.axis('equal')
    plt.tight_layout()

    img4 = io.BytesIO()
    plt.savefig(img4,format="png",transparent =True)
    img4.seek(0)

    charts["chart4"] =base64.b64encode(img4.getvalue()).decode()
    plt.clf()
    plt.close()
    
    mark5 =[ai,100-ai]
    plt.figure(figsize=(4,4))
    plt.pie(mark5, autopct="%0.1f",wedgeprops=dict(width=0.5),textprops={"fontsize":12})
    plt.legend([sub5,"Remaining"],loc=4)
    plt.title(sub5+" Marks!")
    plt.axis('equal')
    plt.tight_layout()

    img5 = io.BytesIO()
    plt.savefig(img5,format="png",transparent =True)
    img5.seek(0)

    charts["chart5"] =base64.b64encode(img5.getvalue()).decode()
    plt.clf()
    plt.close()

    att =[attandance,100-attandance]
    plt.figure(figsize=(4,4))
    plt.pie(att, autopct="%0.1f%%",wedgeprops=dict(width=0.8),textprops={"fontsize":16},colors=("g","r"))
    plt.legend(["Attandance","Not Attend"],loc=4)
    plt.title("Attandance!")
    plt.axis('equal')
    plt.tight_layout()

    img6 = io.BytesIO()
    plt.savefig(img6,format="png",transparent =True)
    img6.seek(0)

    charts["chart6"] =base64.b64encode(img6.getvalue()).decode()
    plt.clf()
    plt.close()

    totalmarks =[maths,ds,os,dbms,ai]
    plt.figure(figsize=(4,4))
    plt.pie(totalmarks, autopct="%0.1f%%",wedgeprops=dict(width=0.8),textprops={"fontsize":16})
    plt.legend([sub1,sub2,sub3,sub4,sub5],loc=4)
    plt.title("Marks Percentage Out of 100!")
    plt.axis('equal')
    plt.tight_layout()

    img7 = io.BytesIO()
    plt.savefig(img7,format="png",transparent =True)
    img7.seek(0)

    charts["chart7"] =base64.b64encode(img7.getvalue()).decode()
    plt.clf()
    plt.close()
    return render_template("dashboard.html",charts=charts)

@app.route("/dashboard1")
def dashboard1():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    
    roll = session["roll_no"]
    charts ={}
    student = df[df["Roll_No"].astype(str) == str(roll)]
    if student.empty:
        return "Student not found"
    branch=student["Branch"].values[0].strip()
    sub1=df.columns[6]
    sub2=df.columns[7]
    sub3=df.columns[8]
    sub4=df.columns[9]
    sub5=df.columns[10]

    maths =student["Maths"].values[0]
    ds =student["DS"].values[0]
    os =student["OS"].values[0]
    dbms =student["DBMS"].values[0]
    ai =student["AI"].values[0]

    
    x=[sub1,sub2,sub3,sub4,sub5]
    y=[maths,ds,os,dbms,ai]
    plt.figure(figsize=(9,5.5))
    ax =sns.barplot(x=x,y=y,palette="rocket")
    val(ax)
    plt.xticks(rotation=10)
    # plt.xlabel("Subject")
    # plt.ylabel("Marks")
    plt.title("Over All Subject")
    plt.tight_layout()

    img1=io.BytesIO()
    plt.savefig(img1,format="png",transparent=True)
    img1.seek(0)
    
    charts["chart1"] =base64.b64encode(img1.getvalue()).decode()
    plt.clf()
    plt.close()


    x=[sub1,sub2,sub3,sub4,sub5]
    y=[maths,ds,os,dbms,ai]
    plt.figure(figsize=(12,5))
    plt.scatter(x,y,c = "m",alpha=0.8)
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Over All Subject")
    plt.tight_layout()

    img2=io.BytesIO()
    plt.savefig(img2,format="png")
    img2.seek(0)
    
    charts["chart2"] =base64.b64encode(img2.getvalue()).decode()
    plt.clf()
    plt.close()
    return render_template("dashboard1.html",charts=charts)
@app.route("/teacherdashboard")
def teacherdashboard():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    
    bars ={}
    plt.figure(figsize=(15,10))
    plt.subplot(2,2,1)
    _gret85per = df[df["Attandance"]>=85]["Name"].count()
    _gret75per = df[ (df["Attandance"]>=75) & (df["Attandance"]<85)] ["Name"].count()
    _gret50per = df[ (df["Attandance"]>=50) & (df["Attandance"]<75)] ["Name"].count()
    _less50per = df[ (df["Attandance"]<50)]["Name"].count()
    x =["85 and Above","Above 75","Above 50","Less than 50"]
    y =[_gret85per,_gret75per,_gret50per,_less50per]
    ax = sns.barplot(x=x,y=y,width=.5,palette="tab10")
    plt.title("Attandance Wise Student")
    
    val(ax)
    plt.subplot(2,2,2)
    _gret85per = df[df["Final_Percentage"]>=85]["Name"].count()
    _gret75per = df[ (df["Final_Percentage"]>=75) & (df["Final_Percentage"]<85)] ["Name"].count()
    _gret50per = df[ (df["Final_Percentage"]>=50) & (df["Final_Percentage"]<75)] ["Name"].count()
    _less50per = df[ (df["Final_Percentage"]<50)]["Name"].count()
    x =["85 and Above","Above 75","Above 50","Less than 50"]
    y =[_gret85per,_gret75per,_gret50per,_less50per]
    ax = sns.barplot(x=x,y=y,width=.5,palette="tab10")
    plt.title("Percentange Wise Student")
    val(ax)
    plt.subplot(2,2,3)
    count2 = df["Semester"].value_counts()
    ax = sns.barplot(count2,palette="tab10")
    plt.title("Semester wise Student")
    val(ax) 
    plt.subplot(2,2,4)
    top10citystudent = df.value_counts("City").sort_values(ascending=False).head(5)
    ax = sns.barplot(top10citystudent,palette="tab10",width=0.6)
    plt.title("Top 5 City Wise Student")
    val(ax)
    plt.tight_layout()

    bar1=io.BytesIO()
    plt.savefig(bar1,format="png")
    bar1.seek(0)
    
    bars["bar1"] =base64.b64encode(bar1.getvalue()).decode()
    plt.clf()
    plt.close()
    return render_template("teacherdashboard.html",bars=bars)
@app.route("/teacherdashboard1")
def teacherdashboard1():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    pies = {}
    plt.figure(figsize=(15,10))
    plt.subplot(2,2,1)
    count = df["Gender"].value_counts()
    ax = sns.barplot(x=count.index,y=count.values,palette="tab10",width=0.5)
    plt.title("Gender Wise Student")
    val(ax)
    plt.subplot(2,2,2)
    count1 = df["Participant"].value_counts()
    ax = sns.barplot(x=count1.index,y=count1.values,palette="tab10",width=0.5)
    plt.title("Participant Wise Student")
    val(ax)
    plt.subplot(2,2,3)
    branch = df.value_counts("Branch")
    ax = sns.barplot(branch,width=0.8,palette="tab10")
    plt.title("Branch Wise Student")
    val(ax)
    plt.subplot(2,2,4)
    state = df["State"].value_counts()
    ax = sns.barplot(state,palette="tab10",width=0.5)
    plt.title("State Wise Student")
    val(ax)
    plt.xticks(rotation =15)
    plt.tight_layout()

    bar1=io.BytesIO()
    plt.savefig(bar1,format="png")
    bar1.seek(0)
    
    pies["bar1"] =base64.b64encode(bar1.getvalue()).decode()
    plt.clf()
    plt.close()
    return render_template("teacherdashboard1.html",pies=pies)
## ---------------- STUDENT DETAIL DATA API  ----------------
@app.route("/api/student")
def student_api():
    if "roll_no" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    roll_no = session["roll_no"]

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"] == roll_no:
                return jsonify(row)

    return jsonify({"error": "Student not found"}), 404

# ---------------- OTHER ROUTES ----------------
@app.route("/prediction")
def prediction():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    return render_template("prediction.html")

@app.route("/profile")
def profile():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    return render_template("profile.html")

@app.route("/students")
def students():
    if "roll_no" not in session:
        return redirect(url_for("login"))

    # data = students_login_df.to_dict(orient="records")
    return render_template("student.html")

@app.route("/report")
def report():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    return render_template("report.html")

@app.route("/print_page")
def print_page():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    return render_template("print_page.html")

@app.route("/about")
def about():
    if "roll_no" not in session:
        return redirect(url_for("login"))
    return render_template("about.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("welcome"))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)