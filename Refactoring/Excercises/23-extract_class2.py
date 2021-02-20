# by Kami Bigdely
# Extract class

class User:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year    
        self.movies = movies
        self.email = email

    def send_hiring_email(self):
        print("email sent to: ", self.email) 

    def print_movies(self):
        for movie in self.movies:
            print(movie, end=', ')
    
    def custom_method(self):
        """Custom method that can be customized for anything."""
        print(self.first_name, " ", self.last_name)
        self.print_movies()
        self.send_hiring_email()
        print()

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_years = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

users = []
    
for i, _ in enumerate(emails):
    first_name = first_names[i]
    last_name = last_names[i]
    birth_year = birth_years[i]
    movie_list = movies[i]
    email = emails[i]
    user = User(first_name, last_name, birth_year, movie_list, email)
    users.append(user)
    if user.birth_year > 1985:
        user.custom_method()
