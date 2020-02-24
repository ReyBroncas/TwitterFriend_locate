import twitter
import location
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
@app.route('/gen')
def gen():
    return render_template('map.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        acct = request.form['twitter_acct']
        f_num = request.form['twitter_num']
        users_data = twitter.get_users_data(acct, f_num)
        if users_data:
            htmls = location.generate_map(users_data)
            context = {"html": htmls}
            return render_template('map.html', **context)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
