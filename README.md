# Automate It

The collection of ideas(or short examples) to improve the productivity.   

## Node-RED flow deployment with Ansible

#### About Ansible

Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates. ..._from [Ansible Document](https://docs.ansible.com/ansible/latest/index.html)_

Ansible manages machines in an **agent-less manner**. No installation is required on the remote machines. 

#### Prerequisites

[Mac] Install `ansible` 

> $ brew install ansible 

[Mac] Install `sshpass`

> $ brew install http://git.io/sshpass.rb 

[Mac] Create `hosts`(inventory) in /etc/ansible or a local file (with `-i` option).

```
[dev]
111.222.333.444 ansible_user=pi

[prod]
555.666.777.888 ansible_user=pi
```


[Pi] `npm` is not installed yet. `Manage Palette` won't be available(visible). Restart node-red after `npm` installation.

> $ sudo apt update && sudo apt install npm 

[Pi] Install `node-red-dashboard` from Palette Manager or CLI. (It can be installed from ansible as well)

> $ cd $HOME/.node-red && npm install node-red-dashboard 

[Pi] Edit `settings.js` to uncomment `flows.json`

####  In Action [Mac]

In this example,two playbooks(flow1.yml & flow2.yml) were executed one after another and new flow.json was copied over to Pi each time.

> $ ansible-playbook -i hosts -k flow1.yml  

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible-node-red-flow-change-text.gif" width="700px"/>
</p>
