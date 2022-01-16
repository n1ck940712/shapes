# Assessment

Completed by Nicholas Hoo on 16 January 2022, for more info check screenshots included in repo.
A Django RESTful API complete with user registration, login, access token refresh. 

Users are able to create new shapes, list, delete, update and query the perimeter and area of specific shapes. Users are only able to query the information of the shapes created by themselves. Information of the shapes (excluding the area and perimeter) are stored in SQLite database. Area and perimeter of the shapes are computed  on-the-fly.   

Shapes are created with the input as stated:

 - Type: rectangle, triangle, square, diamond
 - Width: width of the shape
 - height: height of the shape

Image below depicts example of shapes created.
![example of created shapes](https://github.com/n1ck940712/shapes/blob/main/screenshots/example_of_created_shapes.png?raw=true?raw=true)

# How to get it running
- Clone to directory from GitHub repo https://github.com/n1ck940712/shapes
- Below is the exact lines of code for me to get it running on a fresh machine
```
git clone https://github.com/n1ck940712/shapes shapes

cd shapes

virtualenv -p python3.8 env

source env/bin/activate 

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```
- API is now up and running



# Specifications
 - Framework: Djangorestframework
 - platform: Ubuntu 20.04 
 - database: SQLite 



# API Documentation
### <ins>User registration</ins>
	POST > http://localhost:8000/auth/register/
Allow user to register for a new account. 
|Form data||
|--|--|
| username (required)| username |
| password (required)| password|
| password2  (required)| confirm password|
| email (required)| email address|
| first_name  (required)| first name of user |
| last_name  (required)| last name of user |

### <ins>User login</ins>
	POST > http://localhost:8000/auth/login/
Allow user to login. Returns refresh token and access token. Use refresh token to update access token as mention below. Access token is required for all of the shapes CRUD requests.
|Form data||
|--|--|
| username (required)| username
| password (required)| password

### <ins>Access token refresh </ins>
	POST > http://localhost:8000/auth/login/refresh/
Allow user to refresh expired access token. Returns new access token.
|Form data||
|--|--|
| refresh (required)| {refresh token}|

### <ins>List all shapes</ins>
	GET > http://localhost:8000/shapes/
Allow user to list all shapes created by themselves. Returns list of shapes minus the area and perimeter.
|Headers||
|--|--|
| Authorization (required)|Bearer {access token}|

### <ins>Create shape</ins>
	POST > http://localhost:8000/shapes/create/
Allow user create shape. Returns information of created shape.
|Headers||
|--|--|
| Authorization (required)|Bearer {access token}|
 
|Form data||
|--|--|
|type (required)|type of shape (options: triangle, rectangle, diamond, square)|
|width (required)|width of shape|
|height (required)|height of shape|

### <ins>Update shape</ins>
	PUT > http://localhost:8000/shapes/update/{id}/
Allow user update  shape created.`id` is the id of the shape. to be updated.  Returns information of updated shape. 
|Headers||
|--|--|
| Authorization (required)|Bearer {access token}|
 
|Form data||
|--|--|
|type (required)|type of shape (options: triangle, rectangle, diamond, square)|
|width (required)|width of shape|
|height (required)|height of shape|

### <ins>Delete shape</ins>
	DELETE > http://localhost:8000/shapes/delete/{id}/
Allow user delete shapes created. `id` is the id of the shape to be deleted. Returns `Null`.
|Headers||
|--|--|
| Authorization (required)|Bearer {access token}|

### <ins>Get area and perimeter of shape</ins>
	GET > http://localhost:8000/shapes/{id}/
Allow user to query the area and perimeter of shape. `id` is the id of the shape to be deleted. Returns information of shape, including area and perimeter (computed on-the-fly).
|Headers||
|--|--|
| Authorization (required)|Bearer {access token}|


