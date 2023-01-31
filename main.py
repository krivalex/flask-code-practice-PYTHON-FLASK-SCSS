from flask import Flask, render_template
from flask import request
import openai

openai.api_key = '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'
app = Flask(__name__)

@app.route("/plankton-app-d5pi9.ondigitalocean.app/")
def hello_world():
    return render_template('openai.html')


@app.route("/plankton-app-d5pi9.ondigitalocean.app/generate-img", methods=['GET', 'POST'])
def generate_img():
   
    if request.method == 'POST':
        try:
            response = openai.Image.create(
                prompt=f"{request.form['text']}",
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            return f"""
                <h1 class="result1"> {request.form['text']}</h1>
                <img style="width: 600px" src='{image_url}' alt='#'>
            """  
        except:
            return 'Ошибка генерации'  
    return render_template('openai.html')

@app.route("/plankton-app-d5pi9.ondigitalocean.app/good-project", methods=['GET', 'POST'])
def good_project():
   
    if request.method == 'POST':
        try:
            student_answer = request.form['good2'].replace(' ', '')
            student_answer = student_answer.replace('\n', '')
            student_answer = student_answer.replace('\r', '')
            true_answer = (
                'response = openai.Image.create( ' 
                'prompt=f"{request.form["text"]}", '
                'n=1, '
                'size="1024x1024" '
                ') '
                'image_url = response["data"][0]["url"] ')
            true_answer = true_answer.replace(' ', '')
            true_answer = true_answer.replace('\n', '')
            true_answer = true_answer.replace('\r', '')

            print(student_answer)
            print('---')
            print(true_answer)
            if student_answer == true_answer:
                return render_template('generate.html')
        except:
            return 'Ошибка генерации'  
    return render_template('error.html')


if __name__ == '__main__':
    app.run()
