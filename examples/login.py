import amino

client = amino.Client()
client.login(email='YOUR EMAIL', password='YOUR PASSWORD')

print(client.profile.nickname)