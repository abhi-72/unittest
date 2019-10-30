import requests
import os,json,traceback

class MCTestRequestHandler:

    def __init__(self,url,data):
        self.base_url = url
        self.token = self.login(data)['token']

    def login(self,data):
        url = os.path.join(self.base_url, 'login/')
        data = json.dumps(data).encode('utf-8')
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url=url,data=data,headers=headers)
        res = json.loads(req.text)
        if res is None or res == '':
            return ''
        else:
            if 'error' in res: #Error Condition
                #if res['error']['code'] == 5002:
                if 'code' in res and res['code'] == 5002:
                    return res
                else:
                    raise Exception('ERROR {0}, Reason:{1}'.format(res['error']['code'],o['error']['message']))
            return res

    def get(self,api):
        url = os.path.join(self.base_url,api)
        headers = {'Content-Type': 'application/json','x-access-token':self.token}
        req = requests.get(url=url,headers=headers)
        res = json.loads(req.text)
        if res is None or res == '':
            return ''
        else:
            if 'error' in res: #Error Condition
                if 'code' in res and res['code'] == 5002:
                    return res
                else:
                    #raise Exception('ERROR {0}, Reason:{1}'.format(o['error']['code'],o['error']['message']))
                    raise Exception('ERROR, Reason:{}'.format(res['error']))
            return res

    def post(self,api,data):
        url = os.path.join(self.base_url,api)
        data = json.dumps(data).encode('utf-8')
        headers = {'Content-Type': 'application/json','x-access-token':self.token}
        req = requests.post(url=url,data=data,headers=headers)
        res = json.loads(req.text)
        if res is None or res == '':
            return ''
        else:
            if 'error' in res: #Error Condition
                if 'code' in res and res['code'] == 5002:
                    return res
                else:
                    #raise Exception('ERROR {0}, Reason:{1}'.format(o['error']['code'],o['error']['message']))
                    raise Exception('ERROR, Reason:{}'.format(res['error']))
            return res

    def upload(self,api,username,zipname):
        url = os.path.join(self.base_url, api)
        with open(zipname, 'rb') as f:
            zipname = zipname.split('/')[-1]
            req = requests.post(
                            url = url,
                            #auth=(base, pwd),
                            #data=f,
                            headers={
                                    'username': username,
                                    'x-access-token':self.token,
                                    #'X-File-Name' : zipname,
                                    #'Content-Disposition': 'form-data; name="{0}"; filename="{0}"'.format(zipname),
                                    #'content-type': 'multipart/form-data'
                                    },
                            files={'archive': (zipname, f, 'application/zip')},
                            )
        res = json.loads(req.text)
        if res is None or res == '':
            return ''
        else:
            if 'error' in res: #Error Condition
                if res['error']['code'] == 5002:
                    return res
                else:
                    raise Exception('ERROR {0}, Reason:{1}'.format(o['error']['code'],o['error']['message']))
            return res


#loginres = mcreqhan.login('login/')
#.upload('upload/','abhinav',self.archive)
