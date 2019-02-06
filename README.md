# Automate It

The collection of ideas & the personal experiments (short examples) on automation tools.   

1. [Node-RED flow deployment with Ansible](https://github.com/phyunsj/automate-it/blob/master/README.md)
2. TBD
3. TBD

## 1. Node-RED flow deployment with [Ansible](https://www.ansible.com/)

Flow re-deployment had been discussed (i.g., [How can I remotely deploy a flow file in Node-RED?](https://stackoverflow.com/questions/42143597/how-can-i-remotely-deploy-a-flow-file-in-node-red) ) I explored different options meeting the following criteria:

1. **simple** 
2. supports scripts
3. control node-red stop/start
4. flow.json re-deployment
5. module management (install/uninstall/update) 

**IMO** After spending a few days of watching clips & reading examples, **Ansible** easily meets this requirements.

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible.png" width="100px"/>
</p>

#### About Ansible

Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. ... _from [Ansible Document](https://docs.ansible.com/ansible/latest/index.html)_

Ansible manages machines(or nodes) in an **agent-less manner**. Ansible connects via SSH to the machines it wants to manage and **pushes** what it’s supposed to do. 

### Prerequisites - Ansible Master (Mac)

Install `ansible` 

> $ brew install ansible 

Install `sshpass`

> $ brew install http://git.io/sshpass.rb 

Create `hosts`(inventory) in /etc/ansible or designated location (`-i` option).

```
[dev]
192.168.201.75 ansible_user=pi

[prod]
192.168.201.75 ansible_user=pi
```

### Prerequisites - Pi

**NOTE** npm/node-red installation, settings.js copy operation can be managed by ansible-playbook as well. 

Install OS Images

https://www.raspberrypi.org/downloads/raspbian/ Pick **Raspbian Stretch with desktop and recommended software**(`2018-11-13-raspbian-stretch-full.zip` for this example).
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Enable `ssh`

https://www.raspberrypi.org/documentation/remote-access/ssh/

Install `npm` (Palette Manager won't be visible from node-red). Restart node-red after `npm` installation.

```
 $ sudo systemctl stop nodered.service (or node-red-stop)
 $ sudo apt update 
 $ sudo apt install npm
 $ sudo systemctl start nodered.service (or node-red-start)
```

Install `node-red-dashboard` from Palette Manager or CLI.

```
 $ cd $HOME/.node-red
 $ npm install node-red-dashboard 
```

Edit `settings.js`

```
 // The file containing the flows. If not set, it defaults to flows_<hostname>.json
 flowFile: 'flows.json', // uncomment this line
```

###  In Action 

In this example,two playbooks(flow1.yml & flow2.yml) were executed one after another and new flow.json was copied over to Pi each time.

```
$ ansible --version
ansible 2.7.6
$ ansible-playbook -i hosts -k flow1.yml  
SSH password:

PLAY [dev] ***************************************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [192.168.201.75]

TASK [stop node-red] *****************************************************************************
changed: [192.168.201.75]

TASK [install bonjour] ***************************************************************************
ok: [192.168.201.75]

TASK [copy new flows.json] ***********************************************************************
changed: [192.168.201.75]

TASK [start node-red] ****************************************************************************
changed: [192.168.201.75]

PLAY RECAP ***************************************************************************************
192.168.201.75             : ok=5    changed=3    unreachable=0    failed=0

```

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible-node-red-flow-change-text.gif" width="700px"/>
</p>

#### flow1.yml 

```
---
- hosts: dev
  tasks:
     - name: stop node-red
       become: yes  # sudo deprecated
       shell:
             systemctl stop nodered.service
     - name: install bonjour # just show as an example how it can be managed.
       become: yes 
       npm:
           name: bonjour
           path: /usr/lib/node_modules/node-red
           state: latest
     #     registry: https://registry.npmjs.org
     - name: copy new flows.json
       copy:
          src:  flows1.json
          dest: /home/pi/.node-red/flows.json
     - name: start node-red
       become: yes
       shell:
             systemctl start nodered.service
  ```
