f = open('nginx_logs.txt', 'r', encoding='utf-8')

remote_addr = ''
request_type = ''
requested_resource = ''
result = []

for line in f:
    line = line.split(' ')
    remote_addr = line[0]
    request_type = line[5].replace('"', '')
    requested_resource = line[6]
    result_el = (remote_addr, request_type, requested_resource)
    result.append(result_el)

print(result)
 #print(result[0]) #это для сверки 0-го элемента списка
 #print(result[-1]) #это для сверки последнего элемента списка

f.close()