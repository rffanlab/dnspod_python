#-*- encoding:utf-8 -*-
import urllib2,urllib,json
print "请输入您的DNSPOD 登录email"
dnspod_email = raw_input('DNSPod Email:')
print '请输入您的DNSPOD 登录密码'
dnspod_password = raw_input('DNSPod Password:')
yourdomains = raw_input('请输入要更改的域名:')
yourrecord = raw_input('请输入您要更改的记录值：')
new_ips = raw_input('请输入需要更改的IP :')

print new_ips
data={'login_email':dnspod_email,'login_password':dnspod_password,'format':'json'}
f = urllib2.urlopen(
   url = 'https://dnsapi.cn/Domain.list',
   data = urllib.urlencode(data)
   )
jsondata = f.read()
cdjson = json.loads(jsondata)
cdjson2=cdjson['domains']
# yourdomains = 'rffan.info'
for x in range(len(cdjson2)):
   if cdjson2[x]['name'] == yourdomains:
      break

domainrecordid = cdjson2[x]['id']

print 'Domain',cdjson2[x]['name']
print 'Domain ID is :',cdjson2[x]['id']
data2={'login_email':dnspod_email,'login_password':dnspod_password,'format':'json','domain_id':cdjson2[x]['id']}
getDomainrecord = urllib2.urlopen(
   url = 'https://dnsapi.cn/Record.List',
   data = urllib.urlencode(data2)
   )
getDomainrecordJSON = getDomainrecord.read()
DomainRecord = json.loads(getDomainrecordJSON)
for xr in range(len(DomainRecord['records'])):
   if DomainRecord['records'][xr]['name'] == yourrecord:
      break

# print DomainRecord['records'][xr]
print 'Record:',DomainRecord['records'][xr]['name']
print 'Last RecordIP:',DomainRecord['records'][xr]['value']


new_data = {'login_email':dnspod_email,'login_password':dnspod_password,'format':'json','domain_id':cdjson2[x]['id'],'record_id':DomainRecord['records'][xr]['id'],'sub_domain':DomainRecord['records'][xr]['name'],'record_type':'A','record_line':'默认','value':new_ips}

fnew = urllib2.urlopen(
   url = 'https://dnsapi.cn/Record.Modify',
   data = urllib.urlencode(new_data)
   )
recive = fnew.read()
