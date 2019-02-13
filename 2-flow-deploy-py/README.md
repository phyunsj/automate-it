

### Console Output - Mac

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
