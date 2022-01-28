import unirest

unirest.timeout(15) # 5s timeout

RAPIDAPI_KEY  = "af12bcdb37msh3c717ac32d4c52ep123283jsn9af19b639252"
RAPIDAPI_HOST =  "imdb8.p.rapidapi.com"

def search_movie(search_keyword):

	response = unirest.get("https://imdb8.p.rapidapi.com/title/find?q="+search_keyword,
	  headers={
	    "X-RapidAPI-Host": RAPIDAPI_HOST,
	    "X-RapidAPI-Key": RAPIDAPI_KEY,
	    "Content-Type": "application/json"
	  }
	)

	return response

def get_ratings(search_keyword):
    response = unirest.get("https://imdb8.p.rapidapi.com/title/get-ratings?tconst="+search_keyword,
	  headers={
	    "X-RapidAPI-Host": RAPIDAPI_HOST,
	    "X-RapidAPI-Key": RAPIDAPI_KEY,
	    "Content-Type": "application/json"
	  }
	)
    return response

def Ratings():
    search_string=""
    while len(search_string) <= 2:
        search_string = raw_input("Enter the movie name to search: ")
            
        print(search_string)
    main_response= search_movie(search_string)
    if(main_response.code == 200):
        if "results" in main_response.body:
            print("Yes.....You Got IT")
            best_match = main_response.body["results"][0]
            ratings = get_ratings(best_match['id'].split("/")[2])
            print(ratings.body['rating'])
            
        else:
            print("No such movie")

Ratings()
