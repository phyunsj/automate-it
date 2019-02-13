#!/usr/bin/python
# flow_deploy.py
import sys
#import shutil
import unittest
import pexpect
import ConfigParser
import argparse
import time

class flowDeployTest(unittest.TestCase):
    targetHost = "127.0.0.1"
    targetUser = "pi"
    targetPass = "pi"
    targetPort = "1880"
    targetPrompt = "pi> " # PS1="pi> " in .bashrc
    targetFlow = None

    @classmethod
    def setUpClass(self):
        self.child = pexpect.spawn('ssh '+self.targetUser+'@'+self.targetHost)
        self.child.logfile_read = sys.stdout
        self.child.expect('password: ')
        self.child.sendline(self.targetPass)
        self.child.expect(self.targetPrompt)

    @classmethod
    def tearDownClass(self):
        self.child.sendline('exit')
        self.child.close()
 
    def setUp(self):
        # targetUrl & headers for REST service
        self.targetUrl = "http://"+self.targetHost+":"+self.targetPort+"/<service_name>" 
        self.headers = {'content-type' : 'application/json'}

    def tearDown(self):
        pass

    def test_1_node_red_stop(self):
        self.child.sendline('sudo systemctl stop nodered.service')
        self.child.expect(self.targetPrompt)
        time.sleep(5)

    def test_2_flow_re_deploy(self):
        if self.targetFlow != None:
           self.child2 = pexpect.spawn('scp '+self.targetFlow+'  '+self.targetUser+'@'+self.targetHost+':/home/'+self.targetUser+'/.node-red/flows.json')
           self.child2.logfile_read = sys.stdout
           self.child2.expect('password: ')
           self.child2.sendline(self.targetPass)
           self.child2.close()
           time.sleep(5)  
        else :
           self.assertFalse( self.targetFlow == None )


    def test_3_node_red_start(self):
        self.child.sendline('sudo systemctl start nodered.service')
        self.child.expect(self.targetPrompt)
        time.sleep(5)

    #
    #def test_x_flow_rest_test(self):
    #    payload = {}
    #    payload['AAA'] = "BBB" 
    #    r = requests.post(self.targetUrl, data=json.dumps(payload), timeout=10, headers=self.headers)
    #    print r.content
    #    self.assertEqual(200, r.status_code)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default='local', help='target hostname')
    parser.add_argument('-i', default='hosts', help='inventory file')
    parser.add_argument('-u', default='pi', help='ssh username')
    parser.add_argument('-p', default='pi', help='ssh password if asked')
    parser.add_argument('-f', help='new flows.json')
    args = parser.parse_args()

    args_dict = vars(args)
    
    flowDeployTest.targetUser = args_dict['u']
    flowDeployTest.targetPass = args_dict['p']
    if args_dict['f'] != None :
       flowDeployTest.targetFlow = args_dict['f']

    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(args_dict['i'])
    # An array of tuple(s) under '-t' section. 
    # [ ('127.0.0.1 ansible_user', 'pi')] => extract  "127.0.0.1"
    # Of course, if there are more target, you have to add a decision flow to pick the right one.
    # or adjust ansible host file to meet your need
    # The goal is to share ansilble inventory file with ConfigParser module.
    # Which means one-side has to accomodate the differences.
    flowDeployTest.targetHost = config.items(args_dict['t'])[0][0].split(' ')[0]

    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__] )
    unittest.TextTestRunner(verbosity=3).run(suite)


 