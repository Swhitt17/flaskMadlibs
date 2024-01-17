from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/' )
def select_story():
    """Show story selection"""
    
    return render_template("select-story.html",  stories=stories.values())

@app.route('/form',methods=["GET"])
def story_form():
    """Generate form to collect words"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template('form.html',story_id=story_id,
                           title=story.title, prompts=prompts)



@app.route('/story', methods=["POST"])
def show_story():
    """Show completed story"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)
    
    return render_template("story.html",title=story.title, text=text)
