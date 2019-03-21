#!/usr/bin/python
# flow_deploy.py
import sys
#import shutil
import unittest
import base64
import paramiko
import ConfigParser
import argparse
import time

class flowDeployTest(unittest.TestCase):
    targetHost = "127.0.0.1"
    targetUser = "pi"
    targetPass = "pi"
    targetPort = "22" # SSH Port 22
    targetPrompt = "pi> " # PS1="pi> " in .bashrc
    targetFlow = None

    @classmethod
    def setUpClass(self):
        self.child = paramiko.SSHClient()
        self.child.load_system_host_keys()
        self.child.set_missing_host_key_policy(paramiko.WarningPolicy())
        self.child.connect(self.targetHost, username=self.targetUser, password=self.targetPass)

        t = paramiko.Transport(self.targetHost, self.targetPort)
        t.connect(username=self.targetUser, password=self.targetPass)
        self.sftp = paramiko.SFTPClient.from_transport(t)

    @classmethod
    def tearDownClass(self):
        self.child.close()
 
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1_node_red_stop(self):
        stdin, stdout, stderr = self.child.exec_command('sudo systemctl stop nodered.service')
        for line in stdout:
             print('... ' + line.strip('\n'))
        time.sleep(5)

    def test_2_flow_re_deploy(self):
        if self.targetFlow != None:
            self.sftp.put(self.targetFlow, '/home/'+self.targetUser+'/.node-red/'+self.targetFlow)
            time.sleep(5)  
        else :
            self.assertFalse( self.targetFlow == None )

    def test_3_node_red_start(self):
        stdin, stdout, stderr = self.child.exec_command('sudo systemctl start nodered.service')
        for line in stdout:
             print('... ' + line.strip('\n'))
        time.sleep(5)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default='127.0.0.1', help='target hostname')
    parser.add_argument('-u', default='pi', help='ssh username')
    parser.add_argument('-p', default='pi', help='ssh password if asked')
    parser.add_argument('-f', help='new flows.json')
    args = parser.parse_args()

    args_dict = vars(args)

    flowDeployTest.targetHost = args_dict['t']    
    flowDeployTest.targetUser = args_dict['u']
    flowDeployTest.targetPass = args_dict['p']
    if args_dict['f'] != None :
       flowDeployTest.targetFlow = args_dict['f']

    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__] )
    unittest.TextTestRunner(verbosity=3).run(suite)
