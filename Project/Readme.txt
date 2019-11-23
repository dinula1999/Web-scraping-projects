This PYTHON SCRIPT will scrape https://www.volunteermatch.org/search/orgs.jsp website's non-profit organization data as follows.

***The first spider will scrape the pages necessary to get each organization links.

***Second spider will scrape each organization page for Oraganization Name, Mission Statement and Website(Some org's don't have websites).

___________________________________________________________________________________________________________________________________________
						INSTRUCTIONS

First and foremost you have to download and install Python (https://www.python.org/downloads/)

Go to the command line or terminal in your computer and install the following libraries using pip.
	***Scrapy (http://docs.scrapy.org/en/latest/intro/install.html)

After downloading the Project folder locate that folder in terminal(MacOs,Linux) or commandline(Windows).

***Use this command - scrapy crawl project_spider

***afeter that use this command -  scrapy crawl project_spider1

You will see org_list.txt and organization_info.csv in the Project folder.

