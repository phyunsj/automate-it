
Revisted [Node-RED flow deployment with Ansible](https://github.com/phyunsj/automate-it/blob/master/README.md). The small scale of nodes can be managed by python alone. See [node_red_flow_deploy.py](https://github.com/phyunsj/automate-it/blob/master/2-flow-deploy-py/node_red_flow_deploy.py). 

#### What is [Pexpect](https://github.com/pexpect/pexpect)?

**Pexpect** is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. Pexpect works like Don Libes’ Expect. Pexpect allows your script to spawn a child application and control it as if a human were typing commands. **Pexpect** can be used for automating interactive applications such as ssh, ftp, passwd, telnet, etc. ..._from [Pexpect Doc](https://pexpect.readthedocs.io/en/stable/)_

#### Installation

```
phyunsj$ pip install pexpect
```

## Console Output

```
phyunsj$ python --version
Python 2.7.15
phyunsj$ python flow_deploy.py -h
usage: flow_deploy.py [-h] [-t T] [-i I] [-u U] [-p P] [-f F]

optional arguments:
  -h, --help  show this help message and exit
  -t T        target hostname
  -i I        inventory file
  -u U        ssh username
  -p P        ssh password if asked
  -f F        new flows.json
phyunsj$ python  flow_deploy.py -t dev -u pi -f flows2.json -p <SSH PASSWORD>
pi@192.168.201.75's password:
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Feb 13 13:53:38 2019 from 192.168.203.243
pi> test_1_node_red_stop (__main__.flowDeployTest) ... sudo systemctl stop nodered.service
pi> ok
test_2_flow_re_deploy (__main__.flowDeployTest) ... pi@192.168.201.75's password: ok
test_3_node_red_start (__main__.flowDeployTest) ... sudo systemctl start nodered.service
pi> ok

----------------------------------------------------------------------
Ran 3 tests in 16.688s

OK
phyunsj$
```

#### See Also

- [pexpect](https://pexpect.readthedocs.io/en/stable/examples.html)
- [argparse](https://docs.python.org/2/howto/argparse.html)
- [ConfigParser](https://docs.python.org/2/library/configparser.html)
- [unittest](https://docs.python.org/2/library/unittest.html)

