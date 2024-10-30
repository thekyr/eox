### Cisco EoX Script

#### eox.py
The script collects the EoX milestones from Cisco Smartnet Total Care EOX API

#### Requirements
In order for the script to work you need to register to the "EOX API" provided at [https://apiconsole.cisco.com/](https://apiconsole.cisco.com/) and create an application with client_credentials. 

Cisco API documentation can be found at [https://developer.cisco.com/docs/support-apis/](https://developer.cisco.com/docs/support-apis/)

EoX API: https://developer.cisco.com/docs/support-apis/eox/

The client_id and client_secret tht will be generated after the application creation will need to be defined in the eox.py script at:

```
CLIENT_ID = '<client_id'>
CLIENT_SECRET = 'client_secret>'
```

#### Usage
python eox.py
