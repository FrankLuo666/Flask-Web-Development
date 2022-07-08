from flask import render_template, session, redirect, url_for, current_app, request,Blueprint
from .. import db
from ..models import User
from ..email import send_email
from ..forms.userForm import NameForm


home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def index():
    # print(__file__)
    # print(request.path)
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=2)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('home.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@home.route('/setSession')
def setSession():
    session['username'] = 'smart'
    session['age'] = 18
    return "设置session"

@home.route('/getSession')
def getSession():
    username = session.get('username')
    age = session.get('age')
    return f'username: {username}, age: {age}'


@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@home.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
