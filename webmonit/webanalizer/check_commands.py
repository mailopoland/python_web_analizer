'''
Created on 7 cze 2015

@author: user
'''
import hashlib

class CheckCommands(object):

    def __init__(self, prev_ver, cur_ver):
        self.prev_ver = prev_ver
        self.cur_ver = cur_ver
        
    def site_changed(self):
        result = hashlib.md5(self.cur_ver) == hashlib.md5(self.prev_ver)
        return result