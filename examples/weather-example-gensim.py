import intentparser

intent = intentparser.intentParser({

    'description' : {
                    "type" : 'WeatherIntent',
                    "args" : [(2,"location"), (1, "weather_types")],
                    "keyword" : [
                    (0, "weather_keyword"),
                    (1, "weather_types"),
                    (2, "location")
                    ]},
    'weather_keyword' : ['is', 'are', 'weather', 'sleet', 'rain', 'humid'],
    'weather_types' : [
        "snow",
        "rain",
        "wind",
        "sleet",
        "sun"
        ],
    'location' : ' in (?P<location>.*)'
}, typeOfSim='gensim')
intent.teachWords(["Weather in Bangkok?", "Good weather in Canada?", "Is it rain in North California?"])

print(intent.getResult("Rain in Khon Kaen?"))
print(intent.getResult("Is it rain in California?"))
