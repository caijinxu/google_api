#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'caijinxu'

from qqwry import QQwry
q = QQwry()
q.load_file('app/libs/qqwry.dat')
# q.load_file('qqwry.dat')


lang_cou = """af	南非语
af-ZA	南非语
ar	阿拉伯语
ar-AE	阿拉伯语(阿联酋)
ar-BH	阿拉伯语(巴林)
ar-DZ	阿拉伯语(阿尔及利亚)
ar-EG	阿拉伯语(埃及)
ar-IQ	阿拉伯语(伊拉克)
ar-JO	阿拉伯语(约旦)
ar-KW	阿拉伯语(科威特)
ar-LB	阿拉伯语(黎巴嫩)
ar-LY	阿拉伯语(利比亚)
ar-MA	阿拉伯语(摩洛哥)
ar-OM	阿拉伯语(阿曼)
ar-QA	阿拉伯语(卡塔尔)
ar-SA	阿拉伯语(沙特阿拉伯)
ar-SY	阿拉伯语(叙利亚)
ar-TN	阿拉伯语(突尼斯)
ar-YE	阿拉伯语(也门)
az	阿塞拜疆语
az-AZ	阿塞拜疆语(拉丁文)
az-AZ	阿塞拜疆语(西里尔文)
be	比利时语
be-BY	比利时语
bg	保加利亚语
bg-BG	保加利亚语
bs-BA	波斯尼亚语(拉丁文，波斯尼亚和黑塞哥维那)
ca	加泰隆语
ca  安道尔
ca-ES	加泰隆语
cs	捷克语
cs-CZ	捷克语
cy	威尔士语
cy-GB	威尔士语
da	丹麦语
da-DK	丹麦语
de	德语
de-AT	德语(奥地利)
de-CH	德语(瑞士)
de-DE	德语(德国)
de-LI	德语(列支敦士登)
de-LU	德语(卢森堡)
dv	第维埃语
dv-MV	第维埃语
el	希腊语
el-GR	希腊语
en	英语
en-AU	英语(澳大利亚)
en-BZ	英语(伯利兹)
en-CA	英语(加拿大)
en-CB	英语(加勒比海)
en-GB	英语(英国)
en-IE	英语(爱尔兰)
en-JM	英语(牙买加)
en-NZ	英语(新西兰)
en-PH	英语(菲律宾)
en-TT	英语(特立尼达)
en-US	英语(美国)
en-ZA	英语(南非)
en-ZW	英语(津巴布韦)
en 北美地区
en 斐济
en 尼日利亚
en 乌干达
en 博茨瓦纳
en 肯尼亚
en 格林纳达
en 加纳
en 莱索托
en 赞比亚
en 纳米比亚
en 毛里求斯
en 多米尼克
en 关岛
en 马尔代夫
en 特立尼达和多巴哥
en 欧洲
en 不丹
eo	世界语
es	西班牙语
es-AR	西班牙语(阿根廷)
es-BO	西班牙语(玻利维亚)
es-CL	西班牙语(智利)
es-CO	西班牙语(哥伦比亚)
es-CR	西班牙语(哥斯达黎加)
es-DO	西班牙语(多米尼加共和国)
es-EC	西班牙语(厄瓜多尔)
es-ES	西班牙语(传统)
es-ES	西班牙语(国际)
es-GT	西班牙语(危地马拉)
es-HN	西班牙语(洪都拉斯)
es-MX	西班牙语(墨西哥)
es-NI	西班牙语(尼加拉瓜)
es-PA	西班牙语(巴拿马)
es-PE	西班牙语(秘鲁)
es-PR	西班牙语(波多黎各(美))
es-PY	西班牙语(巴拉圭)
es-SV	西班牙语(萨尔瓦多)
es-UY	西班牙语(乌拉圭)
es-VE	西班牙语(委内瑞拉)
es 直布罗陀
et	爱沙尼亚语
et-EE	爱沙尼亚语
eu	巴士克语
eu-ES	巴士克语
fa	法斯语
fa-IR	法斯语
fi	芬兰语
fi-FI	芬兰语
fo	法罗语
fo-FO	法罗语
fr	法语
fr-BE	法语(比利时)
fr-CA	法语(加拿大)
fr-CH	法语(瑞士)
fr-FR	法语(法国)
fr-LU	法语(卢森堡)
fr-MC	法语(摩纳哥)
fr 马达加斯加
fr 刚果(金)
fr 科特迪瓦
fr 吉布提
fr 法属波利尼西亚
fr 卢旺达
fr 喀麦隆
fr 塞内加尔
fr 留尼汪岛
fr 贝宁
fr 海地
fr 新喀里多尼亚
fr 瓜德罗普
gl	加里西亚语
gl-ES	加里西亚语
gu	古吉拉特语
gu-IN	古吉拉特语
he	希伯来语
he-IL	希伯来语
he  以色列
hi	印地语
hi-IN	印地语
hr	克罗地亚语
hr-BA	克罗地亚语(波斯尼亚和黑塞哥维那)
hr-HR	克罗地亚语
hu	匈牙利语
hu-HU	匈牙利语
hy	亚美尼亚语
hy-AM	亚美尼亚语
en 印度
id	印度尼西亚语
id-ID	印度尼西亚语
is	冰岛语
is-IS	冰岛语
it	意大利语
it-CH	意大利语(瑞士)
it-IT	意大利语(意大利)
ja	日语
ja-JP	日语日本
ka	格鲁吉亚语
ka-GE	格鲁吉亚语
kk	哈萨克语
kk 哈萨克斯坦
kk-KZ	哈萨克语
kn	卡纳拉语
kn-IN	卡纳拉语
ko	朝鲜语
ko 韩国
ko-KR	朝鲜语
kok	孔卡尼语
kok-IN	孔卡尼语
ky	吉尔吉斯语
ky 吉尔吉斯斯坦
ky-KG	吉尔吉斯语(西里尔文)
lt	立陶宛语
lt-LT	立陶宛语
lv	拉脱维亚语
lv-LV	拉脱维亚语
mi	毛利语
mi-NZ	毛利语
mk	马其顿语
mk-MK	马其顿语(FYROM)
mn	蒙古语
mn-MN	蒙古语(西里尔文)
mr	马拉地语
mr-IN	马拉地语
ms	马来语
ms-BN	马来语(文莱达鲁萨兰)
ms-MY	马来语(马来西亚)
mt	马耳他语
mt-MT	马耳他语
nb	挪威语(伯克梅尔)
nb-NO	挪威语(伯克梅尔)(挪威)
nl	荷兰语
nl-BE	荷兰语(比利时)
nl-NL	荷兰语(荷兰)
nl 阿鲁巴
nl 库拉索
nn-NO	挪威语(尼诺斯克)(挪威)
ns	北梭托语
ns-ZA	北梭托语
pa	旁遮普语
pa-IN	旁遮普语
pl	波兰语
pl-PL	波兰语
pt	葡萄牙语
pt-BR	葡萄牙语(巴西)
pt-PT	葡萄牙语(葡萄牙)
pt 安哥拉
pt 莫桑比克
qu	克丘亚语
qu-BO	克丘亚语(玻利维亚)
qu-EC	克丘亚语(厄瓜多尔)
qu-PE	克丘亚语(秘鲁)
ro	罗马尼亚语
ro-RO	罗马尼亚语
ru	俄语
ru-RU	俄语俄罗斯
sa	梵文
sa-IN	梵文
se	北萨摩斯语
se-FI	北萨摩斯语(芬兰)
se-FI	斯科特萨摩斯语(芬兰)
se-FI	伊那里萨摩斯语(芬兰)
se-NO	北萨摩斯语(挪威)
se-NO	律勒欧萨摩斯语(挪威)
se-NO	南萨摩斯语(挪威)
se-SE	北萨摩斯语(瑞典)
se-SE	律勒欧萨摩斯语(瑞典)
se-SE	南萨摩斯语(瑞典)
sk	斯洛伐克语
sk-SK	斯洛伐克语
sl	斯洛文尼亚语
sl-SI	斯洛文尼亚语
sq	阿尔巴尼亚语
sq-AL	阿尔巴尼亚语
sr-BA	塞尔维亚语(拉丁文，波斯尼亚和黑塞哥维那)
sr-BA	塞尔维亚语(西里尔文，波斯尼亚和黑塞哥维那)
sr-SP	塞尔维亚(拉丁)
sr-SP	塞尔维亚(西里尔文)
sv	瑞典语
ur 巴基斯坦
sv-FI	瑞典语(芬兰)
sv-SE	瑞典语
sw	斯瓦希里语
sw 坦桑尼亚
sw-KE	斯瓦希里语
syr	叙利亚语
syr-SY	叙利亚语
so 索马里
ta	泰米尔语
ta	泰米尔语斯里兰卡
ta-IN	泰米尔语
te	泰卢固语
te-IN	泰卢固语
th	泰语
th-TH	泰语泰国
tl	塔加路语
tl-PH	塔加路语(菲律宾)
tn	茨瓦纳语
tn-ZA	茨瓦纳语
tr	土耳其语
tr-TR	土耳其语
ts	宗加语
tt	鞑靼语
tt-RU	鞑靼语
uk	乌克兰语
uk-UA	乌克兰语
ur	乌都语
ur-PK	乌都语
uz	乌兹别克语
uz-UZ	乌兹别克语(拉丁文)
uz-UZ	乌兹别克语(西里尔文)
vi	越南语
vi-VN	越南语
xh	班图语
xh-ZA	班图语
zh	中文
zh-CN	中文(简体)
zh-HK	中文(香港)
zh-MO	中文(澳门)
zh-SG	中文(新加坡)
zh-TW	中文(繁体)
zu	祖鲁语
zu-ZA	祖鲁语
am 阿姆哈拉语
am 埃塞俄比亚
ga 爱尔兰语
bs 波斯尼亚语
lo 老挝语
lb 卢森堡语
bn  孟加拉语
my 缅甸语
ne 尼泊尔语
no 挪威语
sr 塞尔维亚语
km 柬埔寨
"""


def find_langcode(country):
    res = ''
    for langinfo in lang_cou.split('\n'):
        langinfo = langinfo.split()
        if langinfo and country in langinfo[1]:
            # print(langinfo)
            res = langinfo[0]
            if '-' in res:
                res = res.split('-')[0]
            break
    if not res:
        res = 'zh'
    return res


def ip_to_lancode(ip):
    result = q.lookup(ip)
    country = result[0]
    langcode = find_langcode(country)

    if langcode == 'zh':
        print(ip, country, langcode)

    return langcode

if __name__ == '__main__':
    ipl = """1.9.22.0/24
1.9.24.0/24
1.9.57.0/24
1.9.131.0/24
1.255.22.0/24
1.255.33.0/24
2.127.237.0/24
2.127.251.0/24
2.127.252.0/24
4.31.38.0/24
4.31.115.0/24
4.34.16.0/24
4.35.2.0/24
4.35.21.0/24
4.35.108.0/24
4.35.153.0/24
4.53.36.0/24
4.53.56.0/24
4.53.79.0/24
4.53.166.0/24
4.53.202.0/24
4.59.40.0/24
4.59.67.0/24
4.59.90.0/24
5.20.5.0/24
5.22.190.0/24
5.44.5.0/24
5.102.167.0/24
5.102.252.0/24
5.157.98.0/24
5.226.127.0/24
8.35.80.0/24
23.228.129.0/24
23.228.130.0/24
23.236.5.0/24
24.35.3.0/24
24.41.214.0/24
24.48.248.0/24
24.53.238.0/24
24.100.187.0/24
24.116.134.0/24
24.139.135.0/24
24.149.5.0/24
24.155.92.0/24
24.156.131.0/24
24.156.153.0/24
24.214.95.0/24
24.220.112.0/24
24.225.16.0/24
24.226.15.0/24
24.226.16.0/24
24.244.4.0/24
24.244.19.0/24
27.80.250.0/24
27.90.140.0/24
27.90.141.0/24
27.90.142.0/24
27.90.143.0/24
27.90.189.0/24
27.100.64.0/24
27.106.94.0/24
27.121.46.0/24
27.121.51.0/24
27.121.54.0/24
27.123.17.0/24
27.123.130.0/24
27.131.16.0/24
31.24.56.0/24
31.31.48.0/24
31.46.22.0/24
31.55.162.0/24
31.55.163.0/24
31.55.166.0/24
31.55.167.0/24
31.55.184.0/24
31.172.32.0/24
31.209.137.0/24
31.210.208.0/24
31.211.248.0/24
36.37.218.0/24
36.75.20.0/24
37.8.144.0/24
37.29.1.0/24
37.58.167.0/24
37.139.254.0/24
40.133.6.0/24
40.136.3.0/24
41.71.136.0/24
41.74.24.0/24
41.77.223.0/24
41.84.195.0/24
41.87.140.0/24
41.128.200.0/24
41.160.35.0/24
41.184.60.0/24
41.187.111.0/24
41.189.63.0/24
41.189.230.0/24
41.191.219.0/24
41.201.128.0/24
41.201.129.0/24
41.201.164.0/24
41.205.32.0/24
41.206.47.0/24
41.206.64.0/24
41.206.96.0/24
41.214.4.0/24
41.219.127.0/24
41.220.75.0/24
41.221.166.0/24
41.221.196.0/24
41.223.219.0/24
42.0.4.0/24
42.112.8.0/24
42.112.9.0/24
42.112.10.0/24
42.119.211.0/24
43.230.130.0/24
43.240.231.0/24
43.245.144.0/24
43.245.193.0/24
43.245.195.0/24
43.245.201.0/24
43.245.232.0/24
43.255.113.0/24
45.64.20.0/24
45.64.29.0/24
45.64.30.0/24
45.64.31.0/24
45.64.34.0/24
45.64.76.0/24
45.64.138.0/24
45.64.253.0/24
45.112.179.0/24
45.116.219.0/24
45.120.84.0/24
45.120.85.0/24
45.121.219.0/24
46.16.9.0/24
46.21.52.0/24
46.29.169.0/24
46.61.155.0/24
46.108.1.0/24
46.134.193.0/24
46.134.208.0/24
46.149.88.0/24
46.227.113.0/24
46.229.224.0/24
46.236.127.0/24
46.238.143.0/24
46.249.95.0/24
46.249.239.0/24
49.98.24.0/24
49.98.25.0/24
49.98.35.0/24
49.106.234.0/24
49.231.56.0/24
49.231.58.0/24
49.231.60.0/24
49.243.141.0/24
50.0.2.0/24
50.22.229.0/24
50.27.150.0/24
50.86.10.0/24
58.26.8.0/24
58.27.27.0/24
58.27.61.0/24
58.27.108.0/24
58.27.109.0/24
58.28.64.0/24
58.69.77.0/24
58.71.25.0/24
58.97.143.0/24
58.123.102.0/24
58.123.220.0/24
58.162.62.0/24
58.176.217.0/24
58.229.92.0/24
59.18.34.0/24
59.18.35.0/24
59.18.44.0/24
59.18.45.0/24
59.18.46.0/24
59.18.49.0/24
59.190.145.0/24
60.199.175.0/24
61.4.66.0/24
61.4.67.0/24
61.5.222.0/24
61.7.18.0/24
61.19.1.0/24
61.19.2.0/24
61.33.130.0/24
61.37.150.0/24
61.47.115.0/24
61.86.203.0/24
61.91.8.0/24
61.91.9.0/24
61.91.16.0/24
61.91.17.0/24
61.91.18.0/24
61.91.19.0/24
61.91.160.0/24
61.91.161.0/24
61.114.99.0/24
61.122.213.0/24
61.205.127.0/24
61.219.131.0/24
61.238.203.0/24
61.238.239.0/24
62.1.38.0/24
62.4.253.0/24
62.8.95.0/24
62.24.158.0/24
62.75.10.0/24
62.75.23.0/24
62.78.98.0/24
62.84.6.0/24
62.94.9.0/24
62.101.158.0/24
62.117.4.0/24
62.133.128.0/24
62.149.79.0/24
62.164.169.0/24
62.168.125.0/24
62.197.198.0/24
62.201.216.0/24
62.209.24.0/24
62.212.252.0/24
62.214.62.0/24
62.231.75.0/24
62.231.91.0/24
62.243.26.0/24
62.252.60.0/24
62.252.169.0/24
62.252.170.0/24
62.252.173.0/24
62.252.191.0/24
62.252.232.0/24
62.253.3.0/24
62.253.72.0/24
63.84.3.0/24
63.88.73.0/24
63.117.14.0/24
63.117.68.0/24
63.117.215.0/24
63.135.48.0/24
63.143.72.0/24
64.9.228.0/24
64.9.240.0/24
64.9.241.0/24
64.9.242.0/24
64.9.243.0/24
64.15.112.0/24
64.15.113.0/24
64.15.114.0/24
64.15.115.0/24
64.15.117.0/24
64.15.118.0/24
64.15.119.0/24
64.15.124.0/24
64.20.30.0/24
64.53.1.0/24
64.53.242.0/24
64.53.251.0/24
64.71.249.0/24
64.76.226.0/24
64.203.194.0/24
64.233.160.0/24
64.233.161.0/24
64.233.162.0/24
64.233.163.0/24
64.233.164.0/24
64.233.165.0/24
64.233.166.0/24
64.233.167.0/24
64.233.168.0/24
64.233.169.0/24
64.233.171.0/24
64.233.176.0/24
64.233.177.0/24
64.233.178.0/24
64.233.179.0/24
64.233.180.0/24
64.233.181.0/24
64.233.182.0/24
64.233.183.0/24
64.233.184.0/24
64.233.185.0/24
64.233.186.0/24
64.233.187.0/24
64.233.188.0/24
64.233.189.0/24
64.233.190.0/24
64.233.191.0/24
64.246.133.0/24
65.39.199.0/24
65.60.171.0/24
65.87.229.0/24
65.183.12.0/24
65.199.32.0/24
65.199.248.0/24
66.38.63.0/24
66.44.205.0/24
66.58.255.0/24
66.76.34.0/24
66.76.194.0/24
66.76.246.0/24
66.96.224.0/24
66.96.226.0/24
66.97.30.0/24
66.102.1.0/24
66.102.12.0/24
66.112.178.0/24
66.153.250.0/24
66.185.84.0/24
66.185.85.0/24
66.185.95.0/24
66.187.114.0/24
66.199.151.0/24
67.50.19.0/24
67.89.227.0/24
67.204.184.0/24
67.212.255.0/24
67.218.93.0/24
67.221.221.0/24
67.224.250.0/24
69.46.66.0/24
69.65.64.0/24
69.79.200.0/24
69.85.196.0/24
69.160.212.0/24
69.176.0.0/24
70.34.140.0/24
70.186.10.0/24
70.186.24.0/24
70.186.26.0/24
70.186.28.0/24
70.186.30.0/24
71.19.173.0/24
71.19.176.0/24
72.22.27.0/24
72.195.166.0/24
72.234.39.0/24
74.51.119.0/24
74.124.63.0/24
74.125.0.0/24
74.125.1.0/24
74.125.2.0/24
74.125.3.0/24
74.125.4.0/24
74.125.5.0/24
74.125.6.0/24
74.125.7.0/24
74.125.8.0/24
74.125.9.0/24
74.125.11.0/24
74.125.12.0/24
74.125.13.0/24
74.125.20.0/24
74.125.21.0/24
74.125.22.0/24
74.125.23.0/24
74.125.24.0/24
74.125.25.0/24
74.125.26.0/24
74.125.28.0/24
74.125.29.0/24
74.125.30.0/24
74.125.31.0/24
74.125.68.0/24
74.125.69.0/24
74.125.70.0/24
74.125.71.0/24
74.125.96.0/24
74.125.97.0/24
74.125.98.0/24
74.125.99.0/24
74.125.100.0/24
74.125.101.0/24
74.125.102.0/24
74.125.103.0/24
74.125.104.0/24
74.125.105.0/24
74.125.106.0/24
74.125.107.0/24
74.125.108.0/24
74.125.110.0/24
74.125.111.0/24
74.125.126.0/24
74.125.127.0/24
74.125.128.0/24
74.125.129.0/24
74.125.130.0/24
74.125.133.0/24
74.125.134.0/24
74.125.135.0/24
74.125.136.0/24
74.125.139.0/24
74.125.140.0/24
74.125.141.0/24
74.125.142.0/24
74.125.143.0/24
74.125.152.0/24
74.125.153.0/24
74.125.154.0/24
74.125.156.0/24
74.125.158.0/24
74.125.159.0/24
74.125.160.0/24
74.125.161.0/24
74.125.162.0/24
74.125.163.0/24
74.125.164.0/24
74.125.165.0/24
74.125.166.0/24
74.125.167.0/24
74.125.168.0/24
74.125.169.0/24
74.125.170.0/24
74.125.171.0/24
74.125.172.0/24
74.125.173.0/24
74.125.174.0/24
74.125.175.0/24
74.125.192.0/24
74.125.193.0/24
74.125.195.0/24
74.125.196.0/24
74.125.198.0/24
74.125.199.0/24
74.125.200.0/24
74.125.201.0/24
74.125.202.0/24
74.125.203.0/24
74.125.204.0/24
74.125.205.0/24
74.125.206.0/24
74.125.230.0/24
74.125.232.0/24
74.125.238.0/24
74.205.129.0/24
74.216.233.0/24
75.76.44.0/24
76.75.38.0/24
76.165.14.0/24
77.37.250.0/24
77.37.252.0/24
77.42.249.0/24
77.42.253.0/24
77.66.9.0/24
77.67.49.0/24
77.68.246.0/24
77.68.251.0/24
77.77.7.0/24
77.88.221.0/24
77.91.67.0/24
77.111.2.0/24
77.153.128.0/24
77.214.53.0/24
77.234.90.0/24
77.234.91.0/24
77.237.27.0/24
77.239.64.0/24
77.242.30.0/24
77.252.2.0/24
78.11.253.0/24
78.37.100.0/24
78.37.112.0/24
78.133.98.0/24
78.136.92.0/24
79.101.110.0/24
79.101.111.0/24
79.106.107.0/24
79.121.0.0/24
79.136.239.0/24
79.171.121.0/24
79.171.163.0/24
80.64.175.0/24
80.80.161.0/24
80.91.176.0/24
80.93.31.0/24
80.96.255.0/24
80.97.208.0/24
80.149.20.0/24
80.202.12.0/24
80.228.66.0/24
80.233.168.0/24
80.239.174.0/24
80.239.229.0/24
80.252.129.0/24
80.253.30.0/24
81.3.201.0/24
81.10.128.0/24
81.12.207.0/24
81.12.228.0/24
81.20.240.0/24
81.24.29.0/24
81.30.226.0/24
81.167.38.0/24
81.175.29.0/24
81.180.120.0/24
81.192.190.0/24
81.192.191.0/24
81.209.95.0/24
82.76.79.0/24
82.77.159.0/24
82.94.228.0/24
82.94.234.0/24
82.102.187.0/24
82.113.19.0/24
82.117.119.0/24
82.129.130.0/24
82.135.118.0/24
82.147.54.0/24
82.193.82.0/24
82.206.179.0/24
82.221.224.0/24
83.94.121.0/24
83.100.221.0/24
83.139.106.0/24
83.140.66.0/24
83.145.196.0/24
83.169.197.0/24
83.175.145.0/24
83.233.164.0/24
84.15.64.0/24
84.46.102.0/24
84.54.161.0/24
84.208.42.0/24
84.235.58.0/24
84.235.77.0/24
84.244.62.0/24
85.14.28.0/24
85.91.7.0/24
85.112.116.0/24
85.112.121.0/24
85.118.123.0/24
85.134.33.0/24
85.158.132.0/24
85.172.1.0/24
85.182.250.0/24
85.187.222.0/24
85.233.229.0/24
85.239.127.0/24
85.254.3.0/24
86.38.6.0/24
86.51.24.0/24
86.60.255.0/24
86.127.118.0/24
87.79.22.0/24
87.104.252.0/24
87.119.3.0/24
87.126.158.0/24
87.225.45.0/24
87.245.195.0/24
87.245.196.0/24
87.245.197.0/24
87.245.198.0/24
87.245.200.0/24
87.251.132.0/24
88.132.65.0/24
88.212.9.0/24
88.216.174.0/24
88.217.135.0/24
88.222.2.0/24
89.25.120.0/24
89.25.215.0/24
89.47.210.0/24
89.127.198.0/24
89.189.161.0/24
89.201.175.0/24
89.212.69.0/24
89.228.4.0/24
90.150.4.0/24
90.150.83.0/24
90.201.124.0/24
90.211.177.0/24
90.222.188.0/24
90.223.244.0/24
91.185.100.0/24
91.189.221.0/24
91.202.206.0/24
91.205.69.0/24
91.213.30.0/24
91.218.5.0/24
91.230.210.0/24
91.245.214.0/24
92.46.70.0/24
92.53.32.0/24
92.87.11.0/24
92.87.156.0/24
92.87.232.0/24
92.126.121.0/24
92.126.155.0/24
92.226.2.0/24
92.246.5.0/24
92.246.12.0/24
93.87.90.0/24
93.88.163.0/24
93.89.223.0/24
93.91.155.0/24
93.123.23.0/24
93.183.211.0/24
93.191.15.0/24
94.20.252.0/24
94.21.255.0/24
94.25.137.0/24
94.53.12.0/24
94.129.130.0/24
94.156.188.0/24
94.232.220.0/24
94.236.232.0/24
94.245.201.0/24
95.54.196.0/24
95.67.12.0/24
95.107.145.0/24
95.143.84.0/24
95.153.46.0/24
95.154.114.0/24
95.158.47.0/24
95.158.130.0/24
95.168.222.0/24
95.180.157.0/24
95.209.200.0/24
96.43.49.0/24
96.127.250.0/24
97.75.181.0/24
98.124.44.0/24
101.78.13.0/24
101.98.9.0/24
101.99.49.0/24
101.100.190.0/24
101.203.171.0/24
103.1.139.0/24
103.2.116.0/24
103.4.110.0/24
103.4.111.0/24
103.7.249.0/24
103.9.105.0/24
103.9.112.0/24
103.10.20.0/24
103.10.67.0/24
103.11.28.0/24
103.11.60.0/24
103.11.61.0/24
103.12.72.0/24
103.12.179.0/24
103.13.116.0/24
103.13.250.0/24
103.15.42.0/24
103.15.244.0/24
103.16.152.0/24
103.16.204.0/24
103.16.205.0/24
103.16.207.0/24
103.17.215.0/24
103.21.25.0/24
103.21.42.0/24
103.21.43.0/24
103.21.169.0/24
103.22.242.0/24
103.22.243.0/24
103.25.178.0/24
103.25.229.0/24
103.26.211.0/24
103.28.94.0/24
103.29.146.0/24
103.30.113.0/24
103.31.46.0/24
103.43.149.0/24
103.44.151.0/24
103.224.194.0/24
103.233.36.0/24
103.233.37.0/24
103.233.38.0/24
103.234.122.0/24
103.241.59.0/24
103.244.186.0/24
103.247.45.0/24
103.249.65.0/24
103.250.184.0/24
104.134.128.0/24
104.154.96.0/24
104.166.32.0/24
104.237.160.0/24
104.237.161.0/24
104.237.172.0/24
104.237.174.0/24
104.237.188.0/24
104.237.189.0/24
105.187.242.0/24
105.203.250.0/24
106.103.1.0/24
106.103.2.0/24
106.162.192.0/24
106.162.198.0/24
106.162.199.0/24
106.162.200.0/24
106.162.216.0/24
107.161.13.0/24
108.177.8.0/24
108.177.11.0/24
108.177.12.0/24
108.177.14.0/24
109.88.203.0/24
109.95.77.0/24
109.105.109.0/24
109.110.33.0/24
109.163.221.0/24
109.173.137.0/24
109.193.192.0/24
109.193.193.0/24
109.195.105.0/24
109.199.81.0/24
109.225.113.0/24
109.226.232.0/24
109.231.231.0/24
109.245.221.0/24
110.50.81.0/24
110.93.194.0/24
110.163.42.0/24
110.164.4.0/24
110.164.5.0/24
110.164.6.0/24
110.164.7.0/24
110.164.8.0/24
110.164.9.0/24
110.164.10.0/24
110.164.12.0/24
110.164.13.0/24
110.164.14.0/24
110.164.16.0/24
111.84.96.0/24
111.84.224.0/24
111.86.157.0/24
111.86.247.0/24
111.90.117.0/24
111.92.162.0/24
111.94.248.0/24
111.95.240.0/24
111.107.254.0/24
111.168.255.0/24
112.72.5.0/24
113.59.211.0/24
113.171.18.0/24
113.171.19.0/24
113.171.239.0/24
113.171.241.0/24
113.171.242.0/24
113.171.243.0/24
113.171.244.0/24
113.171.245.0/24
113.171.246.0/24
113.171.247.0/24
113.171.251.0/24
113.171.252.0/24
113.171.253.0/24
114.4.4.0/24
114.31.1.0/24
114.108.207.0/24
114.120.192.0/24
114.121.194.0/24
114.125.129.0/24
114.130.6.0/24
115.84.108.0/24
115.127.52.0/24
115.164.12.0/24
115.164.140.0/24
115.166.169.0/24
115.167.72.0/24
115.167.74.0/24
115.167.76.0/24
115.178.26.0/24
115.178.27.0/24
115.254.97.0/24
115.254.106.0/24
115.254.121.0/24
116.58.204.0/24
116.92.194.0/24
116.93.47.0/24
116.202.230.0/24
116.212.147.0/24
117.102.117.0/24
118.69.249.0/24
118.98.26.0/24
118.98.30.0/24
118.98.36.0/24
118.98.76.0/24
118.98.77.0/24
118.98.106.0/24
118.98.110.0/24
118.98.111.0/24
118.107.75.0/24
118.107.111.0/24
118.143.88.0/24
119.2.100.0/24
119.9.76.0/24
119.15.80.0/24
119.40.97.0/24
119.110.118.0/24
119.149.187.0/24
119.149.188.0/24
119.161.83.0/24
119.224.142.0/24
119.235.103.0/24
120.28.5.0/24
120.28.12.0/24
120.28.26.0/24
120.28.53.0/24
120.89.6.0/24
121.78.52.0/24
121.78.71.0/24
121.78.74.0/24
121.78.206.0/24
122.2.128.0/24
122.2.129.0/24
122.2.152.0/24
122.2.153.0/24
122.54.231.0/24
122.56.60.0/24
122.56.115.0/24
122.149.3.0/24
122.154.58.0/24
122.154.76.0/24
122.154.133.0/24
122.154.160.0/24
122.154.244.0/24
122.168.100.0/24
122.201.16.0/24
122.202.129.0/24
122.251.255.0/24
122.255.117.0/24
123.108.252.0/24
123.136.105.0/24
123.176.0.0/24
123.205.250.0/24
124.40.230.0/24
124.40.233.0/24
124.40.245.0/24
124.153.255.0/24
124.158.72.0/24
124.248.162.0/24
125.214.167.0/24
125.234.50.0/24
125.234.52.0/24
125.234.53.0/24
125.234.54.0/24
125.234.55.0/24
125.235.17.0/24
125.235.30.0/24
125.235.31.0/24
125.235.36.0/24
128.0.86.0/24
128.0.90.0/24
128.0.169.0/24
128.210.224.0/24
129.66.96.0/24
130.111.19.0/24
130.206.193.0/24
130.211.254.0/24
134.90.151.0/24
135.0.199.0/24
137.207.250.0/24
139.175.107.0/24
140.113.14.0/24
140.197.248.0/24
142.163.38.0/24
142.166.12.0/24
142.166.129.0/24
142.166.149.0/24
142.176.121.0/24
143.215.193.0/24
144.131.80.0/24
146.88.60.0/24
146.115.8.0/24
148.245.203.0/24
149.126.86.0/24
149.165.180.0/24
150.100.16.0/24
150.101.213.0/24
150.199.24.0/24
151.21.210.0/24
151.50.168.0/24
151.248.100.0/24
154.65.36.0/24
154.66.245.0/24
154.67.1.0/24
154.73.81.0/24
154.126.74.0/24
155.69.253.0/24
155.232.240.0/24
157.157.135.0/24
157.161.155.0/24
157.197.92.0/24
157.197.93.0/24
159.134.168.0/24
159.148.69.0/24
159.180.253.0/24
161.132.34.0/24
162.212.208.0/24
162.221.128.0/24
162.252.127.0/24
163.28.38.0/24
163.28.83.0/24
163.28.116.0/24
163.53.140.0/24
164.40.244.0/24
164.58.87.0/24
164.85.63.0/24
164.113.94.0/24
165.98.72.0/24
165.165.38.0/24
167.142.232.0/24
167.206.10.0/24
167.206.12.0/24
167.206.145.0/24
167.206.245.0/24
167.206.252.0/24
172.56.136.0/24
172.217.0.0/24
172.217.1.0/24
172.217.2.0/24
172.217.3.0/24
172.217.4.0/24
172.217.5.0/24
172.217.6.0/24
172.217.7.0/24
172.217.17.0/24
172.217.18.0/24
172.217.19.0/24
172.217.20.0/24
172.217.21.0/24
172.217.22.0/24
172.217.23.0/24
172.217.24.0/24
172.217.25.0/24
172.217.26.0/24
172.217.27.0/24
172.217.28.0/24
172.217.29.0/24
173.194.0.0/24
173.194.1.0/24
173.194.2.0/24
173.194.3.0/24
173.194.4.0/24
173.194.5.0/24
173.194.6.0/24
173.194.7.0/24
173.194.8.0/24
173.194.9.0/24
173.194.10.0/24
173.194.11.0/24
173.194.12.0/24
173.194.13.0/24
173.194.14.0/24
173.194.15.0/24
173.194.16.0/24
173.194.17.0/24
173.194.18.0/24
173.194.19.0/24
173.194.20.0/24
173.194.21.0/24
173.194.22.0/24
173.194.24.0/24
173.194.25.0/24
173.194.26.0/24
173.194.27.0/24
173.194.28.0/24
173.194.29.0/24
173.194.31.0/24
173.194.32.0/24
173.194.44.0/24
173.194.48.0/24
173.194.49.0/24
173.194.51.0/24
173.194.53.0/24
173.194.54.0/24
173.194.55.0/24
173.194.56.0/24
173.194.57.0/24
173.194.58.0/24
173.194.59.0/24
173.194.60.0/24
173.194.61.0/24
173.194.62.0/24
173.194.63.0/24
173.194.64.0/24
173.194.65.0/24
173.194.66.0/24
173.194.67.0/24
173.194.69.0/24
173.194.70.0/24
173.194.72.0/24
173.194.74.0/24
173.194.76.0/24
173.194.77.0/24
173.194.78.0/24
173.194.113.0/24
173.194.122.0/24
173.194.124.0/24
173.194.128.0/24
173.194.129.0/24
173.194.130.0/24
173.194.131.0/24
173.194.132.0/24
173.194.133.0/24
173.194.134.0/24
173.194.135.0/24
173.194.136.0/24
173.194.137.0/24
173.194.138.0/24
173.194.139.0/24
173.194.140.0/24
173.194.141.0/24
173.194.142.0/24
173.194.143.0/24
173.194.144.0/24
173.194.146.0/24
173.194.147.0/24
173.194.148.0/24
173.194.149.0/24
173.194.150.0/24
173.194.151.0/24
173.194.152.0/24
173.194.153.0/24
173.194.154.0/24
173.194.155.0/24
173.194.156.0/24
173.194.157.0/24
173.194.158.0/24
173.194.160.0/24
173.194.164.0/24
173.194.165.0/24
173.194.192.0/24
173.194.193.0/24
173.194.194.0/24
173.194.195.0/24
173.194.196.0/24
173.194.197.0/24
173.194.198.0/24
173.194.199.0/24
173.194.200.0/24
173.194.201.0/24
173.194.202.0/24
173.194.203.0/24
173.194.204.0/24
173.194.205.0/24
173.194.206.0/24
173.194.207.0/24
173.194.208.0/24
173.194.209.0/24
173.194.210.0/24
173.194.211.0/24
173.194.212.0/24
173.194.213.0/24
173.194.214.0/24
173.194.215.0/24
173.194.216.0/24
173.194.217.0/24
173.194.218.0/24
173.194.219.0/24
173.194.220.0/24
173.194.221.0/24
173.194.222.0/24
173.194.223.0/24
173.218.248.0/24
173.219.91.0/24
173.219.93.0/24
173.224.96.0/24
173.227.93.0/24
173.227.247.0/24
173.237.115.0/24
174.140.109.0/24
175.28.1.0/24
175.100.94.0/24
176.28.77.0/24
176.126.59.0/24
176.221.96.0/24
176.255.201.0/24
177.35.32.0/24
177.35.203.0/24
177.36.3.0/24
177.36.217.0/24
177.43.115.0/24
177.43.165.0/24
177.43.170.0/24
177.43.196.0/24
177.43.235.0/24
177.43.239.0/24
177.55.62.0/24
177.71.7.0/24
177.91.160.0/24
177.99.179.0/24
177.99.185.0/24
177.99.203.0/24
177.100.48.0/24
177.101.143.0/24
177.107.191.0/24
177.124.192.0/24
177.126.126.0/24
177.128.223.0/24
177.131.1.0/24
177.135.84.0/24
177.135.94.0/24
177.135.103.0/24
177.135.107.0/24
177.135.110.0/24
177.135.135.0/24
177.135.177.0/24
177.135.245.0/24
177.136.113.0/24
177.155.0.0/24
177.155.141.0/24
177.159.161.0/24
177.159.162.0/24
177.159.237.0/24
178.22.222.0/24
178.23.236.0/24
178.35.137.0/24
178.45.249.0/24
178.45.251.0/24
178.45.253.0/24
178.60.128.0/24
178.60.195.0/24
178.74.30.0/24
178.132.81.0/24
178.168.3.0/24
178.209.67.0/24
178.235.206.0/24
178.236.130.0/24
178.250.208.0/24
179.6.63.0/24
179.6.255.0/24
179.60.91.0/24
179.96.24.0/24
179.96.35.0/24
179.97.196.0/24
179.106.47.0/24
179.124.138.0/24
179.124.224.0/24
179.127.142.0/24
179.154.191.0/24
179.183.24.0/24
179.184.10.0/24
179.185.163.0/24
180.93.32.0/24
180.149.5.0/24
180.149.59.0/24
180.149.61.0/24
180.149.91.0/24
180.150.1.0/24
180.188.250.0/24
180.211.201.0/24
180.214.232.0/24
180.234.2.0/24
180.234.129.0/24
180.235.254.0/24
180.251.67.0/24
181.15.96.0/24
181.15.215.0/24
181.15.220.0/24
181.15.221.0/24
181.30.240.0/24
181.30.241.0/24
181.30.242.0/24
181.47.248.0/24
181.48.252.0/24
181.48.254.0/24
181.48.255.0/24
181.49.182.0/24
181.64.130.0/24
181.64.131.0/24
181.64.132.0/24
181.114.54.0/24
181.176.244.0/24
181.188.0.0/24
181.192.63.0/24
181.198.79.0/24
181.198.80.0/24
181.224.253.0/24
182.48.85.0/24
182.79.251.0/24
182.79.253.0/24
182.79.254.0/24
182.163.240.0/24
182.176.44.0/24
182.176.130.0/24
182.176.131.0/24
182.239.95.0/24
182.239.127.0/24
182.248.204.0/24
182.253.220.0/24
183.78.5.0/24
183.78.64.0/24
183.78.96.0/24
183.87.151.0/24
183.91.18.0/24
183.182.96.0/24
184.150.152.0/24
184.150.153.0/24
184.150.182.0/24
184.150.183.0/24
184.150.186.0/24
184.170.67.0/24
185.2.108.0/24
185.3.1.0/24
185.5.161.0/24
185.13.132.0/24
185.37.85.0/24
185.38.0.0/24
185.42.244.0/24
185.48.9.0/24
185.59.69.0/24
185.73.88.0/24
185.95.204.0/24
185.119.13.0/24
186.1.197.0/24
186.2.131.0/24
186.15.250.0/24
186.27.124.0/24
186.32.236.0/24
186.46.140.0/24
186.68.154.0/24
186.68.247.0/24
186.73.72.0/24
186.73.79.0/24
186.96.91.0/24
186.151.236.0/24
186.160.223.0/24
186.176.224.0/24
186.177.65.0/24
186.178.0.0/24
186.192.145.0/24
186.194.48.0/24
186.207.162.0/24
186.215.92.0/24
186.215.155.0/24
186.215.194.0/24
186.215.208.0/24
186.225.147.0/24
186.226.128.0/24
186.232.197.0/24
186.235.31.0/24
186.251.10.0/24
187.1.89.0/24
187.2.74.0/24
187.7.117.0/24
187.18.184.0/24
187.19.96.0/24
187.19.145.0/24
187.33.247.0/24
187.44.0.0/24
187.58.66.0/24
187.66.78.0/24
187.72.192.0/24
187.86.49.0/24
187.110.64.0/24
187.110.238.0/24
187.115.167.0/24
187.123.28.0/24
187.160.243.0/24
187.160.254.0/24
187.254.78.0/24
188.21.9.0/24
188.43.64.0/24
188.43.65.0/24
188.43.66.0/24
188.43.68.0/24
188.43.69.0/24
188.93.174.0/24
188.112.3.0/24
188.113.128.0/24
188.247.240.0/24
188.254.87.0/24
189.1.145.0/24
189.5.130.0/24
189.7.75.0/24
189.14.52.0/24
189.26.123.0/24
189.34.253.0/24
189.38.33.0/24
189.39.126.0/24
189.45.193.0/24
189.51.155.0/24
189.58.99.0/24
189.59.93.0/24
189.63.251.0/24
189.73.192.0/24
189.76.142.0/24
189.86.41.0/24
189.89.161.0/24
189.90.243.0/24
189.103.27.0/24
189.115.42.0/24
189.124.133.0/24
189.193.189.0/24
189.194.54.0/24
189.194.94.0/24
189.195.96.0/24
189.195.222.0/24
189.196.168.0/24
189.196.189.0/24
189.197.77.0/24
189.197.79.0/24
189.197.190.0/24
189.198.236.0/24
189.198.250.0/24
189.199.19.0/24
189.199.71.0/24
189.199.81.0/24
189.199.103.0/24
189.199.105.0/24
189.199.250.0/24
189.203.167.0/24
189.203.232.0/24
189.215.132.0/24
189.215.200.0/24
189.247.133.0/24
189.247.134.0/24
189.247.135.0/24
189.247.136.0/24
189.247.138.0/24
189.247.144.0/24
189.247.145.0/24
189.247.146.0/24
189.247.147.0/24
189.247.148.0/24
189.247.160.0/24
189.247.161.0/24
189.247.168.0/24
189.247.169.0/24
190.45.0.0/24
190.57.158.0/24
190.58.136.0/24
190.92.89.0/24
190.94.130.0/24
190.94.176.0/24
190.96.100.0/24
190.97.0.0/24
190.98.163.0/24
190.98.170.0/24
190.98.171.0/24
190.104.150.0/24
190.106.220.0/24
190.108.82.0/24
190.113.97.0/24
190.116.191.0/24
190.120.207.0/24
190.121.11.0/24
190.122.100.0/24
190.129.124.0/24
190.143.134.0/24
190.145.255.0/24
190.150.50.0/24
190.166.41.0/24
190.167.241.0/24
190.186.210.0/24
190.197.64.0/24
190.211.175.0/24
190.212.166.0/24
190.221.162.0/24
190.235.154.0/24
190.240.1.0/24
190.240.2.0/24
190.240.6.0/24
190.241.121.0/24
190.248.1.0/24
190.248.34.0/24
190.248.35.0/24
191.33.177.0/24
191.99.255.0/24
191.243.156.0/24
191.251.128.0/24
191.251.192.0/24
191.253.208.0/24
192.31.228.0/24
192.70.222.0/24
192.122.185.0/24
192.124.233.0/24
192.154.121.0/24
192.232.16.0/24
192.248.3.0/24
193.0.255.0/24
193.4.115.0/24
193.28.236.0/24
193.51.224.0/24
193.90.147.0/24
193.92.133.0/24
193.95.12.0/24
193.95.144.0/24
193.134.255.0/24
193.170.141.0/24
193.189.184.0/24
193.192.226.0/24
193.192.250.0/24
193.206.135.0/24
193.229.108.0/24
194.9.24.0/24
194.9.25.0/24
194.24.134.0/24
194.44.4.0/24
194.44.64.0/24
194.78.0.0/24
194.78.99.0/24
194.90.196.0/24
194.106.173.0/24
194.116.101.0/24
194.122.80.0/24
194.122.81.0/24
194.122.82.0/24
194.134.26.0/24
194.152.31.0/24
194.158.92.0/24
194.182.232.0/24
194.183.149.0/24
194.199.78.0/24
194.210.238.0/24
195.8.11.0/24
195.8.12.0/24
195.12.176.0/24
195.12.177.0/24
195.13.189.0/24
195.13.231.0/24
195.39.213.0/24
195.43.73.0/24
195.46.107.0/24
195.49.27.0/24
195.50.84.0/24
195.64.213.0/24
195.78.217.0/24
195.80.179.0/24
195.95.178.0/24
195.111.111.0/24
195.113.214.0/24
195.122.16.0/24
195.122.30.0/24
195.162.39.0/24
195.176.255.0/24
195.177.197.0/24
195.187.242.0/24
195.202.131.0/24
195.249.20.0/24
195.249.23.0/24
196.0.3.0/24
196.12.217.0/24
196.23.168.0/24
196.27.66.0/24
196.29.35.0/24
196.44.149.0/24
196.46.1.0/24
196.46.123.0/24
196.49.8.0/24
196.201.223.0/24
196.202.235.0/24
196.202.246.0/24
196.203.102.0/24
196.204.32.0/24
196.207.198.0/24
197.136.0.0/24
197.149.150.0/24
197.157.244.0/24
197.158.80.0/24
197.159.29.0/24
197.199.253.0/24
197.199.254.0/24
197.218.0.0/24
197.220.0.0/24
197.221.233.0/24
197.235.0.0/24
197.243.124.0/24
197.251.230.0/24
197.253.18.0/24
198.7.237.0/24
198.52.15.0/24
198.70.68.0/24
198.70.69.0/24
198.70.70.0/24
198.142.187.0/24
198.231.29.0/24
198.235.201.0/24
199.59.103.0/24
199.83.198.0/24
199.87.241.0/24
200.3.21.0/24
200.10.226.0/24
200.28.0.0/24
200.28.6.0/24
200.28.8.0/24
200.28.12.0/24
200.29.113.0/24
200.31.96.0/24
200.40.3.0/24
200.40.172.0/24
200.49.185.0/24
200.50.67.0/24
200.52.21.0/24
200.53.245.0/24
200.55.230.0/24
200.56.193.0/24
200.62.26.0/24
200.63.214.0/24
200.77.139.0/24
200.77.168.0/24
200.81.125.0/24
200.85.99.0/24
200.94.238.0/24
200.105.131.0/24
200.108.53.0/24
200.110.122.0/24
200.115.92.0/24
200.115.94.0/24
200.115.95.0/24
200.124.254.0/24
200.142.191.0/24
200.149.119.0/24
200.150.4.0/24
200.160.97.0/24
200.172.62.0/24
200.188.128.0/24
200.189.63.0/24
200.195.190.0/24
200.216.56.0/24
200.216.90.0/24
200.220.141.0/24
201.6.16.0/24
201.16.57.0/24
201.16.134.0/24
201.23.161.0/24
201.30.4.0/24
201.31.84.0/24
201.33.240.0/24
201.49.80.0/24
201.57.54.0/24
201.64.241.0/24
201.67.193.0/24
201.82.108.0/24
201.86.233.0/24
201.87.209.0/24
201.130.49.0/24
201.130.208.0/24
201.132.92.0/24
201.132.200.0/24
201.151.207.0/24
201.157.30.0/24
201.157.200.0/24
201.162.64.0/24
201.163.0.0/24
201.165.0.0/24
201.165.116.0/24
201.165.221.0/24
201.167.5.0/24
201.167.51.0/24
201.167.56.0/24
201.167.64.0/24
201.174.48.0/24
201.174.82.0/24
201.174.96.0/24
201.174.97.0/24
201.174.98.0/24
201.175.77.0/24
201.218.56.0/24
201.227.61.0/24
201.229.1.0/24
201.245.193.0/24
201.245.194.0/24
201.248.76.0/24
201.248.78.0/24
202.3.240.0/24
202.4.173.0/24
202.28.85.0/24
202.38.180.0/24
202.39.143.0/24
202.40.221.0/24
202.51.65.0/24
202.51.67.0/24
202.51.247.0/24
202.56.33.0/24
202.58.96.0/24
202.58.97.0/24
202.67.35.0/24
202.67.37.0/24
202.67.39.0/24
202.67.41.0/24
202.67.43.0/24
202.67.45.0/24
202.69.12.0/24
202.69.185.0/24
202.73.230.0/24
202.75.141.0/24
202.75.147.0/24
202.78.83.0/24
202.78.113.0/24
202.86.162.0/24
202.88.68.0/24
202.88.157.0/24
202.88.186.0/24
202.89.241.0/24
202.90.152.0/24
202.90.156.0/24
202.93.153.0/24
202.122.145.0/24
202.122.146.0/24
202.124.127.0/24
202.128.15.0/24
202.129.8.0/24
202.134.14.0/24
202.148.204.0/24
202.151.87.0/24
202.152.47.0/24
202.152.130.0/24
202.153.85.0/24
202.158.57.0/24
202.160.9.0/24
202.163.106.0/24
202.163.174.0/24
202.166.193.0/24
202.169.173.0/24
202.169.175.0/24
202.169.193.0/24
202.170.35.0/24
202.179.1.0/24
202.208.170.0/24
202.216.0.0/24
202.220.161.0/24
202.224.62.0/24
202.224.83.0/24
202.231.177.0/24
202.248.151.0/24
202.248.248.0/24
203.2.228.0/24
203.5.76.0/24
203.13.161.0/24
203.66.124.0/24
203.66.155.0/24
203.78.32.0/24
203.78.36.0/24
203.82.75.0/24
203.82.76.0/24
203.82.77.0/24
203.82.95.0/24
203.94.209.0/24
203.113.160.0/24
203.113.161.0/24
203.114.135.0/24
203.116.165.0/24
203.116.189.0/24
203.117.34.0/24
203.118.141.0/24
203.118.143.0/24
203.121.59.0/24
203.133.8.0/24
203.133.72.0/24
203.139.206.0/24
203.142.74.0/24
203.146.98.0/24
203.151.116.0/24
203.152.112.0/24
203.165.13.0/24
203.165.14.0/24
203.176.177.0/24
203.176.178.0/24
203.184.5.0/24
203.184.7.0/24
203.207.55.0/24
203.211.0.0/24
203.211.8.0/24
203.217.98.0/24
203.217.168.0/24
203.233.10.0/24
203.233.18.0/24
203.233.63.0/24
203.233.88.0/24
203.233.92.0/24
203.233.96.0/24
203.233.126.0/24
203.248.180.0/24
203.248.210.0/24
203.252.15.0/24
204.9.80.0/24
204.17.140.0/24
204.85.30.0/24
204.111.84.0/24
204.186.48.0/24
204.186.215.0/24
205.158.11.0/24
205.213.108.0/24
205.213.114.0/24
205.237.38.0/24
205.237.60.0/24
206.80.249.0/24
206.126.112.0/24
206.131.134.0/24
206.167.212.0/24
206.169.145.0/24
206.181.8.0/24
206.248.149.0/24
206.248.151.0/24
207.34.103.0/24
207.134.64.0/24
207.172.159.0/24
207.173.228.0/24
207.181.192.0/24
207.191.178.0/24
207.192.241.0/24
207.204.159.0/24
207.237.69.0/24
207.238.252.0/24
207.255.26.0/24
208.53.243.0/24
208.65.155.0/24
208.73.255.0/24
208.90.107.0/24
208.93.196.0/24
208.94.168.0/24
208.104.242.0/24
208.111.59.0/24
208.117.225.0/24
208.117.226.0/24
208.117.227.0/24
208.117.229.0/24
208.117.230.0/24
208.117.231.0/24
208.117.234.0/24
208.117.236.0/24
208.117.239.0/24
208.117.242.0/24
208.117.243.0/24
208.117.244.0/24
208.117.253.0/24
208.138.46.0/24
208.187.128.0/24
209.33.235.0/24
209.52.189.0/24
209.56.124.0/24
209.81.111.0/24
209.85.144.0/24
209.85.145.0/24
209.85.147.0/24
209.85.200.0/24
209.85.201.0/24
209.85.202.0/24
209.85.203.0/24
209.85.224.0/24
209.85.225.0/24
209.85.226.0/24
209.85.227.0/24
209.85.228.0/24
209.85.229.0/24
209.85.230.0/24
209.85.231.0/24
209.85.232.0/24
209.85.233.0/24
209.85.234.0/24
209.85.235.0/24
209.85.239.0/24
209.91.176.0/24
209.91.216.0/24
209.116.150.0/24
209.116.186.0/24
209.118.7.0/24
209.118.99.0/24
209.118.208.0/24
209.141.120.0/24
209.148.195.0/24
209.183.147.0/24
209.191.218.0/24
209.226.57.0/24
210.2.185.0/24
210.7.45.0/24
210.61.221.0/24
210.92.119.0/24
210.94.153.0/24
210.139.253.0/24
210.143.70.0/24
210.143.147.0/24
210.153.73.0/24
210.158.146.0/24
210.187.22.0/24
210.187.25.0/24
210.191.74.0/24
210.236.185.0/24
210.242.125.0/24
210.242.127.0/24
210.242.128.0/24
210.245.14.0/24
210.253.46.0/24
211.117.39.0/24
211.175.187.0/24
211.239.234.0/24
212.0.195.0/24
212.1.249.0/24
212.1.250.0/24
212.2.108.0/24
212.6.83.0/24
212.7.1.0/24
212.9.14.0/24
212.10.212.0/24
212.30.5.0/24
212.39.82.0/24
212.40.1.0/24
212.40.34.0/24
212.40.98.0/24
212.52.60.0/24
212.56.71.0/24
212.56.131.0/24
212.56.132.0/24
212.57.191.0/24
212.88.109.0/24
212.89.5.0/24
212.92.207.0/24
212.106.207.0/24
212.106.221.0/24
212.112.37.0/24
212.113.7.0/24
212.113.49.0/24
212.113.52.0/24
212.113.185.0/24
212.120.241.0/24
212.122.6.0/24
212.122.14.0/24
212.142.160.0/24
212.146.69.0/24
212.179.154.0/24
212.188.7.0/24
212.188.10.0/24
212.188.15.0/24
212.188.49.0/24
212.191.227.0/24
212.191.236.0/24
212.247.8.0/24
213.24.121.0/24
213.30.5.0/24
213.30.114.0/24
213.55.64.0/24
213.59.210.0/24
213.59.237.0/24
213.81.154.0/24
213.85.209.0/24
213.94.75.0/24
213.105.64.0/24
213.108.23.0/24
213.145.140.0/24
213.152.1.0/24
213.153.32.0/24
213.155.151.0/24
213.158.11.0/24
213.158.189.0/24
213.159.32.0/24
213.163.23.0/24
213.190.196.0/24
213.196.106.0/24
213.208.156.0/24
213.233.153.0/24
213.240.44.0/24
213.241.87.0/24
213.241.88.0/24
213.241.89.0/24
213.242.89.0/24
213.253.9.0/24
216.11.246.0/24
216.12.120.0/24
216.21.170.0/24
216.50.166.0/24
216.58.192.0/24
216.58.193.0/24
216.58.194.0/24
216.58.196.0/24
216.58.197.0/24
216.58.198.0/24
216.58.200.0/24
216.58.202.0/24
216.58.208.0/24
216.58.209.0/24
216.58.210.0/24
216.58.211.0/24
216.58.212.0/24
216.58.213.0/24
216.58.216.0/24
216.58.217.0/24
216.58.218.0/24
216.58.219.0/24
216.58.220.0/24
216.58.221.0/24
216.58.222.0/24
216.58.223.0/24
216.59.116.0/24
216.68.10.0/24
216.68.248.0/24
216.93.235.0/24
216.123.194.0/24
216.126.108.0/24
216.147.171.0/24
216.152.163.0/24
216.177.189.0/24
216.197.242.0/24
216.211.1.0/24
216.221.127.0/24
216.229.87.0/24
216.239.32.0/24
216.239.34.0/24
216.239.36.0/24
216.239.38.0/24
216.239.90.0/24
216.254.140.0/24
217.15.105.0/24
217.16.73.0/24
217.18.145.0/24
217.18.243.0/24
217.19.150.0/24
217.73.128.0/24
217.73.160.0/24
217.75.205.0/24
217.115.45.0/24
217.116.143.0/24
217.119.118.0/24
217.147.40.0/24
217.174.48.0/24
218.189.25.0/24
218.208.3.0/24
218.219.168.0/24
218.253.0.0/24
219.88.188.0/24
219.88.189.0/24
219.117.33.0/24
219.117.35.0/24
219.124.146.0/24
220.102.0.0/24
220.148.241.0/24
220.225.89.0/24
220.255.0.0/24
220.255.2.0/24
220.255.5.0/24
220.255.6.0/24
221.120.207.0/24
221.133.8.0/24
222.165.163.0/24
222.251.134.0/24
223.25.220.0/24
223.26.69.0/24
223.27.237.0/24
223.62.225.0/24
223.196.4.0/24
223.196.82.0/24
223.255.229.0/24"""

    iplist = ipl.split('\n')
    for ipd in iplist:
        ip = ipd.split('/')[0]
        # print(ip)
        # print(ip_to_lancode(ip))
        langcode = ip_to_lancode(ip)
        # langcode = find_langcode(country)
        # if langcode == 'zh':
        #     print('fefefef', find_langcode(country))