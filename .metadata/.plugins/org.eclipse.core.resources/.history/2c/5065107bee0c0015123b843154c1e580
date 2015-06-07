'''
Iterate all sites and write output from webanalizer to result file
'''
from settings_handler import SettingsHandler
from page_analizer import PageAnalizer
from loggers.system_logger import SystemLogger
from loggers.system_logger import Logger

class AllsitesAnalizer(object):
    
    def __init__(self):
        self.sites = SettingsHandler().instructions
        if self.sites is None:
            self.get_system_logger().report_error("Error during interpret settings")
            return
        for site in self.sites.keys():
            analizer = PageAnalizer()
            for result_file in self.sites[site].keys():
                for (command, result_action) in self.sites[site][result_file]:
                    analize_result = analizer.check(site, command, result_action)
                    # success, site changed in request rule
                    if(analize_result == 0):
                        Logger(site, result_file).report(analizer.result_cmd(result_action))
                    # fail, some error (1 means success but nothing was changed as request rule ask)
                    elif(analize_result != 1):
                        self.get_system_logger().report_error(analize_result)
                 
    def get_system_logger(self):
        if self.__system_logger__ is None:
            self.__system_logger__ = SystemLogger()
        return self.__system_logger__    