<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, flash, Blueprint, session, abort, current_app, escape, url_for
import pandas as pd
import pickle
import psycopg2
import psycopg2.extras
import os
import pathlib
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from pip._vendor import cachecontrol
from flask_mail import Mail, Message
from oauth2client.contrib.flask_util import UserOAuth2
import requests
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

#####로그인세션########
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
s = URLSafeTimedSerializer('이것은시크릿!')

GOOGLE_CLIENT_ID = "413604575504-avbhaie5t3mr91qfhosf8s2hjq875iin.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file = client_secrets_file,
    scopes = ["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost:5000/callback")

conn = psycopg2.connect(
    host='heffalump.db.elephantsql.com', 
    dbname='hezwfjbb',
    user='hezwfjbb',
    password='bwf3k0irq7kZDzoMrnUV2ZXxRD7fXkhZ')

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'leechangso1@gmail.com'
MAIL_PASSWORD = 'dkohoevrzyjinnqn'
#############
=======
from flask import Flask, render_template, request
import pandas as pd
import pickle
>>>>>>> d5239a0c140c3f9a7920c288f059c24c4156fda8

def create_app():

    app = Flask(__name__)
<<<<<<< HEAD
    app.secret_key = 'super secret key'

=======
    
>>>>>>> d5239a0c140c3f9a7920c288f059c24c4156fda8
    @app.route('/')
    def index():
        return render_template('index.html'), 200
    
<<<<<<< HEAD
    @app.route('/notice')
    def notice():
        return render_template('notice.html'), 200
    
    @app.route('/login')
    def login():
        return render_template('login.html'), 200
    
    @app.route('/regist')
    def regit():
        return render_template('regist.html'), 200

    @app.route('/service')
    def service():
        return render_template('service.html'), 200

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html'), 200
    
    ###############################################################################################
   
    @app.route('/login',methods=["POST"])
    def login_post():
        email = request.form.get('email')
        pw = request.form.get('pw')

        ## 기존 db에서 이메일 유무 확인
        cur.execute("""select u.email, u.password From users u where u.email = %s""", (email,))
        userinfo_DB = cur.fetchone()

        if userinfo_DB :
            db_email = userinfo_DB[0]
            db_pw = userinfo_DB[1]
        else :
            db_pw = None
            db_email = None

        if email == db_email :
            ## 비밀번호 해쉬 체크 => 일치하면 로그인(protect_area 이동)
            if db_pw == pw :
                session['email'] = email
                flash('로그인 되었습니다.')
                return redirect('/')
            else :
                flash("비밀번호가 일치하지 않습니다.")
                return redirect('/login')
        else :
            flash("이메일 정보가 없습니다.")
            return redirect('/login')
    
    @app.route('/logout')
    def logout():
        session.clear()
        flash('로그아웃 되었습니다.')
        return redirect(url_for("login"))

    ############################################################################################

    @app.route('/regist', methods=['GET', 'POST'])
    def regist_post() :
        id = request.form.get('id')
        pw = request.form.get('pw')
        pw2 = request.form.get('pw2')
        email = request.form.get('email')

        id = str(id)
        email = str(email)
        pw = str(pw)
        pw2 = str(pw2)

        ## id 중복 확인
        cur.execute("""select * From users u where u.user_id = %s""", (id,))
        id_account = cur.fetchone()

        ## email 중복 확인
        cur.execute("""select * From users u where u.email = %s""", (email,))
        email_account = cur.fetchone()
    
        if id_account :
            flash('이미 존재하는 ID입니다.')
            return render_template("regist.html")

        elif email_account :
            flash('이미 존재하는 email입니다.')
            return render_template("regist.html", id=id)

        elif pw != pw2 :
            flash("비밀번호가 일치하지 않습니다!")
            return render_template("regist.html", id=id, email=email)

        else : 
            flash(f'{email}로 인증 메일이 발송되었습니다!')
            current_app.config['MAIL_SERVER'] = MAIL_SERVER
            current_app.config['MAIL_PORT'] = MAIL_PORT
            current_app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
            current_app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
            current_app.config['MAIL_USERNAME'] = MAIL_USERNAME
            current_app.config['MAIL_PASSWORD'] = MAIL_PASSWORD


            ## 인증 메일보내기

            mail = Mail(current_app)

            if request.method == 'GET' :
                return '<form action="/email" method="POST"><input name="email"><input type="submit"></form>'
            email = request.form['email']
            token = s.dumps(email, salt='email-confirm')

            session['MAIL_TOKEN'] = token
            session['user_id'] = id
            session['user_password'] = pw
            session['user_email'] = email

            msg = Message('Confirm Email', sender = "leechangso1@gmail.com", recipients=[email])

            msg.body = """인증번호는 {} 입니다. 5분 안에 인증번호를 입력해주세요.""".format(token)
            mail.send(msg)
            return render_template("confirm.html")
   
    ###########################################
    
    @app.route('/confirm', methods=['POST', 'GET'])
    def confirm_email():
        if session['MAIL_TOKEN'] :
            token = '%s' % escape(session['MAIL_TOKEN'])
            certification_num = request.form.get('certification_num')

            user_id = '%s' % escape(session['user_id'])
            password = '%s' % escape(session['user_password'])
            email = '%s' % escape(session['user_email'])

            if token == certification_num:
                cur.execute("""insert into users ("user_id", "password", "email") values(%s, %s, %s)""", (user_id, password, email))
                conn.commit()
                flash('축하합니다. 회원가입이 완료되었습니다!')
                return render_template('login.html')
            else :
                flash('인증번호가 일치하지 않습니다.')
                return render_template('confirm.html')
        else :
            flash('처음부터 다시 시작해주세요.')
        return render_template('confirm.html')
    
    ####################################################

    @app.route('/service/predict', methods=["GET","POST"])
    def price_predict():
        if request.method == "POST":
            
            price = request.form['price']
            location = request.form['location']
            unused = request.form['unused']
            model = request.form['model']
            series = request.form['series']
            size = request.form['size']
            gps = request.form['gps']
            edition = request.form['edition']
            material = request.form['material']
            quality = request.form['quality']

            modeling = None
            with open('price_app/pipe.pkl','rb') as pickle_file:
                modeling = pickle.load(pickle_file)
                
            df = pd.DataFrame([[price, unused, location, model, series, size, gps, edition,
            material, quality]],
            columns=['price','unused','location','model','series','size','gps/cell','edition',
            'material','quality'])
            
            X_test = df
            y_pred = modeling.predict(X_test)
            
            if y_pred < 1:
                predict_price = int(price) - round(y_pred[0] * int(price) * 0.2)
            elif (1 <= y_pred) and (y_pred < 7):
                predict_price = int(price) - round(y_pred[0] * int(price) * 0.1)
            elif (7 <= y_pred) and (y_pred < 15):
                predict_price = int(price) - round(y_pred[0] * int(price) * 0.05)
            else:
                predict_price = round(y_pred[0] * int(price) * 0.05) + int(price)

            return render_template('./service.html', predict = predict_price, pred=y_pred) , 200

    @app.route('/google_login')
    def google_login():
        authorization_url, state = flow.authorization_url()
        session["state"] = state
        return redirect(authorization_url)

    @app.route('/callback')
    def callback():
        flow.fetch_token(authorization_response=request.url)

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID)
        session["google_id"] = id_info.get("sub")
        session["name"] = id_info.get("name")
        return redirect("/")
    
    def login_is_required(function):
        def wrapper(*args, **kwargs):
            if "email" in session or "google_id" in session :
                return function()
            else :
                return function()
        return wrapper

    return app
=======
    
    @app.route('/service.html')
    def service():
        return render_template('service.html'), 200

    @app.route('/dashboard.html')
    def dashboard():
        return render_template('dashboard.html'), 200



    @app.route('/service.html/predict', methods=["POST"])
    def price_predict():
        if request.method == "POST":
            
            degree = request.form['manner_degree']
            price = request.form['price']
            chat = request.form['chat']
            view = request.form['view']
            time = request.form['time']
            attention = request.form['attention']
            open_closed = request.form['open_closed']
            modelname = request.form['modelname']
            discounted = request.form['discounted']
            origin_price = request.form['origin_price']

            modeling = None
            with open(r'C:\Users\woals\AI_13\qqq\flask\clf.pkl','rb') as pickle_file:
                modeling = pickle.load(pickle_file)
                
            df = pd.DataFrame([[degree, price, chat, view, time,attention, open_closed, modelname,
            discounted, origin_price]],
            columns=['manner_degree','price','chat','view','time','attention','open_closed',
            'model','discounted','origin_price'])
            X_test = df
            y_pred = modeling.predict(X_test)
            
            predict_price = round(y_pred[0],2) * price

            return render_template('service.html/', predict = predict_price) , 200

    return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)
>>>>>>> d5239a0c140c3f9a7920c288f059c24c4156fda8
