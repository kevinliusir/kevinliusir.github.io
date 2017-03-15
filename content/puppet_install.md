Title: Puppet(一) 安装  
Date: 2015-01-07 10:30  
Modified: 2015-01-07 10:30   
Category: 运维自动化    
Tags: puppet   
Slug: puppet_install   
Author: Kevin
# Puppet(一) 安装 #
操作系统：Centos6.6  
--------------------- | -------------
master.feisblog.com	  | 192.168.212.100
agent.feisblog.com    | 192.168.212.110

## 1安装Centos EPEL 源     ##
`#rpm -ivh  http://mirrors.yun-idc.com/epel/6/x86_64/epel-release-6-8.noarch.rpm`   
## 2.安装puppetLabs 源 ##   
`#rpm -ivh http://yum.puppetlabs.com/el/6Server/products/x86_64/puppetlabs-release-6-11.noarch.rpm`   
## 3.安装服务器端   ##
`#yum install puppet-server`   
检查安装：   
`#puppet -V`   
`#facter -v`   
## 4.在客户端   ## 
`#yum install puppet`   

## 5.配置    ##
- 5.1 主机名和host 文件的修改   
- 5.2 设置NTP时间同步   
    在crontab中加入：	   
`*/10 * * * *  ntpdate -s time.nist.gov`  
- 5.3 配置site.pp   
`#vim /etc/puppet/manifests/site.pp`   
```ruby
node default { 
	file {“/tmp/puppettest1.txt”: 
		content => “Hello World”;
	}
}
```
 
## 6.启动服务  ##
```shell
#/etc/init.d/puppetmaster start
#chkconfig puppetmaster on  
#/etc/init.d/puppet start 
#chkconfig puppet on 
```
## 7.客户端测试   ##  
首先是发起验证  
`# puppet agent --test --server server`    
服务器端完成验证      
`#puppet cert --list`   
`#puppet cert sign agent.feisblog.com`




