# -*- coding: utf-8 -*-
"""
__author__ = "Asim Hussain"
"""
import logging

from fabric.colors import green
from fabric.api import *
from fabric.utils import puts


LOGGER = logging.getLogger(__name__)


def qa():
    puts(green('Using QA settings'))
    env.herokuapp = "huffpsst-qa"
    env.branch = "master"
    env.remote = "heroku-qa"


def prod():
    puts(green('Using prod settings'))
    env.herokuapp = "huffpsst-prod"
    env.branch = "master"
    env.remote = "heroku"


def push():
    local("git push %s %s:master" % (env.remote, env.branch))

def deploy():
    # local("python manage.py compress")
    local("git push %s %s:master" % (env.remote, env.branch))
    local("heroku run --app %s python manage.py migrate" % (env.herokuapp))

def schema():
    local("python manage.py schemamigration huffpsst --auto")

def migrate():
    local("python manage.py migrate huffpsst")
