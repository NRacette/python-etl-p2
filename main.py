from datetime import datetime
import json
import requests
import pgsql
import sql


def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


if __name__ == '__main__':
    # get some movie data from the API
    # print(get_movie_data('WarGames'))
    # pgsql.query(sql.create_schema)
    # pgsql.query(sql.create_table)
    titlelist = []
    movieDict = {}
    f1 = open("datasets/json/movies.json")
    reader = json.load(f1)
    f1.close()
    for titleitems in reader:
        if titleitems["year"] >= 2018:
            titlelist.append(titleitems["title"])
    titleset = set(titlelist)
    titlelist = list(titleset)
    moviedict = {}

    # for filteritem in titlelist:
    #    moviedict[filteritem] = get_movie_data(filteritem)
    # print(titlelist)
    # f1_write = open("datasets/json/filteredmovies.json", "w")
    # json.dump(moviedict, f1_write)
    # f1_write.close()

    with open("datasets/json/filteredmovies.json", 'r') as f3:
        filteredmovies_json = json.loads(f3.read())
    f1.close()

    englishmovie = []
    for k1, v1 in filteredmovies_json.items():
        for k2, v2 in v1.items():
            if k2 == "Language":
                if "English" in v2:
                    englishmovie.append(v1)

    final_columns = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Awards",
                     "Poster"]
    final_list_NA = []
    for i in englishmovie:
        x = {key: i[key] for key in final_columns}
        final_list_NA.append(x)

    final_list = []
    for i in final_list_NA:
        if "N/A" not in i.values():
            final_list.append(i)



    for i in final_list:
        sqltable = []
        sqltable.append(i["Title"])
        sqltable.append(i["Rated"])
        date_obj = datetime.strptime(i["Released"], "%d %b %Y")
        sqltable.append(date_obj)
        sqltable.append(int(i["Runtime"][0:3].strip()))
        sqltable.append(i["Genre"].split(","))
        sqltable.append(i["Director"])
        sqltable.append(i["Writer"].split(","))
        sqltable.append(i["Actors"].split(","))
        sqltable.append(i["Plot"].strip(','))
        sqltable.append(i["Awards"].split(","))
        sqltable.append(i["Poster"])
        pgsql.query(sql.insert_movie, sqltable)

