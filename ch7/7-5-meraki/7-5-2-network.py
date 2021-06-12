import meraki

API_KEY = "123456789012345678901234567890"

meraki = meraki.DashboardAPI(API_KEY)

my_net = meraki.organizations.getOrganizationNetworks("1234567890")

print (my_net)


'''
(venv) WANKIM-M-L2HC:7-5 wansookim$ python3 7-5-1-network.py 
2021-01-31 13:15:01       meraki:     INFO > Meraki dashboard API session initialized with these parameters: {'version': '1.4.3', 'api_key': '************************************5606', 'base_url': 'https://api.meraki.com/api/v1', 'single_request_timeout': 60, 'certificate_path': '', 'requests_proxy': '', 'wait_on_rate_limit': True, 'nginx_429_retry_wait_time': 60, 'action_batch_retry_wait_time': 60, 'retry_4xx_error': False, 'retry_4xx_error_wait_time': 60, 'maximum_retries': 2, 'simulate': False, 'be_geo_id': None, 'caller': None}
2021-01-31 13:15:01       meraki:     INFO > GET https://api.meraki.com/api/v1/organizations/896077/networks
2021-01-31 13:15:02       meraki:     INFO > organizations, getOrganizationNetworks; page 1 - 200 OK
[{'id': 'N_12345678901234567890', 'organizationId': '1234567890', 'name': 'meraki lab', 'productTypes': ['wireless'], 'timeZone': 'Asia/Seougs': [], 'enrollmentString': None, 'url': 'https://meraki.com', 'notes': ''}]
(venv) WANKIM-M-L2HC:7-5 wansookim$ 

'''
