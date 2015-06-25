# -*- coding: utf-8 -*-

import subprocess
import os
from tamabot.logger import Logger


class TestLogger(object):
    def setup(self):
        cmd = "echo '' > /var/log/tamabot.log"
        p = subprocess.Popen(cmd, shell=True)
        os.waitpid(p.pid, 0)

    def teardown(self):
        self.setup()

    def test_logging(self):
        log_str = "This is test message from TestLogger."
        logger = Logger()
        logger.logger.info(log_str)
        p = subprocess.Popen(["tail", "-n1", "/var/log/tamabot.log"], stdout=subprocess.PIPE)
        logs = p.communicate()
        assert log_str in logs[0]
