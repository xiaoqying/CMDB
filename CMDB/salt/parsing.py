from salt import conf_set
from utils import send_salt_api
import json
dic = {}
dic2 = {}
#将salt-api发过来的数据进行解析
class ResApi(object):
    def info(self,arg):
        try:
            for k,v in arg.items():
                    if k.isalnum():
                        self.info(v)
                        dic[k] =v
                    else:
                        dic[k] = v
        except AttributeError:
            pass

    def parsing(self,arg):
        for j,p in arg.items():
            self.info(arg[j])
            host = dic['id']
            ip_interfaces = dic['ip_interfaces']['ens192'][0]
            oscodename = dic['osfinger']
            mem_total = dic['mem_total']
            mem_total = str(round(int(mem_total) / 1024)) + ('G')
            dic2[host]=ip_interfaces,oscodename,mem_total
        return dic2



# api = send_salt_api.SaltApi
# api_url = send_salt_api.salt_api
# salt = api(api_url)
# salt_client = 'python'
# # salt_test = 'free -h'
# salt_method = 'cmd.run'
# salt_params = 'df -h'
#
# result2 = salt.salt_command(salt_client, salt_method, salt_params)
# # for k,v in result2.items():
# #     print(v)
# for disk,value in result2.items():
#     # font_size=str(round(int(value['1K-blocks']) /1024 /1024,2)) +('G')
#     # print('目录',disk,'磁盘大小',font_size)
#     print(value)
# result1 = salt.salt_command(salt_client, salt_test)
# print(result2)



