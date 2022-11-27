from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    msg = "登录"
    return render_template("index.html", data=msg)  # 加入变量传递


@app.route('/news')  # 增加一个news页面
def newspage():
    newsContent = "全国上下一心支持武汉，武汉加油！"
    return render_template("news.html", data=newsContent)


@app.route('/product/<a>', methods=['GET'])  # 增加一个 product 页面 并传递参数
def productpage(a):
    return render_template("product.html", data=a)


@app.route('/login')
def loginpage():
    return render_template("login.html")


@app.route('/loginProcess', methods=['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']  # 获取姓名文本框的输入值
        pwd = request.form['pwd']  # 获取密码框的输入值
        if nm == 'dio' and pwd == '123':
            return render_template("index.html", data=nm)  # 使用跳转html页面路由
        else:
            return 'the username or userpwd does not match!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
