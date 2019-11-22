import scrapy
import csv

url_list = []

r_list = []

listof_lines = []

org_info = []

class scraping_project(scrapy.Spider):
    name = 'project_spider'

    def start_requests(self):
        num_list = [i for i in range(1,4193,10)] 

        for num in num_list:

            url_list.append("https://www.volunteermatch.org/search/orgs.jsp?aff=&r=region&l=Ohio%2C+USA&o=update&s=" + str(num))

            
        for url in url_list:
            
            yield scrapy.Request(url, callback = self.parse)


    def parse(self, response):
        r = response.xpath('//div[@class = "searchitem"]/@id').extract()
		
        for item in r:
            r_list.append(item)

        if len(r_list) == 4193:
            self.write(r_list)
    
    
    def write(self, r_list):
    
        filename = 'org_list.txt'
        
        with open(filename, 'w') as f:
            for item in r_list:
                f.write(item + '\n')
        
        
class scraping_project1(scrapy.Spider):        
    name = 'project_spider1'
    
    def start_requests(self):
        
        filename = 'org_list.txt'
        
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                line = 'https://www.volunteermatch.org/search/' + line + '.jsp'
                listof_lines.append(line)
        
        for n in range(4193):
            yield scrapy.Request(listof_lines[n], callback = self.parse)


    def parse(self, response):
        org_dict = {}
        
        org_dict['Organization Name'] = response.xpath('//span[@class = "rwd_display"]/text()').extract()[0]
        
        org_dict['Mission Statement'] = response.xpath('//span[@id = "short_mission"]/text()').extract()[0]
        
        if 'Website' in response.xpath('//h2[@class = "header_underlined"]/text()').extract():
            org_dict['Website Link'] = response.xpath('//p/a[@target = "new"]/text()').extract()[0]
        
        else:
            org_dict['Website Link'] = 'n/a'

        org_info.append(org_dict)
        
        if len(org_info) == 4193:
            self.write(org_info)
    
    def write(self, org_info):
    
        filename = 'organization_info.csv'
        
        with open(filename, 'w', encoding="utf-8") as f:
            w = csv.DictWriter(f, ['Organization Name', 'Mission Statement', 'Website Link'])
            
            w.writeheader()
            
            for row in org_info:
                w.writerow(row)

    