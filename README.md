# tensorflow-kr-docker
slide : http://www.slideshare.net/EricAhn/tensorflow-in-docker 


```
$ git clone https://github.com/bwahn/tensorflow-kr-docker.git

$ cd tensorflow-kr-docker

$ docker-compose -f docker-compose.yaml
```

Jupyter : http://192.168.99.101:8888/tree

```
intro_word2vec_distributed.ipynb
=> url = 'http://mattmahoney.net/dc/'
=> filename = maybe_download('text8.zip', 31344016)
```

```
$ mkdir weave

$ cd weave

$ wget -O docker-compose.yml http://git.io/scope-compose

$ docker-compose up -d


$ docker ps -a

CONTAINER ID  IMAGE            PORTS                 NAMES
fe41c10a63ca  tns_lb1:latest   0.0.0.0:8001->80/tcp  tns_lb1_1
c94005d87115  tns_lb2:latest   0.0.0.0:8002->80/tcp  tns_lb2_1
8c15a1325094  tns_app1:latest  8080/tcp              tns_app1_1
645386356a2e  tns_app2:latest  8080/tcp              tns_app2_1
e34ccea042fd  tns_db3:latest   9000/tcp              tns_db3_1
c0d53d1327b4  tns_db2:latest   9000/tcp              tns_db2_1
0a920e17818a  tns_db1:latest   9000/tcp              tns_db1_1
```


Weave Scope is reachable at the following URL(s):
  * http://192.168.99.101:4040/
