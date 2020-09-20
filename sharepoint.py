# import json
# from office365.runtime.auth.UserCredential import UserCredential
# from office365.runtime.http.request_options import RequestOptions
# from office365.sharepoint.client_context import ClientContext

# site_url = 'https://o365ku.sharepoint.com/sites/6140205888/Lists/Student/AllItems.aspx'
# username = "sanayut.t@live.ku.th"
# password = "Art@7582009"

# ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
# web = ctx.web
# ctx.load(web)
# ctx.execute_query()
# print("Web title: {0}".format(web.properties['Title']))


# https://o365ku.sharepoint.com/sites/6140205888/Lists/Student/AllItems.aspx

import json
from office365.runtime.auth.UserCredential import UserCredential
from office365.runtime.http.request_options import RequestOptions
from office365.sharepoint.client_context import ClientContext

site_url = 'https://o365ku.sharepoint.com/sites/6140205888/Lists/Student/AllItems.aspx'
username = "sanayut.t@live.ku.th"
password = "Art@7582009"


ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))
request = RequestOptions("{0}/_api/web/".format(site_url))
response = ctx.execute_request_direct(request)
json = json.loads(response.content)
web_title = json['d']['Title']
print("Web title: {0}".format(web_title))