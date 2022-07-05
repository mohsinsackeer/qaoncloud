from flask import Flask, render_template, request, redirect

class IncompleteFormError(Exception):
    pass

app = Flask(__name__)


@app.route('/')
def display_form() -> 'web form':
    return render_template('form_page.html',
                           the_title='Submit Your Details')


@app.route('/submit', methods=['POST'])
def retrieve_form_details() -> str:
    langs = ['C', 'CPP', 'CS', 'Java', 'Python', 'Javascript']

    # Receiving the form data
    try:
        name = request.form['full_name']
        age = request.form['age']
        if not name or not age:
            raise IncompleteFormError('The Form is Incomplete!')
        gender = request.form['gender']
        lang_expertise = []
        for lang in langs:
            val = f"language_{lang}"
            if val in request.form.keys():
                lang_expertise.append(request.form[val])
        lang_expertise = ', '.join(lang for lang in lang_expertise)
        if not lang_expertise:
            lang_expertise = 'None'
        favourite_lang = request.form['favourite_lang']


        # Printing the form data
        msg = f"""Submitted Details
    --- Name: {name}
    --- Age: {age}
    --- Gender: {gender}
    --- Language Expertise: {lang_expertise}
    --- Favourite Language: {favourite_lang}"""

        # Displaying the form data in terminal
        print(msg)

        # Displaying the form data in an html file
        return render_template('results.html',
                               the_title='Submitted Details',
                               name=name,
                               age=age,
                               gender=gender,
                               lang_expertise=lang_expertise,
                               favourite_lang=favourite_lang)
    except Exception as e:
        print(f"Error: {e}")
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
