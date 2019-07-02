import io
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
    bi = io.BytesIO()  # 分配内存空间  创建一个BytesIO对象，用于在内存中存储二维码图像数据
    img.save(bi, "png")  # 调用img对象的save方法，将二维码图像数据以PNG编码格式写入bi对象管理的内存空间
    bi.seek(0)  # 将bi对象内部的位置指针移动到图像数据的起始位置
    return flask.send_file(bi, "image/png")
    # return '<img src= "data:image/png;base64,"/>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)