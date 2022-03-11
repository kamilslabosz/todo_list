from flask import Flask, render_template, request, session, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = ''

Bootstrap(app)


class TodoForm(FlaskForm):
    todo_text = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/", methods=["GET", "POST"])
def home():
    form = TodoForm()
    if request.method == "POST":
        try:
            session['todo_list'] += form.todo_text.data.split(" ")
        except KeyError:
            session['todo_list'] = form.todo_text.data.split(" ")
        current_list = session.get('todo_list')
        print(current_list)
        form.todo_text.data = ""
        return render_template('index.html', form=form, tasks=current_list)
    return render_template("index.html", form=form)


@app.route('/clear', methods=["GET", "POST"])
def clear_todo_list():
    session['todo_list'] = []
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)