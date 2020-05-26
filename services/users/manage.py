#!/usr/bin/env python
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
import unittest

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreatedb():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def seeddb():
    db.session.add(User(username='nishant', email="nishantmailbox2011@gmail.com"))
    db.session.commit()


@cli.command()
def test():
    tests = unittest.TestLoader().discover(
        'project/tests',
        pattern='test*.py'
    )
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
