import media  # Contains the class Movie
import fresh_tomatoes  # Contains the webpage markup and style sheets


toy_story = 		media.Movie("Toy Story",
						"Toys that come to life.",
            			"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  
                       	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

jaws =				media.Movie("Jaws",
						"A killer shark terrorizes a beach community.",
            			"https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",
            			"https://www.youtube.com/watch?v=ucMLFO6TsFM")
    
love_and_death = 	media.Movie("Love and Death",
						"Nitwit becomes war hero - gets married.",
            			"https://upload.wikimedia.org/wikipedia/en/7/73/Love_and_death.jpg",
            			"https://www.youtube.com/watch?v=ESMIOnDD3Gg")

inside_out = 		media.Movie("Inside Out",
						"A peek inside a young girl's head.",			
						"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
						"https://www.youtube.com/watch?v=seMwpP0yeu4",)

apollo_13 = 		media.Movie("Appolo 13",			
						"Houston we have a problem.",
						"https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
						"https://www.youtube.com/watch?v=KtEIMC58sZo")

Anna_and_the_king = media.Movie("Anna and the King",
						"An English widow becomes a school teacher in Siam",
						"https://upload.wikimedia.org/wikipedia/en/5/5d/Anna_and_the_king.jpg",
						"https://www.youtube.com/watch?v=s_RO3S-KniE")


movies = [toy_story, jaws, love_and_death, inside_out, apollo_13, Anna_and_the_king]

fresh_tomatoes.open_movies_page(movies)  # pass the movie instances into 
										 # html and open the webpage
