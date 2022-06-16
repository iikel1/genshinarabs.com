from urllib import parse
# .env 
CLIENT_ID = 905104018869739551
TOKEN = 'OTA1MTA0MDE4ODY5NzM5NTUx.YYFNzg._EppQQt8UUSKNWKzvXJEEoGU52c'
CLIENT_SECRET = 'FeXuZx7DqGX_CDOChG-Qj90wQd_BX333'
REDIRECT_URI = 'http://localhost:5000/callback'
OAUTH_URL = f'https://discord.com/api/oauth2/authorize?client_id=905104018869739551&redirect_uri={parse.quote(REDIRECT_URI)}&response_type=code&scope=identify%20guilds'
MONGO = 'mongodb+srv://HMusic:ylmdDpyjyCv4XzMr@hutao.14vgh.mongodb.net/Hutao?retryWrites=true&w=majority'