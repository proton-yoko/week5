import webapp2
import urllib
import json

data = json.load(urllib.urlopen('http://fantasy-transit.appspot.com/net?format=json'))

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
		self.response.write('<form action="/transit" method = "post">出発駅<select name=stationfrom>山手線<option value=品川>品川</option><option value=大崎>大崎</option><option value=五反田>五反田</option><option value=目黒>目黒</option><option value=恵比寿>恵比寿</option><option value=渋谷>渋谷</option><option value=原宿>原宿</option><option value=代々木>代々木</option><option value=新宿>新宿</option><option value=新大久保>新大久保</option><option value=高田馬場>高田馬場</option><option value=目白>目白</option><option value=池袋>池袋</option><option value=大塚>大塚</option><option value=巣鴨>巣鴨</option><option value=駒越>駒越</option><option value=田端駅>田端駅</option><option value=西日暮里>西日暮里</option><option value=日暮里>日暮里</option><option value=鶯谷>鶯谷</option><option value=上野>上野</option><option value=御徒町>御徒町</option><option value=秋葉原>秋葉原</option><option value=神田>神田</option><option value=東京>東京</option><option value=有楽町>有楽町</option><option value=新橋>新橋</option><option value=浜松町>浜松町</option><option value=田町>田町</option>東横線<option value=反町>反町</option><option value=東白楽>東白楽</option><option value=白楽>白楽</option><option value=妙蓮寺>妙蓮寺</option><option value=菊名>菊名</option><option value=大倉山>大倉山</option><option value=綱島>綱島</option><option value=日吉>日吉</option><option value=元住吉>元住吉</option><option value=武蔵小杉>武蔵小杉</option><option value=新丸子>新丸子</option><option value=多摩川>多摩川</option><option value=田園調布>田園調布</option><option value=自由が丘>自由が丘</option><option value=都立大学>都立大学</option><option value=学芸大学>学芸大学</option><option value=祐天寺>祐天寺</option><option value=中目黒>中目黒</option><option value=代官山>代官山</option><option value=渋谷>渋谷</option>目黒線<option value=日吉>日吉</option><option value=元住吉>元住吉</option><option value=武蔵小杉>武蔵小杉</option><option value=新丸子>新丸子</option><option value=多摩川>多摩川</option><option value=田園調布>田園調布</option><option value=奥沢>奥沢</option><option value=大岡山>大岡山</option><option value=洗足>洗足</option><option value=西小山>西小山</option><option value=武蔵小山>武蔵小山</option><option value=不動前>不動前</option><option value=目黒>目黒</option></select><br>')
		self.response.write('到着駅<select name=stationfrom>山手線<option value=品川>品川</option><option value=大崎>大崎</option><option value=五反田>五反田</option><option value=目黒>目黒</option><option value=恵比寿>恵比寿</option><option value=渋谷>渋谷</option><option value=原宿>原宿</option><option value=代々木>代々木</option><option value=新宿>新宿</option><option value=新大久保>新大久保</option><option value=高田馬場>高田馬場</option><option value=目白>目白</option><option value=池袋>池袋</option><option value=大塚>大塚</option><option value=巣鴨>巣鴨</option><option value=駒越>駒越</option><option value=田端駅>田端駅</option><option value=西日暮里>西日暮里</option><option value=日暮里>日暮里</option><option value=鶯谷>鶯谷</option><option value=上野>上野</option><option value=御徒町>御徒町</option><option value=秋葉原>秋葉原</option><option value=神田>神田</option><option value=東京>東京</option><option value=有楽町>有楽町</option><option value=新橋>新橋</option><option value=浜松町>浜松町</option><option value=田町>田町</option>東横線<option value=反町>反町</option><option value=東白楽>東白楽</option><option value=白楽>白楽</option><option value=妙蓮寺>妙蓮寺</option><option value=菊名>菊名</option><option value=大倉山>大倉山</option><option value=綱島>綱島</option><option value=日吉>日吉</option><option value=元住吉>元住吉</option><option value=武蔵小杉>武蔵小杉</option><option value=新丸子>新丸子</option><option value=多摩川>多摩川</option><option value=田園調布>田園調布</option><option value=自由が丘>自由が丘</option><option value=都立大学>都立大学</option><option value=学芸大学>学芸大学</option><option value=祐天寺>祐天寺</option><option value=中目黒>中目黒</option><option value=代官山>代官山</option><option value=渋谷>渋谷</option>目黒線<option value=日吉>日吉</option><option value=元住吉>元住吉</option><option value=武蔵小杉>武蔵小杉</option><option value=新丸子>新丸子</option><option value=多摩川>多摩川</option><option value=田園調布>田園調布</option><option value=奥沢>奥沢</option><option value=大岡山>大岡山</option><option value=洗足>洗足</option><option value=西小山>西小山</option><option value=武蔵小山>武蔵小山</option><option value=不動前>不動前</option><option value=目黒>目黒</option></select><br><input type=submit value=検索></form>')

class Guide(webapp2.RequestHandler):
	def get(self):
		stationF = self.request.get('stationfrom')
		stationT = self.request.get('stationto')
		self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
		self.response.write('出発駅:%s'%stationF)
		self.response.write('到着駅:%s'%stationT)

		#同じ駅をふたつ選んだとき
		if stationF == stationT:
			self.response.write('もう到着してます！')
		#同じ路線上の二駅を選んだ時
		elif len(check_ifsame(stationF, stationT)) != 0:
			self.response.write('<FONT color="ff00ff">(乗り換えなし)<br>')
			self.response.write('乗り換えなしで可能な路線:%s' %check_ifsame(stationF, stationT))
			for line in check_ifsame(stationF, stationT):
				indexF = self.get_index(stationF, self.get_one_line(line)['Stations'])
				indexT = self.get_index(stationT, self.get_one_line(line)['Stations'])
				if indexF < indexT:
					for index in xrange(indexF, indexT):
						self.response.write('>> %s '% self.get_one_line(line)['Stations'][index])
				else:
					path = self.get_one_line(line['Stations'][indexT:indexF + 1]
					path.reverse()
					for station in path:
						self.response.write('>> %s' %station)
		#それ以外
		else:
			line_to_take = self.transfer_line(stationF, starionT)

			for line_index in xrange(1, len(line_to_take)):
				trans_station = (self.get_one_line(line_to_take[line_index - 1])['Stations'] & self.get_one_line(line_to_take[line_index])['Stations'])
			#まだ途中


	def get_index(self, station, line):
		#その路線内で何個目の要素かをさがす
		for index in xrange(len(line)):
			if line[index] == station:
				return index

	def get_lines(self, name):
		#駅名を渡すとその駅を通る路線を返してくれる
		for dictionary in data:
			for station in dictionary['Stations']
				if station == name:
					station_lines.add(dictionary['Name'])
		return station_lines
	
	def get_one_line(self, line):
		#その路線の説明の行をひとつ持ってくる
		for dictionary in data:
			if dictionary['Name'] == line:
				return dictionary

	def get check_ifsame(self, stationF, stationT):
		#同じ路線内に存在していないか確認、その路線をかえす	
		line_inF = self.get_lines(stationF)
		line_inT = self.get_lines(stationT)
		sameline_list = [str(item) for item in (line_inF & line_inT)]
		return sameline_list

	def check_line(self, current_lines, stationT):
		#今ある路線のどこかにstationTがあるかを判断してる
		for line in current_lines:
			if stationT in self.get_one_line(line)['Stations']:
				return True
		return False

	def adjunt_line(self, line):
		#今使える路線の駅を経由して乗り換えできる路線群を探す
		line_set = set()
		for station in self.get_one_line(line)['Stations']:
			for line in self.get_lines(station):
				line_set.add(line)
		return line_set

	def transfer_line(self, stationF, stationT):
		current_lines = self.get_lines(stationF)
		count_changes = 0
		line_path = []
		while not self.check_line(current_lines, stationT):
			line_path.append(current_lines)
			next_lines = set()
			for line in current_lines:
				next_lines |= self.adjunt_line(line)
			current_lines = next_lines
			count += 1
		stationT_line_set = self.get_lines(stationT)
		line_to_take = []
		stationT_line_to_take = ''
		for item in (stationT_line_set & current_lines):
			stationT_line_to_take = str(item)
		

		self.response.write('乗り換え%d回<br>' % count)
		self.response.write('推奨路線:<br>')
		for line in line_to_take:
			self.response.write('>> %s ' % line)
		return line_to_take
		#まだ途中

app = webapp2.WSGIApplication{
	[('/', MainPage),('/guide',Guide),],
	debug=True)
