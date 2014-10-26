import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.co/watch?v=-9ceBgWV8io")

amelie = media.Movie("Amelie",
                     "An introvert creates her own karma",
                     "http://www.movieposters101.com/gallery/Hollywood/2001/Am%C3%A9lie/2013/7/8/Am%C3%A9lie_2001_Movie_Poster_5_fadup_movieposters101(com).jpg",
                     "http://youtu.be/sECzJY07oK4")
movies = [toy_story, avatar, amelie]
fresh_tomatoes.open_movies_page

#print(avatar.storyline)
#print(toy_story.storyline)
#print(toy_story.poster_image_url)
#avatar.show_trailer()
#amelie.show_trailer()

