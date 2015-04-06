#File provided by Udacity. Modified to add the storyline object
import webbrowser

class Movie():
	def __init__(self, m_title, m_story,  m_poster, m_link):
		self.title = m_title
		self.storyline = m_story
		self.poster_image_url = m_poster
		self.trailer_youtube_url = m_link

'''     	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) '''

