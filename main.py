#yokokato
#mix words

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		#self.response.write('Hello, <i>STEP</i> World!')
		self.response.write('<title>step.week5.mixer.yoko</title>')
		self.response.write('<body><h1>put two words in the mixer!</h1>')
		self.response.write('<form>word1:<input type=text name=a><br>')
		self.response.write('word2:<input type=text name=b><br>')
		self.response.write('<input type=submit>')
		self.response.write('<h2>wordjuice:</h2></form></body>')

		aLen=len(self.request.get("a"))
		bLen=len(self.request.get("b"))
		a=self.request.get("a")
		b=self.request.get("b") 
		if aLen > bLen:
			for i in xrange(bLen):
				self.response.write('%s%s' % (a[i], b[i]))
			for i in xrange(bLen, aLen):
				self.response.write('%s' % (a[i]))
		elif aLen == bLen:
			for i in xrange(aLen):
				self.response.write('%s%s' % (a[i], b[i]))
		elif aLen < bLen:
			for i in xrange(aLen):
				self.response.write('%s%s' % (a[i], b[i]))
			for i in xrange(aLen, bLen):
				self.response.write('%s' % (b[i]))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
