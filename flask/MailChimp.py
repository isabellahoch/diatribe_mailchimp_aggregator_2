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

	def get_content(self):
		request_auth = (self.user, self.api_key)
		request_url = "https://" + self.region + ".api.mailchimp.com/3.0/campaigns/" + self.id + "/content"
		response = requests.get(request_url, auth=request_auth)
		if response.status_code != 200:
			return False
		return response.json()

	def get_email_content_links_by_type(self):
		content = self.get_content()
		type_1_img_src = "http://diatribe.org/sites/default/files/styles/diabetes_icon_articles/public/type-1.png"
		type_2_img_src = "http://diatribe.org/sites/default/files/styles/diabetes_icon_articles/public/type-2.png"
		type_1_2_img_src = "http://diatribe.org/sites/default/files/styles/diabetes_icon_articles/public/type-1-2.png"

		if not content:
			return False
		all_links = {"t1":list(), "t2":list(), "t1t2":list()}

		# Get all links next to the desired image references
		if "variate_contents" not in content:
			html = content["html"]
			f = open("../email_html_examples/"+self.id+".html", "w")
			f.write(html)
			f.close()
			tabs = html.split("<table")
			for table_div in tabs:
				if type_1_img_src in table_div:
					link = table_div.split("href=\"")[1].split("\"")[0]
					if link not in all_links["t1"]:
						all_links["t1"].append(link)
				if type_2_img_src in table_div:
					link = table_div.split("href=\"")[1].split("\"")[0]
					if link not in all_links["t2"]:
						all_links["t2"].append(link)
				if type_1_2_img_src in table_div:
					link = table_div.split("href=\"")[1].split("\"")[0]
					if link not in all_links["t1t2"]:
						all_links["t1t2"].append(link)
		else:
			for variate in content["variate_contents"]:
				html = variate["html"]
				f = open("../email_html_examples/"+self.id+".html", "w")
				f.write(html)
				f.close()
				tabs = html.split("<table")
				for table_div in tabs:
					if type_1_img_src in table_div:
						link = table_div.split("href=\"")[1].split("\"")[0]
						if link not in all_links["t1"]:
							all_links["t1"].append(link)
					if type_2_img_src in table_div:
						link = table_div.split("href=\"")[1].split("\"")[0]
						if link not in all_links["t2"]:
							all_links["t2"].append(link)
					if type_1_2_img_src in table_div:
						link = table_div.split("href=\"")[1].split("\"")[0]
						if link not in all_links["t1t2"]:
							all_links["t1t2"].append(link)


		print("\n\n\n\n")
		print(content)
		print("\n\n\n\n")
		exit()


		return all_links




test = MailChimp(mailchimp_api_key, mailchimp_region, mailchimp_user)
camp_ids = test.get_campaigns(get_all=False, return_ids=True)

for camp_id in camp_ids:

	camp = MailChimpCampaign(test, camp_id)
	print(camp_id)
	print(camp.get_email_content_links_by_type())






