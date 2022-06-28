import os
import click
from flask import request
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role
from ckan import create_app, db
from ckan.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)



@app.before_first_request  #第1个请求到来执行
def before_first_request1():
    print('before_first_request1')


@app.before_request #中间件2
def before_request1():
    print('before_request1')  #不能有返回值，一旦有返回值在当前返回


@app.before_request
def before_request2():
    print('before_request2')
    print(request.path)


@app.after_request #中间件 执行视图之后
def after_request1(response):
    print('after_request1', response)
    return response


@app.after_request #中间件 执行视图之后 先执行 after_request2（最下面的先执行）
def after_request2(response):
    print('after_request2', response)
    return response


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    print(app.url_map)