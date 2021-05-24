from flask import Flask, render_template
from flask import request
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='main')


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/power", methods=['GET'])
def power():
  searchText = request.args.get("s")
  site = "https://www.coolpc.com.tw/eachview.php?IGrp=15"
  response = requests.get(site)
  soup = BeautifulSoup(response.text, "html.parser")
  titles = soup.find_all("div", class_="t")
  searchdata = []
  for title in titles:
    str = title.getText()
    try:
      sin = str.find(searchText)
    except:
      sin = -1
    if sin != -1:
      searchdata.append({'title': str})
  jsonChang = json.dumps({'data': searchdata}, indent = 4)
  return jsonChang

  if __name__ == '__main__':
    app.run()