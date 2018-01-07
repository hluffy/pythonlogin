# Django session
session设置，修改settings.py文件		
1. SESSION_COOKIE_NAME = 'sessionid'		
2. SESSION_COOKIE_PATH = '/'		
3. SESSION_COOKIE_DOMAIN = None		
4. SESSION_COOKIE_SECURE = False   #是否https请求传输cookie		
5. SESSION_COOKIE_HTTPONLY = TRUE  #是否session的cookie只支持http		
6. SESSION_COOKIE_AGE = 1209600    #cookie失效日期		
7. SESSION_EXPIRE_AT_BROUSER_CLOSE = False #关闭浏览器是session过期		
8. SESSION_SAVE_EVERY_REQUEST = False  #是否每次请求更新session