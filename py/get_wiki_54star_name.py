# -*- coding: utf-8 -*
import urllib
import urllib.request
from bs4 import BeautifulSoup

# 抓4星为2，抓5星为1
GET_STAR_TYPE = 1

# 通过6星角色名获取其他星级角色名
name_list = ['钢铁骑士圣女贞德','将军须佐能乎','绝对魔王薇薇安','蒙泰终极型','二天一流香织','狩魔猎人亚伯','族长乌兹门特','捕盗大将卞剑秀','异能者伊莎贝尔','民族英雄郑成功','约定之维多利亚','黑骑士莱昂内尔','森林魔女娅莉塔','暴走僵尸希恩','鬼王钟馗','冥帝博格斯','火之魔女莎莎','引领者伊西丝','屠杀者哈尔菲亚','雷神托尔','皇帝亚历山大','战神阿基里斯','白胡子德雷克','黑暗骑士贝恩','圣魔该隐','粉碎者斯黛拉','大莫离支文德','V-暴走型','意志坚定的赫克托尔','战场上的圣女雅典娜','龙骑士齐格弗里德','末世杜尔拉汗','扭蛋鲁格斯','冰锤沃尔夫冈','节制的芬里尔','料理武术家雷玲','铁女修尔拉','驯龙高手·坤','疾风半藏','密使罗宾汉','R-0','月圆奇波郎','百发百中小光','寒霜恶灵妮芬','倾国倾城春香','浪漫的麦格尼斯','月光追击者阿塔兰特','黑曼巴','首席舞蹈家李','鹰之女儿拉喜玛','幽灵公主贝欧琳','月姬辉夜姬','荣誉者凯伦','收割者塞特','五虎大将军韩胜','牛仔梅西','司令斯派洛','最强佣兵斯内克','恶灵乌鸦','审判者文森特','噬魂射手No.9','哨兵R','超杀女明蒂','黑暗驱逐者威廉','赤色弹丸孙市','武装女仆迪雅','名侦探夏洛克','电子人斯佩妮','探究者罗蕾莱','妮欧','梅尔','蕾拉','海军上将斯嘉丽','冰霜猎人雷芬','百万富翁桃太郎','双面人鲁伊希尔拉','美食家阿索斯','觉醒的雅甘','阎罗使者桂香','冰封王座萨斯夸奇','月光女神莉莉丝','夜之女王瑞秋','黑桃王后爱丽丝','自然的纳兹伦','状元李梦龙','死灵法师内克伦','丰饶女神德米特尔','异端审判官乌列','稀世怪盗路尼昂','创造者宾森恩','苏醒的贝斯派','魔法傀儡师贝萝特','月亮花伊吹','森罗万象海獭','风之魔女乌尔弗兰姆','引导者奥西里斯','猫咪大师喵','光之南丁格尔','九尾狐阿狸','ICU特工护士','万能的乌帕','神女卑弥呼','疯狂科学家斯坦因','美食猎人彩依','追求幸福的达拉','无限的贝阿朵莉切','诱惑之奥菲欧','星光之娅莉娅','涅斯军长官尤莉娅','虚无的福斯特','使者赛莲','圣都之守护者诺埃尔','白花瓦莉','阴阳师晴明','先知墨菲斯']
for name in name_list:
     response = urllib.request.urlopen('http://wiki.joyme.com/cq/'+urllib.parse.quote(name))
     html = response.read()
     res = BeautifulSoup(html,"html.parser")
     if GET_STAR_TYPE==1:
          s=0
          for tag1 in res.find_all('div', class_='hero-info-block hero-info-block-frame hero-promote'):
               for tag2 in tag1.find_all('div', class_='promote'):
                    for tag3 in tag2.find_all('div', class_='name'):
                         try:
                              r_name = tag3.find('a').get_text()
                              s=s+1
                         except:
                              r_name = None
                         
                         if r_name!=None:
                              if s==1:
                                   with open("result_name.txt","a") as file:
                                        file.write(r_name+'\n')
                                   print(r_name + "success")
                              else:
                                   s=0
                                   continue
     elif GET_STAR_TYPE==2:
          s=0
          for tag1 in res.find_all('div', class_='hero-info-block hero-info-block-frame hero-promote'):
               for tag2 in tag1.find_all('div', class_='promote'):
                    for tag3 in tag2.find_all('div', class_='name'):
                         try:
                              r_name = tag3.find('a').get_text()
                         except:
                              r_name = None
                         
                         if r_name!=None:
                              if s==1:
                                   with open("result_name.txt","a") as file:
                                        file.write(r_name+'\n')
                                   print(r_name + "success")
                              else:
                                   s=s+1