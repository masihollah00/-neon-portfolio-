
from flask import Flask, render_template_string
import os

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>سایت شخصی من</title>
<style>
*{box-sizing:border-box}
body{
 margin:0;background:#080816;color:white;
 font-family:Tahoma,Arial,sans-serif;
 text-align:center;min-height:100vh;
 display:flex;align-items:center;justify-content:center;
 padding:20px
}
main{
 width:100%;max-width:650px;padding:35px 20px;
 border:1px solid #00f7ff;border-radius:22px;
 box-shadow:0 0 25px #00f7ff55
}
h1{color:#00f7ff;text-shadow:0 0 15px #00f7ff}
p{color:#d2d2e8;line-height:2}
section{
 margin-top:22px;padding:18px;
 border:1px solid #a855f7;border-radius:14px
}
a{
 display:inline-block;margin:15px;padding:12px 22px;
 background:#00f7ff;color:#080816;
 border-radius:9px;text-decoration:none;font-weight:bold
}
</style>
</head>
<body>
<main>
<h1>⚡ سلام، من برنامه‌نویسم!</h1>
<p>به سایت شخصی نئونی من خوش اومدی 🚀</p>
<section>
<h2>👨‍💻 درباره من</h2>
<p>من به برنامه‌نویسی پایتون و طراحی سایت علاقه دارم.</p>
</section>
<section>
<h2>🔥 پروژه‌های من</h2>
<p>اینجا قراره پروژه‌های جذابم رو معرفی کنم.</p>
</section>
<a href="https://github.com/">گیت‌هاب من</a>
</main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
