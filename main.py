from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    res = []
    for job in jobs:
        leader = db_sess.query(User).filter(User.id == job.team_leader).first()
        leader = f"{leader.surname} {leader.name}"
        is_fin = job.is_finished
        if is_fin:
            is_fin = 'is finished'
        else:
            is_fin = 'is not finished'
        res.append([f"Action # {job.id}", job.job, leader, f"{job.work_size} hours", job.collaborators, is_fin])

    return render_template('jobs.html', jobs=res)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

'''
db_name = input()
global_init(db_name)
db_sess = create_session()

find = db_sess.query(User).filter(User.speciality.notlike('%engineer%'), User.position.notlike('%engineer%'),
                                  User.address == 'module_1')

for item in find:
    print(item.id)
'''
