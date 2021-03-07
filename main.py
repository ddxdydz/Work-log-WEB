import random
from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.jobs import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
jobs_num = 5


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    for i in range(1, jobs_num + 1):
        job = Job()
        job.team_leader = "1"
        job.job = f"deployment of residential modules {i}"
        job.work_size = str(random.randint(1, 60))
        job.collaborators = f"{i}, 3"
        job.start_date = "now"
        job.is_finished = random.choice([True, False])
        db_sess.add(job)
    db_sess.commit()
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
def index():
    jobs = []
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    for job in db_sess.query(Job).all():
        jobs.append({
            'job': job.job,
            'work_size': job.work_size,
            'collaborators': job.collaborators,
            'start_date': job.start_date,
            'is_finished': job.is_finished
        })
    return render_template('index.html', title='Jobs', jobs=jobs)


if __name__ == '__main__':
    main()
