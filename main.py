#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request
from stories import Story

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
    story = Story.get(Story.id == story_id)
    story.story_title = request.form["story_title"]
    story.user_story = request.form["user_story"]
    story.acceptance_criteria = request.form["acceptance_criteria"]
    story.business_value = request.form["business_value"]
    story.estimation = request.form["estimation"]
    story.status = request.form["status"]
    story.save()
    return redirect(url_for("story_listing"))


@app.route('/delete/<int:story_id>', methods=["GET", "POST"])
def story_del(story_id):
    story_to_be_deleted = Story.get(Story.id == story_id)
    story_to_be_deleted.delete_instance()
    return redirect(url_for("story_listing"))



if __name__ == '__main__':
    app.run(debug=True)
