import requests

BASE_URL = "https://goodreads-devf-aaron.herokuapp.com/"

def get_biography():
	get_authors = BASE_URL + "/api/v1/authors"
	response = requests.get(get_authors)
	authors_dictionnary = response.json()
	author_count = len(authors_dictionnary)
	author_name = str(input("Which author are you looking for? \n"))
	variable = None
	for i in range(0,author_count):
		if authors_dictionnary[i]['name'] == author_name:
			variable = i
		else:
			continue
	if variable == None:
		print("We couldn't find that author")
	else:
		biography = (authors_dictionnary[variable]['biography'])
		print(biography)

get_biography()

def post_new_author(nombre, apellidos, bio, nacionalidad, edad):
	post_authors = BASE_URL + "/api/v1/authors/"
	new_author = {
		"name": nombre,
		"last_name": apellidos,
		"nacionalidad": nacionalidad,
		"biography": bio,
		"gender": "F",
		"age": edad
	}
	new_author_response = requests.post(post_authors, json=new_author)
	return(new_author_response)	
name = str(input("What's the name of your author? \n"))
last_name = str(input("What's his or her last_name? \n"))
nationality = str(input("Where was he or she born? \n"))
bio = str(input("Tell us something interesting about him or her \n"))
age = int(input("How old is he or she? \n"))
new_author_response = post_new_author(name, last_name, bio, nationality, age)
print(new_author_response.status_code)

def create_new_user(email, password):
	post_user = BASE_URL + "/api/v1/users/"
	new_user = {
		"email": email,
		"password": password,
	}
	new_user_response = requests.post(post_user, json=new_user)
	return(new_user_response)	
email = str(input("What's your e-mail address? \n"))
password = str(input("Choose a password \n"))
new_user_response = create_new_user(email,password)
print(new_user_response.status_code)