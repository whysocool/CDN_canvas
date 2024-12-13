### run python files in different terminals:
1. python replica_server.py 5001  
2. python replica_server.py 5002  
3. python replica_server.py 5003  
4. python origin_server.py   
5. python controller.py  

### add some mappings in hosts.
'127.0.0.1 controller.com  
127.0.0.1 replica1.com  
127.0.0.1 replica2.com  
127.0.0.1 replica3.com  '

### config caddyfile:
'tls D:\Caddy\certs\controller.com+3.pem D:\Caddy\certs\controller.com+3-key.pem
}

replica1.com {
    reverse_proxy localhost:5001
    tls D:\Caddy\certs\controller.com+3.pem D:\Caddy\certs\controller.com+3-key.pem
}

replica2.com {
    reverse_proxy localhost:5002
    tls D:\Caddy\certs\controller.com+3.pem D:\Caddy\certs\controller.com+3-key.pem
}

replica3.com {
    reverse_proxy localhost:5003
    tls D:\Caddy\certs\controller.com+3.pem D:\Caddy\certs\controller.com+3-key.pem
}'

### run caddy in the directory where caddy.exe exists:
'caddy run'

### go to page of controller https://controller.com
