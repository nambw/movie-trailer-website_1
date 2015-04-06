#file template provided by Udacity. Invokes the webbrowser to display the dynamically created web page of movies.
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.", 
                        "HTTP://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www/youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", 
		     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
		     "HTTP://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	             "https://www.youtube.com/watch?v=d1_JBMrrYw8")

cars = media.Movie("Cars", 
		   "While traveling to California to race against The King (Richard Petty) and Chick Hicks (Michael Keaton) for the Piston Cup Championship, Lightning McQueen (Owen Wilson) becomes lost after falling out of his trailer in a run down town called Radiator Springs. While there he slowly befriends the town's odd residents, including Sally (Bonnie Hunt), Doc Hudson (Paul Newman) and Mater (Larry the Cable Guy). When it comes time for him to leave to championship is no longer his top priority.",
                   "http://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
                   "HTTP://www.youtube.com/watch?v=uxx75HVd-F0")

KFP1 = media.Movie("Kung Fu Panda",
	           "In the Valley of Peace, Po the Panda finds himself chosen as the Dragon Warrior despite the fact that he is obese and a complete novice at martial arts.",
                    "http://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg"	,
                    "HTTP://www.youtube.com/watch?v=PXi3Mv6KMzY")

KFP2 = media.Movie("Kung Fu Panda2",
		   "Po and his friends fight to stop a peacock villain from conquering China with a deadly new weapon, but first the Dragon Warrior must come to terms with his past.",
	           "http://upload.wikimedia.org/wikipedia/en/b/b1/Kung_Fu_Panda_2_Poster.jpg",
                   "HTTP://www.youtube.com/watch?v=7GHT-TSiZio")

Dhoom3 = media.Movie("Dhoom3",
		     "To avenge his father's death, a circus entertainer trained in magic and acrobatics turns thief to take down a corrupt bank in Chicago. Two cops from Mumbai are assigned to the case.",
		     "http://upload.wikimedia.org/wikipedia/en/f/f1/Dhoom_3_Film_Poster.jpg",
		     "https://www.youtube.com/watch?v=yeF_b8EQcK0");

movie_list = [toy_story, avatar, cars, KFP1, KFP2, Dhoom3]
fresh_tomatoes.open_movies_page(movie_list)

