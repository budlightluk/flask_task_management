from os import abort

from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Task
from app.forms import LoginForm, RegistrationForm, TaskForm

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@bp.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, due_date=form.due_date.data,
                    user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!')
        return redirect(url_for('main.index'))
    return render_template('task_form.html', title='New Task', form=form)


@bp.route('/task/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        abort(403)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.due_date.data = task.due_date
    return render_template('task_form.html', title='Edit Task', form=form)


@bp.route('/task/<int:id>/delete', methods=['POST'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash('Your task has been deleted!')
    return redirect(url_for('main.index'))
