import csv
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open('final.csv',"a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

for movie in all_movies:
    poster_found = any(movie[8]in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_items in all_movie_links:
            if movie[8] == movie_link_items[0]:
                movie.append(movie_link_items[1])
                if len(movie) == 28:
                    with open('final.csv',"a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie) 