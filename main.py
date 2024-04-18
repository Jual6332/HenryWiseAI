class User():
  def init(self):
    self.email = "";
    self.username = "";
    self.password = "";
    self.firstName = "";
    self.lastName = "";
  def setEmail(self,email):
    self.email = email
  def getEmail(self):
    return self.email

class Movie():
  def init(self):
    self.title = "";
    self.year = "";
    self.genre = [];
    self.ranking = "";
    self.blurb = "";
  def setTitle(self,title):
    self.title = title
  def getTitle(self):
    return self.title
  def setGenre(self,genre):
    self.genre = genre

users = []

# Create a movie instance for Dune 2
duneTwo = Movie();
duneTwo.setTitle("Dune: Part Two")
duneTwo.setGenre(['action','adventure','drama']);

movies = []
movies.append(duneTwo)

print(movies[0].getTitle())


# On the Movies page, have Movies on the top row and TV shows on the bottom row
