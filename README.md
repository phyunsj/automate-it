# Automate It

The collection of ideas to improve the productivity.   

## Ansible + Node-RED flow

1. Where to start/Environment Setup

TBD

2. Prerequisites

Insall `ansible` 

> $ brew install ansible // Mac

Install `sshpass`

> $ brew install http://git.io/sshpass.rb // Mac

`npm` is not installed. Manage Palette won't be available(visible). Restart node-red after `npm` installation.

> $ sudo apt update && sudo apt install npm // Pi

Either install `node-red-dashboard' from Palette or CLI.

> $ cd $HOME/.node-red && npm install node-red-dashboard // Pi

3. In Action

> $ ansible-playbook -i hosts -k flow1.yml  // Mac

<p align="center">
<img src="https://github.com/phyunsj/automate-it/blob/master/ansible-node-red/ansible-node-red-flow-change-text.gif" width="650px"/>
</p>
