### run python files in different terminals:
1. python replica_server.py 5001  
2. python replica_server.py 5002  
3. python replica_server.py 5003  
4. python origin_server.py   
5. python controller.py  

### add some mappings in C:\Windows\System32\drivers\etc\hosts.
'127.0.0.1 controller.com  
127.0.0.1 replica1.com  
127.0.0.1 replica2.com  
127.0.0.1 replica3.com'

### certificates and privates keys are generated by mkcert:
'mkcert controller.com replica1.com replica2.com replica3.com'  

### config caddyFile:
'controller.com {
    reverse_proxy localhost:5004
    tls D:\Caddy\certs\controller.com+3.pem D:\Caddy\certs\controller.com+3-key.pem
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

### run caddy in the directory where caddy.exe exists as admin:
'caddy run'

### go to page of controller https://controller.com
