import json
import re
import urllib

regex = r".*\/title\/\s*([^\n\r]*\/)"

with open('./movie_metadata.json') as f:
    meta_data = json.load(f)

for a in meta_data:

    if 'movie_imdb_link' in a:
        m = re.match(regex, a['movie_imdb_link'])
        if m:
            try:
                groups = m.groups()
                movie_id = groups[0].encode('ascii','ignore')
                movie_id_fixed = movie_id[:-1]

                api_url = 'http://www.omdbapi.com/?i=' + movie_id_fixed + '&plot=full&r=json'
                response = urllib.urlopen(api_url)
                data = json.loads(response.read())

                with open('movies_data.json', 'a') as outfile:
                    json.dump(data, outfile)
                    outfile.write(', ')

                with open('posters_links.json', 'a') as p:
		    p.write(data['Poster'] + '\n')

                    img_path = './images/' + movie_id_fixed + '_' + data['Title']
                    #img_url = data['Poster']
                    #urllib.urlretrieve(img_url, img_path)
                    print('New poster saved to ' + img_path)
            except:
                print ('error')
