Title: Docker Machine 创建Swarm 集群  
Date: 2017-03-15 23:30  
Modified: 2017-03-15 23:30   
Category: docker    
Tags: docker   
Slug: Docker_Machine_Create_Swarm_Cluster   
Author: Kevin
# 1swarm主节点

```
#docker run swarm create
a03ab86659df32ea3813d748f8a42f82
```


```
docker-machine create \
-d virtualbox \
--swarm \
--swarm-master \
--swarm-discovery token://a03ab86659df32ea3813d748f8a42f82 \
swarm-master
```

# 2创建Swarm从节点

```
docker-machine create \
-d virtualbox \
--swarm \
--swarm-discovery token://<TOKEN-FROM-ABOVE> \
swarm-node
```
# 3. 测试和查看
然后，我们就可以跨节点地运行我们所需的容器了。在这里，我们还要检查一下是否一切正常。所以，运行docker info命令来检查Swarm集群的信息。
# docker info
