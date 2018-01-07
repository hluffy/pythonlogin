# Django session
session设置，修改settings.py文件
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = False   #是否https请求传输cookie
SESSION_COOKIE_HTTPONLY = TRUE  #是否session的cookie只支持http
SESSION_COOKIE_AGE = 1209600    #cookie失效日期
SESSION_EXPIRE_AT_BROUSER_CLOSE = False #关闭浏览器是session过期
SESSION_SAVE_EVERY_REQUEST = False  #是否每次请求更新session