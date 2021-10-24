#!/usr/bin/env python3
# by jesse hitch for reaqta
from flask import Flask
from flask import render_template
from flask import request
import logging as log
import sys

# these are global configs
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")
app = Flask(__name__)


@app.route("/")
def index():
    """
    it's me, the main endpoint for the web frontend :3
    """
    log.info("Reached out default web endpoint :D")
    return render_template('index.html')


@app.route("/api")
def api():
    """
    pretend api for imaginary people
    """
    log.info("Reached the main API endpoint")
    return "Welcome to ReaQta API"


@app.route("/api/v1")
def api_v1():
    """
    dummy v1 endpoint
    """
    log.info("Reached the main API endpoint")
    cool_return = """
    Welcome to ReaQta API - v1 - version one - the version of one - one version,
    as you know, this is the initial release, which is most often referred to as
    v1, although you may have seen similar, perhaps v2, but this is v1, and not 
    V1 either, which is also possible, but we're not doing. This is indeed v1
    """
    return cool_return
