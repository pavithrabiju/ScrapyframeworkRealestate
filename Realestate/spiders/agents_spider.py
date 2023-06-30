import scrapy
import json

class AgentsSpider(scrapy.Spider):
    name = 'agents'
    start_urls = ['https://www.bhhsamb.com/agents']

    def parse(self, response):
        # Extract agent details
        agents = response.xpath('//div[contains(@class, "agent-details")]')
        data = []
        for agent in agents:
            name = agent.xpath('.//h2/a/text()').get().strip()
            job_title = agent.xpath('.//h3/text()').get().strip()
            image_url = agent.xpath('.//img/@src').get()
            address = agent.xpath('.//p[contains(@class, "agent-address")]/text()').get().strip()
            contact_details = agent.xpath('.//p[contains(@class, "agent-contact-info")]/text()').get().strip()
            office = agent.xpath('.//p[contains(@class, "agent-office")]/text()').get().strip()
            fax = agent.xpath('.//p[contains(@class, "agent-fax")]/text()').get().strip()
            cell = agent.xpath('.//p[contains(@class, "agent-cell")]/text()').get().strip()
            social_accounts = agent.xpath('.//div[contains(@class, "agent-social")]/a/@href').getall()
            languages = agent.xpath('.//p[contains(@class, "agent-languages")]/text()').get().strip()
            description = agent.xpath('.//div[contains(@class, "agent-description")]/text()').get().strip()

            agent_data = {
                'Name': name,
                'Job Title': job_title,
                'Image URL': image_url,
                'Address': address,
                'Contact Details': contact_details,
                'Office': office,
                'Fax': fax,
                'Cell': cell,
                'Social Accounts': social_accounts,
                'Languages': languages,
                'Description': description
            }
            data.append(agent_data)

        # Save data as JSON
        filename = 'agents.json'
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        self.log(f'Saved data to {filename}')