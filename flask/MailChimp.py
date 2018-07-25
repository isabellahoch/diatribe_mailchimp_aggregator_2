import requests
from credentials import mailchimp_api_key, mailchimp_region, mailchimp_user

class MailChimp:

	def __init__(self, api_key, region, user):
		self.api_key = api_key
		self.region = region
		self.user = user

	def get_campaigns(self, get_all, return_ids=False):
		if get_all:
			num_to_get = 10000 # a large number
		else:
			num_to_get = 10
		request_params = (("count",num_to_get),)
		request_auth = (self.user, self.api_key)
		request_url = "https://" + self.region + ".api.mailchimp.com/3.0/campaigns"
		response = requests.get(request_url, params=request_params, auth=request_auth)
		if response.status_code != 200:
			return False
		
		if return_ids:
			return [campaign["id"] for campaign in response.json()["campaigns"]]

		return response.json()

	def get_campaign_report(self, campaign_id):
		request_auth = (self.user, self.api_key)
		request_url = "https://" + self.region + ".api.mailchimp.com/3.0/reports/" + campaign_id	
		response = requests.get(request_url, auth=request_auth)
		if response.status_code != 200:
			return False
		return response.json()

	def get_campaign_click_report(self, campaign_id):
		request_auth = (self.user, self.api_key)
		request_url = "https://" + self.region + ".api.mailchimp.com/3.0/reports/" + campaign_id + "/click-details"
		response = requests.get(request_url, auth=request_auth)
		if response.status_code != 200:
			return False
		return response.json()

	def get_campaign_content(self, campaign_id):
		request_auth = (self.user, self.api_key)
		request_url = "https://" + self.region + ".api.mailchimp.com/3.0/campaigns/" + campaign_id + "/content"
		response = requests.get(request_url, auth=request_auth)
		if response.status_code != 200:
			return False
		return response.json()




class MailChimpCampaign:

	def __init__(self, chimp, campaign_id):
		self.id = campaign_id
		self.chimp = chimp
		self.api_key = self.chimp.api_key
		self.region = self.chimp.region
		self.user = self.chimp.user




test = MailChimp(mailchimp_api_key, mailchimp_region, mailchimp_user)
camp_ids = test.get_campaigns(get_all=False, return_ids=True)



content = test.get_campaign_content(camp_ids[0])

for foo in content["variate_contents"]:
	for i in foo:
		print(i)


print(content["variate_contents"][0]["html"])


"""
for camp in camp_ids:
	urls = test.get_campaign_click_report(camp)["urls_clicked"]
	for url in urls:
		print(url["url"] + "  :  " + str(url["total_clicks"]))
"""



