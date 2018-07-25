# diatribe_mailchimp_aggregator
Aggregating MailChimp email statistics using Flask &amp; MongoDB

## Requirements

Install (with pip): flask, requests, pymongo.

## Database

The flask app will be taking information from a MongoDB non relational database. This will have the following collections:

- Campaigns
- Members

## Website Structure

An initial website structure proposal:

- / : Home (some sort of landing page)
- /login : Login page
- /logout : Logout page
- /register : Registration page (I have to think about whether we'd want registration to be an option, or just create accounts manually)
- /campaigns : This is the page where the user sees a list of all campaigns, as well as some global information on each one
- /campaigns/campaign_id : View detailed statistics on a specific campaign
- /members : View the characteristics the mailing list such as diabetes type (estimated from click data), usage, click rate, etc.


