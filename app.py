import os
from config import *
from flask import Flask, render_template, request, session, redirect, url_for, send_from_directory
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized
import pymongo
from resources.character import endpoint_list
from resources.team import team

app = Flask(__name__)

os.environ["OAUTHLIB_INSECURE_TR.ANSPORT"] = "true"

app.config['SECRET_KEY'] = 'yoimiya'
app.config["DISCORD_CLIENT_ID"] = CLIENT_ID
app.config["DISCORD_CLIENT_SECRET"] = CLIENT_SECRET 
app.config["DISCORD_REDIRECT_URI"] = REDIRECT_URI
app.config["DISCORD_BOT_TOKEN"] = TOKEN


discord = DiscordOAuth2Session(app)

myclient = pymongo.MongoClient(MONGO)
mydb = myclient["commands"]
mycol = mydb["builds"]
players = myclient["players"]
iddb = players["id"]

admins = [853311019509481523]

@app.route("/", methods=['GET', 'POST'])
def home():
    if discord.authorized :
        user = discord.fetch_user()
        try :
            fin = {f"{user.id}": {"$gt": "1"}}
            for i in iddb.find(fin):
                userid = i[f"{user.id}"]
        except: userid = 'لم تقم بتسجيل الأيدي الخاص بك'
        return render_template('index.html', authorized=discord.authorized, current_user=user,admins=admins, userid=userid,team=team)
    else :
        return render_template('index.html', team=team)

 
@app.route("/oauth")
def login():
    return discord.create_session(scope=['identify', 'guilds'])
    
@app.route("/callback")
def callback():
    discord.callback()
    return redirect('/')

@app.route("/logout")
@requires_authorization
def logout():
    discord.revoke()
    return redirect('/')


@app.route("/admin", methods=['GET', 'POST'])
@requires_authorization
def admin():
    user = discord.fetch_user()
    if user.id in admins:
        x = (mycol.find())
        data = []
        for i in x :
            data.append(i)

        if request.method == 'POST':
            cmdname = request.form['cmdname']
            build = request.form['link1']
            lvl = request.form['link2']
            aliases = (request.form['aliases']).split(' ')
            newcommand = {
                'name' : f'{cmdname}',
                'images' : [f'{build}', f'{lvl}'],
                'aliases' : aliases
            }
            mycol.insert_one(newcommand)
            return render_template('admin.html', submit=True, cmdname=cmdname, aliases=aliases)
        else:
            return render_template('admin.html', submit=False, data=data)
    else :
        return redirect('/')

@app.route('/library')
def library():
    return render_template('library.html', data=endpoint_list)


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect('/')

for endpoint in endpoint_list:
    name = endpoint['name']
    app.add_url_rule(f"/library{endpoint['route']}", view_func=endpoint['view_func'], defaults = {"name" : endpoint['name'], "data" : endpoint})

if __name__ == '__main__':
    app.run(debug=True)