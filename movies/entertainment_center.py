import fresh_tomatoes
import media


toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg'                        ,
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

##print toy_story.storyline

avatar = media.Movie("Avatar",
                     "a marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print avatar.storyline
#avatar.show_trailer()

in_the_mood_for_love = media.Movie("in the mood for love",
                     "a love story between maried neighbors",
                     "http://upload.wikimedia.org/wikipedia/en/4/45/In_the_Mood_for_Love_movie.jpg",
                     "https://www.youtube.com/watch?v=BnFjSHQFVkA")
##print in_the_mood_for_love.storyline
##in_the_mood_for_love.show_trailer()
f_for_fake = media.Movie("f for fake",
                         "a story about fraud",
                         "http://upload.wikimedia.org/wikipedia/en/6/69/F_for_Fake_poster.jpg",
                         "https://www.youtube.com/watch?v=TMkZWWLHGXU")
office_space = media.Movie("office space",
                           "workplace satire",
                           "http://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                           "https://www.youtube.com/watch?v=_IwzZYRejZQ")

movies  = [toy_story,avatar, in_the_mood_for_love, f_for_fake, office_space]                           

fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__
                           
