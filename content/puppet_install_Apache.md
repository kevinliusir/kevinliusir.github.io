Title: Puppet(二)简单安装配置Apache  
Date: 2015-01-08 10:30  
Modified: 2015-01-08 10:30   
Category: 运维自动化    
Tags: puppet   
Slug: puppet_install_Apache   
Author: Kevin
# Puppet(二)简单安装配置Apache #


操作系统：CentOS6.6  
master.feisblog.com	192.168.212.100   
agent.feisblog.com	192.168.212.110

    

## 1. 创建模块目录 ##
`#mkdir -p /etc/puppet/modules/httpd/{manifests,templates,files}`



## 2. 创建安装httpd类 ##
```ruby   
#vim /etc/puppet/modules/httpd/manifests/install.pp 
class httpd::install { 
	 package { [ "httpd" ]: 
       ensure => present,
   }
}	
```
    
##3. 创建启动httpd服务类
```ruby
#vim /etc/puppet/modules/httpd/manifests/service.pp  
class httpd::service {
  service { "httpd":
	ensure => running,
	hasstatus => true,
	hasrestart => true,
	enable => true,
	require => Class["httpd::install"],
  }
}
```
##4. 创建httpd 配置文件类，配置文件通过puppet获取（目录：/etc/puppet/modules/httpd/files/httpd.conf）
```ruby
#vim /etc/puppet/modules/httpd/manifests/conf.pp
class httpd::conf {
  file { "httpd.conf":
	ensure => present,
	owner => 'root',
	group => 'root',
	mode => '644',
	path => '/etc/httpd/conf/httpd.conf',
	source => 'puppet:///modules/httpd/httpd.conf',
	require => Class["httpd::install"], 
	notify => Class["httpd::service"], 
  }
}
```
##5. 创建主配置文件init.pp 
```ruby
#vim /etc/puppet/modules/httpd/manifests/init.pp
class httpd { 
	include httpd::install, httpd::service, httpd::conf
} 
```
##6. 配置客户端节点 
```ruby    
#vim /etc/puppet/manifests/nodes/agent.feisblog.com.pp
node 'agent.feisblog.com' {
   include httpd
} 
```
##7. 将节点载入puppet的site.pp 文件
```ruby
#vim /etc/puppet/manifests/site.pp
import "nodes/agent.feisblog.com.pp"
```    
##8. 在agent端
`#puppet agent --test --server master.feisblog.com --noop`			

`#puppet agent --test --server master.feisblog.com `


