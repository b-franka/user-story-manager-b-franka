#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request
from stories import *

app = Flask(__name__)


@app.route('/')
@app.route('/list', methods=["GET"])
def story_listing():
    stories = Story.select()
    return render_template('list.html', stories=stories)


@app.route('/story', methods=["GET"])
def story_adding():
    return render_template('form.html', status='new')


@app.route('/story', methods=["POST"])
def story_saving():
    Story.create(story_title=request.form["story_title"],
                 user_story=request.form["user_story"],
                 acceptance_criteria=request.form["acceptance_criteria"],
                 business_value=request.form["business_value"],
                 estimation=request.form["estimation"],
                 status=request.form["status"])
    return redirect(url_for("story_listing"))


@app.route('/story/<int:story_id>', methods=["GET"])
def story_view(story_id):
    story = Story.get(Story.id == story_id)
    return render_template('form.html', status='edit', data=story)


@app.route('/story/<int:story_id>', methods=["POST"])
def story_editing(story_id):
    if request.method == "POST":
        story = Story.update(story_title=request.form["story_title"],
                             user_story=request.form["user_story"],
                             acceptance_criteria=request.form["acceptance_criteria"],
                             business_value=request.form["business_value"],
                             estimation=request.form["estimation"],
                             status=request.form["status"]).where(Story.id==story_id)
        story.save()
    return redirect(url_for("story_listing"))


# @app.route('/story/<int:story_id>', methods=["GET", "POST"])
# def story_editing():
#     if request.method == "POST":
#         Story.update(story_title=request.form["story_title"],
#                      user_story=request.form["user_story"],
#                      acceptance_criteria=request.form["acceptance_criteria"],
#                      business_value=request.form["business_value"],
#                      estimation=request.form["estimation"],
#                      status=request.form["status"]).where(Story.id==story_id)
#     else:
#         return render_template('form.html', status='edit')

# @app.route('/')
# @app.route('/list', methods=["GET", "POST"])
# def story_listing():
#     # if request.method == "POST":
#     stories = Story.select()
#     return render_template('list.html', stories=stories)

if __name__ == '__main__':
    app.run(debug=True)
