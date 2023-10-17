from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return '<p>Mijn huiswerk voor les 10 heb ik veel te lang over gedaan omdat ik de voorgeprogrammeerde website van NHA probeerde te pimpen</p>'

if __name__ == '__main__':
    app.run(port=5000,debug=True)
