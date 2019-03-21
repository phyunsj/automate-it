
Revisted [Node-RED flow deployment with Ansible](https://github.com/phyunsj/automate-it/blob/master/README.md). The small scale of nodes can be managed by python alone. 

See [node_red_flow_deploy.py](https://github.com/phyunsj/automate-it/blob/master/2-flow-deploy-py/node_red_flow_deploy.py). 

## What is [Pexpect](https://github.com/pexpect/pexpect)?

**Pexpect** is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. Pexpect works like Don Libes’ Expect. Pexpect allows your script to spawn a child application and control it as if a human were typing commands. **Pexpect** can be used for automating interactive applications such as ssh, ftp, passwd, telnet, etc. ..._from [Pexpect Doc](https://pexpect.readthedocs.io/en/stable/)_

#### Installation

```
phyunsj$ pip install pexpect
```

#### Flow (Re)deployment 

Use `unittest` framework to control the flow of tasks. Flow-specific testcase(s) can be added if desired.

```
    @classmethod
    def setUpClass(self):
        self.child = pexpect.spawn('ssh '+self.targetUser+'@'+self.targetHost)        
        ...

    def test_1_node_red_stop(self):
        self.child.sendline('sudo systemctl stop nodered.service')
        ...
        
    def test_2_flow_re_deploy(self):
        # spawn scp
        ...
        
    def test_3_node_red_start(self):
        self.child.sendline('sudo systemctl start nodered.service')
        ...
```

#### Console Output

```
phyunsj$ python --version
Python 2.7.15
phyunsj$ python node_red_flow_deploy.py -h
usage: node_red_flow_deploy.py [-h] [-t T] [-i I] [-u U] [-p P] [-f F]

optional arguments:
  -h, --help  show this help message and exit
  -t T        target hostname
  -i I        inventory file
  -u U        ssh username
  -p P        ssh password if asked
  -f F        new flows.json
```

log what the child sends back 

> self.child.logfile_read = sys.stdout

```
phyunsj$ python  node_red_flow_deploy.py -t dev -u pi -f flows2.json -p <SSH PASSWORD>
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

## [Pexpect](https://github.com/pexpect/pexpect) Alternative : [Paramiko](https://github.com/paramiko/paramiko)

> pip install paramiko

See [node_red_flow_deploy_w_paramiko.py](https://github.com/phyunsj/automate-it/blob/master/2-flow-deploy-py/node_red_flow_deploy_w_paramiko.py).

#### Console Output

```
phyunsj$ python ./flow_deploy_wiht_paramiko.py -t <IP ADDRESS> -u pi -p <SSH PASSWORD> -f flows-1234.json
/usr/local/lib/python2.7/site-packages/paramiko/ecdsakey.py:164: CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
 ...
/usr/local/lib/python2.7/site-packages/paramiko/client.py:822: UserWarning: Unknown ssh-ed25519 host key for 192.168.201.74: d6a9e1efd449831010b1c15ad6a9c07d
  key.get_name(), hostname, hexlify(key.get_fingerprint())
test_1_node_red_stop (__main__.flowDeployTest) ... ok
test_2_flow_re_deploy (__main__.flowDeployTest) ... ok
test_3_node_red_start (__main__.flowDeployTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 17.269s

OK
phyunsj$
```

#### See Also

- [pexpect](https://pexpect.readthedocs.io/en/stable/examples.html)
- [Paramiko](https://github.com/paramiko/paramiko)
- [argparse](https://docs.python.org/2/howto/argparse.html)
- [ConfigParser](https://docs.python.org/2/library/configparser.html)
- [unittest](https://docs.python.org/2/library/unittest.html)

