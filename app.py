from flask import Flask, render_template
from search import search_all_kv_vt

app = Flask(__name__)
IP = '319343c0-2efc-4ada-b206-7e98ff41dd8e'


@app.route('/')
def index():
    # data_kv = search_all_kv_vt()
    # print(data_kv)
    # write_all_kv_vr_to_json()
    return render_template('index.html')
    # return render_template('index.html')


@app.route('/map')
def map_kv():
    return render_template('map.html')


if __name__ == "__main__":
    app.run(debug=True)
