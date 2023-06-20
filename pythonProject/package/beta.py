from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello Flask!"

# 외부 패키지 설치해서 사용하는 법

# 패키지 다운법
# Python Package로 가기 _ 원하는 거 검색
# PyPI - Flask
# PyPI는 파이썬 개발자들이 패키지를 올리는 곳이다.

# 결국 app은 main()을 꾸며준다