import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

config = dotenv_values(".env")

filters = []

# response = requests.get("https://www.linkedin.com/search/results/people/?keywords=%22CTO%22%20AND%20%22Industrial%20Company%22%20AND%20%22Europe%22&origin=SWITCH_SEARCH_VERTICAL&sid=XhJ"

def get_csrf_token():
    page  = requests.get("https://linkedin.com/")
    soup = BeautifulSoup(page.text, features="html.parser")
    return soup.find('input', attrs={'name': 'loginCsrfParam'})['value']


csrf = get_csrf_token()

payload={
    'session-key' : config['USER_EMAIL'],
    'session-password' : config['USER_PASSWORD'],
    'loginCsrfParam': csrf,
}

URL='https://www.linkedin.com/uas/login'
session =requests.session()
session.post(URL,data=payload)

r=session.get('https://www.linkedin.com/')
soup = BeautifulSoup(r.text, features = "html.parser")
print(soup.find('title'))


##cookies
# JSESSIONID	
# li_gc
# lidc
# lang
# bcookie	
# bscookie
# li_alerts
# G_ENABLED_IDPS

##Headers
# cache-control: no-cache, no-store
# content-length: 0
# content-security-policy: default-src *; connect-src 'self' *.licdn.com *.linkedin.com wss://*.linkedin.com dpm.demdex.net/id lnkd.demdex.net blob: accounts.google.com/gsi/ *.microsoft.com; img-src data: blob: *; font-src data: *; style-src 'unsafe-inline' 'self' static-src.linkedin.com *.licdn.com; script-src 'unsafe-inline' 'unsafe-eval' 'self' spdy.linkedin.com static-src.linkedin.com *.ads.linkedin.com *.licdn.com static.chartbeat.com bcvipva02.rightnowtech.com www.bizographics.com sjs.bizographics.com js.bizographics.com d.la4-c1-was.salesforceliveagent.com platform.linkedin.com platform-akam.linkedin.com platform-ecst.linkedin.com platform-azur.linkedin.com; object-src 'none'; media-src blob: *; worker-src blob: 'self'; frame-src blob: lnkd-communities: voyager: *; frame-ancestors 'self' *.linkedin.com www.linkedin.cn; report-uri /security/csp?e=p&f=rl
# date: Sat, 21 Jan 2023 18:49:38 GMT
# expect-ct: max-age=86400, report-uri="https://www.linkedin.com/platform-telemetry/ct"
# expires: Thu, 01 Jan 1970 00:00:00 GMT
# location: https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit
# pragma: no-cache
# set-cookie: lang=v=2&lang=en-us; Domain=linkedin.com; Path=/; Secure; SameSite=None
# set-cookie: wwepo=delete me; Domain=.www.linkedin.com; Max-Age=0; Expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/; Secure; SameSite=None
# set-cookie: chp_token=delete me; Domain=.www.linkedin.com; Max-Age=0; Expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/; Secure; SameSite=None
# set-cookie: liap=true; Domain=.linkedin.com; Max-Age=7776000; Expires=Fri, 21 Apr 2023 18:49:38 GMT; Path=/; Secure; SameSite=None
# set-cookie: li_at=AQEDASw3l14CnsJZAAABhdWqMCsAAAGF-ba0K00Ar-VJQu9Ie6jfXb4kpYp0WadMcP-JBZmZjxMo8bNMLXjBiB8JOuhwq940ZxlggnbgUsbjbA9_Y6THPzkJWim4fNbsjwHKKv8-eHGvFCusPTCWo4K7; Domain=.www.linkedin.com; Max-Age=31536000; Expires=Sun, 21 Jan 2024 18:49:38 GMT; Path=/; HttpOnly; Secure; SameSite=None
# set-cookie: JSESSIONID="ajax:5550894944830362304"; Domain=.www.linkedin.com; Max-Age=7776000; Expires=Fri, 21 Apr 2023 18:49:38 GMT; Path=/; Secure; SameSite=None
# set-cookie: bcookie="v=2&f17dd592-e13e-4113-8f53-f6930755d81f"; Domain=.linkedin.com; Expires=Sun, 21-Jan-2024 18:49:38 GMT; Path=/; Secure; SameSite=None
# set-cookie: bscookie="v=1&202301211849093021e151-0f5a-472c-81b4-9ec2e4aaf451AQFZmuZJ3Bzq9AoLzpvFhqCXVcOvl3nW"; Domain=.www.linkedin.com; Expires=Sun, 21-Jan-2024 18:49:38 GMT; Path=/; HttpOnly; Secure; SameSite=None
# strict-transport-security: max-age=31536000
# x-cache: CONFIG_NOCACHE
# x-content-type-options: nosniff
# x-frame-options: sameorigin
# x-fs-uuid: 0005f2caa0c917328afea6781c786a94
# x-li-fabric: prod-lva1
# x-li-pop: afd-prod-lva1-x
# x-li-proto: http/2
# x-li-uuid: AAXyyqDJFzKK/qZ4HHhqlA==
# x-msedge-ref: Ref A: 9174A901040C45EE8181B075ADC1D91A Ref B: FRAEDGE1410 Ref C: 2023-01-21T18:49:38Z