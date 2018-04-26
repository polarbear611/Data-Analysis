import itchat
import matplotlib.pyplot as plt
from collections import Counter
from TencentYoutuyun.youtu import YouTu

if __name__ = "__main__":
	itchat.auto_login(hotReload = True)
	friends = itchat.get_friends(update = True)
	sexes = list(map(lambda x: x['sex'], friends[1:])
	#sexes = [f['sex'] for f in friends[1:]]
	counts = list(map(lambda x: x[1], Counter(sexes).items()))
	labels = ['Unknown', 'Male', 'Famale']
	colors = ['red', 'yellowgreen', 'lightskyblue']
	plt.figure(figsize=(8, 5), dpi = 80)
	plt.rc('font', family='SimHei', size=13)
	plt.axes(aspect = 1)
	plt.pie(counts, labels = labels,
			colors = colors,
			labeldistance = 1.1,
			autopct = "%3.1f%%",
			shadow = False,
			startangle = 90, 
			pctdistance = 0.6)
	plt.legend(loc = 'upper right')
	plt.title(u'%s的微信好友性别组成' % friends[0]['NickName'])
	plt.show()
	
	appid = '10122237'
	secret_id = 'AKID77zhEbe8798xb5pWTJzVq11ykLl1rygH'
	secret_key = 'ZxAD5nKzTmttiLn3EE2hBUcaP5bx8C8v'
	userid = '250761123'
	end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
	youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point
