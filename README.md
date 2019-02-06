# Automate It

The collection of ideas(or short examples) of performing personal experiments on automation tools.   

1. [Node-RED flow deployment with Ansible](https://github.com/phyunsj/automate-it/blob/master/README.md)
2. TBD
3. TBD

## 1. Node-RED flow deployment with [Ansible](https://www.ansible.com/)

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible.png" width="100px"/>
</p>

#### About Ansible

Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. ... _from [Ansible Document](https://docs.ansible.com/ansible/latest/index.html)_

Ansible manages machines(or nodes) in an **agent-less manner**. Ansible connects via SSH to the machines it wants to manage and **pushes** what it’s supposed to do. 

### Prerequisites

**Mac:** Install `ansible` 

> $ brew install ansible 

**Mac:** Install `sshpass`

> $ brew install http://git.io/sshpass.rb 

**Mac:** Create `hosts`(inventory) in /etc/ansible or designated location (`-i` option).

```
[dev]
111.222.333.444 ansible_user=pi

[prod]
555.666.777.888 ansible_user=pi
```

**Pi:** Install OS Images

https://www.raspberrypi.org/downloads/raspbian/ download **Raspbian Stretch with desktop and recommended software**(`2018-11-13-raspbian-stretch-full.zip`) for this example.
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

**Pi:** Enable `ssh`

https://www.raspberrypi.org/documentation/remote-access/ssh/

**Pi:** Install `npm` (Palette Manager won't be visible from node-red). Restart node-red after `npm` installation.

```
 $ sudo systemctl stop nodered.service (or node-red-stop)
 $ sudo apt update 
 $ sudo apt install npm
 $ sudo systemctl start nodered.service (or node-red-start)
```

**Pi:** Install `node-red-dashboard` from Palette Manager or CLI.

> $ cd $HOME/.node-red && npm install node-red-dashboard 

**Pi:** Edit `settings.js`

```
 // The file containing the flows. If not set, it defaults to flows_<hostname>.json
 flowFile: 'flows.json', // uncomment this line
```

###  In Action 

In this example,two playbooks(flow1.yml & flow2.yml) were executed one after another and new flow.json was copied over to Pi each time.

```
$ ansible-playbook -i hosts -k flow1.yml  

```

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible-node-red-flow-change-text.gif" width="700px"/>
</p>
