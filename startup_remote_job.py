import requests
import time

# 远程触发jenkins
REMOTE_URL = 'http://192.168.12.24'
PORT = '8080'
PROJECT_NAME = 'call_sosotest'
TOKEN = '123456'
REMOTE_JOB_URL = '%s:%s/jenkins/job/%s/build?token=%s' % (REMOTE_URL, PORT, PROJECT_NAME, TOKEN)
REMOTE_JENKINS_LOGIN_URL = '%s:%s/jenkins/j_acegi_security_check' % (REMOTE_URL, PORT)
print(REMOTE_JOB_URL)
# 等待解压 10分钟
print('wait~')
# time.sleep(10*60)
print('10分钟等待结束~')
session = requests.session()
bady = {
    'j_username': 'root',
    'j_password': 'root1',
    'from': '/jenkins/',
    'Submit': '登录'
}

# 关闭重定向，登录获取token
response = session.post(
    url=REMOTE_JENKINS_LOGIN_URL,
    data=bady,
    allow_redirects=False
)
# 触发远程job
result = session.get(
    url=REMOTE_JOB_URL
)

print(result.text)
assert result.text == ''








