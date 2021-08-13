from flask import Flask, render_template
from search import search_all_kv_vt, write_all_kv_vr_to_json

app = Flask(__name__)
IP = '319343c0-2efc-4ada-b206-7e98ff41dd8e'


@app.route('/')
def index():
    search_all_kv_vt()
    write_all_kv_vr_to_json()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
