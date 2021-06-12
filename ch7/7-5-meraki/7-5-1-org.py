import meraki

API_KEY = "123456789012345678901234567890"

meraki = meraki.DashboardAPI(API_KEY)

my_orgs = meraki.organizations.getOrganizations()
print (my_orgs)

'''
(venv) WANKIM-M-L2HC:7-5 wansookim$ python3 7-5-1-org.py 
2021-01-31 13:13:19       meraki:     INFO > Meraki dashboard API session initialized with these parameters: {'version': '1.4.3', 'api_key': '************************************5606', 'base_url': 'https://api.meraki.com/api/v1', 'single_request_timeout': 60, 'certificate_path': '', 'requests_proxy': '', 'wait_on_rate_limit': True, 'nginx_429_retry_wait_time': 60, 'action_batch_retry_wait_time': 60, 'retry_4xx_error': False, 'retry_4xx_error_wait_time': 60, 'maximum_retries': 2, 'simulate': False, 'be_geo_id': None, 'caller': None}
2021-01-31 13:13:19       meraki:     INFO > GET https://api.meraki.com/api/v1/organizations
2021-01-31 13:13:21       meraki:     INFO > organizations, getOrganizations - 200 OK
[{'id': '1234567890', 'name': 'meraki lab', 'url': 'https://meraki.com//organization/overview'}]
(venv) WANKIM-M-L2HC:7-5 wansookim$ 
'''