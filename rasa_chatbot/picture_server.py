from flask import Flask, send_file

app = Flask(__name__)


@app.route('/plot/<path:path>')
def get_image(path):
    plot_path = f'plot/{path}'

    return send_file(plot_path) #mimetype is infered automatically


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4321)