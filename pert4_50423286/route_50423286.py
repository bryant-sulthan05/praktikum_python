from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/about')
def about():
  return 'This is the about page'

@app.route('/hello/<name>')
def hello_name(name):
  return f'Hello {name}'

@app.route('/rev/<int:postID>')
def show_blog(postID):
  return f'Blog Number {postID}'

@app.route('/rev/<float:revNo>')
def revision(revNo):
  return f'Revision Number {revNo}'

# Tugas : Menambah 3 route
@app.route('/profile')
def my_profile():
  return render_template('profile.html')

@app.route('/luas_segitiga', methods=['GET', 'POST'])
def luas_segitiga():
    if request.method == 'POST':
        alas = float(request.form['alas'])
        tinggi = float(request.form['tinggi'])
        rumus = float((1/2) * alas * tinggi)
        return render_template('luas_segitiga.html', hasil=rumus)
    else:
        return render_template('luas_segitiga.html', hasil='---')


if __name__ == '__main__':
  app.run(debug=True)