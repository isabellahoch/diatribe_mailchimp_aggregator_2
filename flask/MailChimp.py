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

		return response.json()["campaigns"]


	def get_campaign_report(self, campaign_id):
		request_auth = (self.user, self.api_key)
		request_url = "https://" + self.region + ".api.mailchimp.com/3.0/reports/" + campaign_id	
		response = requests.get(request_url, auth=request_auth)
		if response.status_code != 200:
			return False
		return response.json()









test = MailChimp(mailchimp_api_key, mailchimp_region, mailchimp_user)
camp_ids = test.get_campaigns(get_all=False, return_ids=True)

camp_details = test.get_campaign_report(camp_ids[0])


for foo in camp_details:
	print(foo)


print(camp_details["_links"])
	





