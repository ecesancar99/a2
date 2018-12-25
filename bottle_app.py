from bottle import route, run, default_app, debug, static_file, route, request
from hashlib import sha256

# The following step is taken from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


password = '9d777935627a29c77604c57273520eb42635fd1847d2eeea1e7441fbaeb26253'

@route('static/<filename>')
def static_file_callback(filename):
    return static_file(filename, root='./static')
route('/static/<filename>', 'GET', static_file_callback)

comment_adding = '''<form action = "/static/index.html" method = "post">
	<fieldset>
	<legend>Visitors's Comments:</legend>
	<legend>Your Comment:</legend>
	<textarea name="comment" rows="5" cols="100">Please write your comments here :)</textarea>
	<legend>Password:</legend>
    <input type = "password" name = "password" ><br>
    <input type = "submit" name="submit">
    </fieldset>
    <br/>
    <br/>
    </form>
    '''
all_comments = []

evaluation_adding = '''<form action = "/static/index.html" method = "post">
    <fieldset>
    <legend> Visitors' Evaluations: <legend>
    <legend> Which point do you give to this website? </legend>
    <select name ="points">
        <option value="0"> 0 </option>
        <option value="1"> 1 </option>
        <option value="2"> 2 </option>
        <option value="3"> 3 </option>
        <option value="4"> 4 </option>
        <option value="5"> 5 </option>
    </select>
    <legend>Password:</legend>
    <input type = "password" name = "password" ><br>
    <input type = "submit" name="submit">
    </fieldset>
    </form>'''
all_evalutions =[]



@route('/static/index.html')
def comment_section():
	page = '''<!DOCTYPE html>
    <html>
        <head>
    		<title> That '70's show </title>
    		<link rel="stylesheet" href="styles.css">
    		<meta charset="UTF-8">
    		<link rel="icon" href="logo.png">
    	</head>

    	<body>
    		<br>
    		<div class="navbar">
    		<ul style="background-color:DimGray;">
    		<li> <a href="index.html"> Home </a></li>
    		<li> <a href="seasons.html">Seasons</a></li>
    		<li> <a href="characters.html"> Characters</a></li>
    		<li> <a href="cast.html"> Cast</a></li>
    		<li> <a href="howdotheylooklikenow.html"> How do they look like now!</a></li>
    		</ul>
    		</div>

    		<br>
    		<div class="index">
    		<img src="logo.png" alt="That 70's Show!">
    		</div>

            <p> That 70's show was a sit-com about 6 teens adventures living in the town of Wisconsin in 70's. The show last
    	8 seasons and was aired on FOX from <em>1998 to 2006.</em> The main characters are <b> Eric, Donna, Fez, Michael, Jackie,
    	and Hyde. </b> </p> <blockquote cite="http://that70sshow.wikia.com/wiki/That_%2770s_Show">Eric Forman is a nerdy teenage boy; Donna Pinciotti is the feminist
    	next-door neighbor and Eric's girlfriend; Steven Hyde, a cynical, hard-rocking stoner and Eric's childhood friend; Michael Kelso,
    	a dim-witted,
    	narcissistic ladies man; Jackie Burkhart, a self-involved high school cheerleader overly preoccupied with wealth and status; and
    	Fez, a sometimes goofy foreigner, whose country of origin is ambiguous, whose real name is unknown to all but him, and whose
    	hormones are, at times, out of control. Eric drives a 1969 Vista Cruiser, a station wagon given to him by his father in the first
    	episode.Other main characters include Red Forman, Eric's overbearing war veteran father, obsessed with making "...him a man,
    	which he's not" and using the word "dumb-ass" frequently plus always threatening people with putting his 'foot in your ass';
    	Eric's overprotective mother, Kitty, who is caught up in trying to be a full-time mom and housewife, while maintaining a job as a
    	nurse in a local hospital; and Laurie Forman, the promiscuous older sister who can do no wrong in the eyes of her father. The show
    	also follows the relationship of Bob Pinciotti and Midge Pinciotti, Donna's parents, both of whom are slow witted and easily
    	influenced by the movements and fads of the '70s, which sometimes places stress on their marriage. Tommy Chong also appears as
    	the recurring character of Leo, the stoner owner of the Foto Hut. </blockquote>
    		 <br>
    		 <br>
    		 <p style="text-align:center;">Theme song of this show is <em> In The Street</em>. You can listen the
    	song from <a href= "https://www.youtube.com/watch?v=yZFdKW43yGM"> here </a>. The lyrics are as follows:<br>
    		Hanging out, down the street<br>
    		The same old thing, we did last week <br>
    		Not a thing to do, but talk to you<br>
    		We're all alright! We're all alright!</p>


    	</body>
    </html>

			''' + comment_adding + evaluation_adding

	i = 1
	page = page+ "<p>Visitors' Comments and Evalutions:<br><p>"
	for x in all_comments:
			page = page+ "<p>%d. %s<br></p>" + all_evalutions[i-1]% (i, x)
			i=i+1
	return page


@route('/static/index.html', method='POST')
def post_comment():
	page = '''<!DOCTYPE html>
    <html>

    	<head>
    		<title> That '70's show </title>
    		<link rel="stylesheet" href="styles.css">
    		<meta charset="UTF-8">
    		<link rel="icon" href="logo.png">
    	</head>

    	<body>

    		<br>
    		<div class="navbar">
    		<ul style="background-color:DimGray;">
    		<li> <a href="index.html"> Home </a></li>
    		<li> <a href="seasons.html">Seasons</a></li>
    		<li> <a href="characters.html"> Characters</a></li>
    		<li> <a href="cast.html"> Cast</a></li>
    		<li> <a href="howdotheylooklikenow.html"> How do they look like now!</a></li>
    		</ul>
    		</div>

    		<br>
    		<div class="index">
    		<img src="logo.png" alt="That 70's Show!">
    		</div>



    		<p> That 70's show was a sit-com about 6 teens adventures living in the town of Wisconsin in 70's. The show last
    	8 seasons and was aired on FOX from <em>1998 to 2006.</em> The main characters are <b> Eric, Donna, Fez, Michael, Jackie,
    	and Hyde. </b> </p> <blockquote cite="http://that70sshow.wikia.com/wiki/That_%2770s_Show">Eric Forman is a nerdy teenage boy; Donna Pinciotti is the feminist
    	next-door neighbor and Eric's girlfriend; Steven Hyde, a cynical, hard-rocking stoner and Eric's childhood friend; Michael Kelso,
    	a dim-witted,
    	narcissistic ladies man; Jackie Burkhart, a self-involved high school cheerleader overly preoccupied with wealth and status; and
    	Fez, a sometimes goofy foreigner, whose country of origin is ambiguous, whose real name is unknown to all but him, and whose
    	hormones are, at times, out of control. Eric drives a 1969 Vista Cruiser, a station wagon given to him by his father in the first
    	episode.Other main characters include Red Forman, Eric's overbearing war veteran father, obsessed with making "...him a man,
    	which he's not" and using the word "dumb-ass" frequently plus always threatening people with putting his 'foot in your ass';
    	Eric's overprotective mother, Kitty, who is caught up in trying to be a full-time mom and housewife, while maintaining a job as a
    	nurse in a local hospital; and Laurie Forman, the promiscuous older sister who can do no wrong in the eyes of her father. The show
    	also follows the relationship of Bob Pinciotti and Midge Pinciotti, Donna's parents, both of whom are slow witted and easily
    	influenced by the movements and fads of the '70s, which sometimes places stress on their marriage. Tommy Chong also appears as
    	the recurring character of Leo, the stoner owner of the Foto Hut. </blockquote>
    		 <br>
    		 <br>
    		 <p style="text-align:center;">Theme song of this show is <em> In The Street</em>. You can listen the
    	song from <a href= "https://www.youtube.com/watch?v=yZFdKW43yGM"> here </a>. The lyrics are as follows:<br>
    		Hanging out, down the street<br>
    		The same old thing, we did last week <br>
    		Not a thing to do, but talk to you<br>
    		We're all alright! We're all alright!</p>


    	</body>
    </html>

			''' + comment_adding + evaluation_adding
	if request.POST and (create_hash(request.POST['password'])) == password:
		print(5)
		all_comments.append(request.POST['comment'])

	i = 1
	page = page + "<p>Visitors' Comments:<br><p>"
	for x in all_comments:
			page = page + "<p>%d. %s<br><p>" % (i, x)
			i=i+1

	return page




#####################################################################
# Don't alter the below code.
# It allows this website to be hosted on Heroku
# OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()
