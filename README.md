# Automate It

The collection of ideas to improve the productivity.   

## Ansible + Node-RED flow

1. Where to start/Environment Setup

TBD

2. Prerequisites

'npm' is not installed. Manage Palette won't be available. Restart node-red after npm installation

> sudo apt update && sudo apt install npm

Either install `node-red-dashboard' from Palette or CLI.

> npm install node-red-dashboard

3. In Action

> $ ansible-playbook -i hosts -k flow1.yml

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible-node-red-flow-change-text.gif" width="650px"/>
</p>
