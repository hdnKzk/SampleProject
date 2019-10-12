import requests
import json

# APIキーの指定
apikey = "f2e5fc287fa3addba5e9ef8d5ed7f2fb"

# 天気を調べたい都市の一覧
cities = ["Saitama,JP", "London,UK", "New York,US"]
# APIのひな型
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

#http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d69518f4c77bbc134ebb61c558342475

# 温度変換(ケルビン→摂氏)
k2c = lambda k: k - 273.15

# 各都市の温度を取得する
for name in cities:
    # APIのURLを得る
    url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url, timeout=(6, 12))
    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)
    # 結果を出力
    print("+ 都市=", data["name"])
    print("| 天気=", data["weather"][0]["description"])
    print("| 最低気温=", k2c(data["main"]["temp_min"]))
    print("| 最高気温=", k2c(data["main"]["temp_max"]))
    print("| 湿度=", data["main"]["humidity"])
    print("| 気圧=", data["main"]["pressure"])
    print("| 風向き=", data["wind"]["deg"])
    print("| 風速度=", data["wind"]["speed"])
    print("")

    # {
    #     "coord": {"lon": 139.66, "lat": 35.91},
    #     "weather": [{"id": 502, "main": "Rain", "description": "heavy intensity rain", "icon": "10d"},
    #                 {"id": 521, "main": "Rain", "description": "shower rain", "icon": "09d"},
    #                 {"id": 701, "main": "Mist", "description": "mist", "icon": "50d"}
    #                 ],
    #     "base": "stations",
    #     "main": {"temp": 297.68, "pressure": 995, "humidity": 94, "temp_min": 297.04, "temp_max": 298.71},
    #     "visibility": 2000,
    #     "wind": {"speed": 10.3, "deg": 90, "gust": 17.5},
    #     "rain": {"1h": 10.41},
    #     "clouds": {"all": 90},
    #     "dt": 1570853947,
    #     "sys": {"type": 1, "id": 8058, "country": "JP", "sunrise": 1570826673, "sunset": 1570867872},
    #     "timezone": 32400,
    #     "id": 6940394,
    #     "name": "Saitama",
    #     "cod": 200
    # }