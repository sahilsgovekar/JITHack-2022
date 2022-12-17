from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

question = ["Is mediatation good for health", "Why does someone with mental illness need to have a routine?", "Why do some people choose to just take meds and no therapy, is that safe?"]
answer = ["Meditation is great for health", "Mental illness can often disrupt a person's life by hindering that person's ability to focus on and complete tasks that they otherwise would be able to complete. Establishing a productive daily routine can help to normalize that person's daily life and having a routine most often contributes to increased life satisfaction that comes with personal accomplishment (in the human population as a whole, not just those living with mental illness).", "The decision to take prescription medication is one that every individual must make for his or herself. Some people do not feel comfortable divulging information to doctors or others living with mental illness in a therapy environment so they choose to rely solely on medication to combat the disturbances in their lives caused by mental illness. The question of whether it is safe to take prescription medication without partaking in therapy can best be answered by stating that it might be less effective to take medication without the benefit of therapy, but it does not seem to have been proven to be unsafe."]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), unique=True)
    answer = db.Column(db.String(100))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        que = request.form['question']
        ans = " "
        nq = User(question=que, answer=ans)
        db.session.add(nq)
        db.session.commit()
        question.append(que)
        answer.append(ans)
        redirect("/")

    qna = db.session.query(User).all() 
    print(qna)
    return render_template('index.html', qna = question, ans = answer)





if __name__ == "__main__":
    app.run(debug=True)

