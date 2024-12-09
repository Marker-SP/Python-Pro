from flask import Flask
import random

app = Flask(__name__)

a = "According to a study conducted in 2018, more than %50 of people aged 18-34 are addicted to their smartphones."
b = "The study of technological addiction is one of the most relevant areas of modern scientific research. According to a 2019 study, more than %60 of people respond to work messages on their smartphones within 15 minutes of leaving work."
c = "One way to combat technological addiction is to seek out activities that provide pleasure and improve mood."
d = "Elon Musk claims that social networks are designed to keep us inside the platform so that we spend as much time as possible viewing content. Elon Musk also advocates for the regulation of social networks and the protection of users personal data. He claims that social networks collect large amounts of information about us, which is then used to influence our thoughts. and claims that it can be used to manipulate our behavior."
e = "Social networks have positive and negative aspects, and we must be aware of both when using these platforms."

@app.route("/")
def hello():
    return f'<h1>Hello, change the URL to "/facts".</h1>'

@app.route("/facts")
def facts():
    return f'<h1>{random.choice(facts_list)}</h1>'

facts_list= [a, b, c, d, e]



@app.route("/randomnumber")
def egg():
    return f'<h1>{random.randint(0, 100000)}</h1>'

app.run(debug=True)
