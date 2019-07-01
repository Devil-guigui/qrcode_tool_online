import flask
import qrcode

app = flask.Flask(__name__)

@app.route("/")
def home():
    # # 第一步：获取要生成二维码的数据
    # data = flask.request.args.get("data")

    # # 第二步，生成二维码图像
    # img = qrcode.make(data)
    # img.save(r"D:\C\Python实训\day6\代码\qrcode_tool_online\static\qr.png")
    # # 第三步：在页面显示二维码图片
    # return '<img src= "static/qr.png"/>'
    return flask.render_template('qr_tool.html')

@app.route("/qr", methods=["POST"])
def qr():
    data = flask.request.form.get("data")
    img = qrcode.make(data)
    img.save(r"D:\C\Python实训\day6\代码\qrcode_tool_online\static\qr.png")
    return '<img src= "static/qr.png"/>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)