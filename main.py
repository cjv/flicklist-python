import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        # TODO: make a list with at least 5 movie titles        
            movie_list = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5"]

        # TODO: randomly choose one of the movies, and return it
            today = random.randrange(len(movie_list))

        return movie_list[today]


    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"
        # "<p>{movie}</p>".format(self.getRandomMovie)

        # TODO: pick a different random movie, and display it under
        tomorrow = self.getRandomMovie()
        # the heading "<h1>Tommorrow's Movie</h1>"
            content += "<h1>Tommorrow's Movie</h1>"
            content += "<p>" + tomorrow + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
