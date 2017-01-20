import media
import fresh_tomatoes

# (Create multiple instances of the movie class  to represent your favorite
# movies)

kill_bill = media.Movie("Kill BIll",
                        "The revenge of a widow",
                        "http://fr.web.img2.acsta.net/medias/nmedia/18/35/13/"
                        "44/18364816.jpg",
                        "https://www.youtube.com/watch?v=7kSuas6mRpk")


dallas_buyers_club = media.Movie("Dallas Buyers Club",
                                 "The story of hustler who works around the "
                                 "system to help AIDS patients get the "
                                 "medication they need after he is diagnosed "
                                 "with the disease",
                                 "http://fr.web.img3.acsta.net/pictures/14/01/"
                                 "24/12/09/007448.jpg",
                                 "https://www.youtube.com/watch?v=U8utPuIFVnU")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in "
                           "space in an attempt to ensure humanity's survival",
                           "http://fr.web.img6.acsta.net/pictures/14/09/24/12/"
                           "08/158828.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movie_library = [kill_bill, dallas_buyers_club, interstellar]  # Create a
# list of your favourites movies
fresh_tomatoes.open_movies_page(movie_library)  # Display your favorites
# movies+ in a web browser
