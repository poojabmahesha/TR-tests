#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `treerunner_lib` package."""


import logging
import os
import pytest

from treerunner_lib.treerunner import Treerunner
from common_lib.ssh_connection import SSHClient
from treerunner_lib.conf import config


#@pytest.mark.skip(reason="Needs Hardware to execute")
class TestTreerunner(object):
    log_level = logging.DEBUG
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level)

    ip = config.root.treerunner.ip
    user = config.root.treerunner.username
    password = config.root.treerunner.password
    ssh_client = SSHClient(ip, user, password)
    treerunner = Treerunner(ssh_client, serial_port="COM20")
    process = "sshd"
    log_dir = os.path.dirname(os.path.realpath(__file__))

    # @pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_start_sshd_server(self):
    #     """Test start_sshd_server"""
    #     self.treerunner.start_sshd_server()
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_exec_command_ssh(self):
    #     """Test exec_command_ssh"""
    #     exit_status, stdout, stderr = self.treerunner.\
    #         exec_command_ssh("pidin | grep sshd")
    #     assert exit_status == 0, "ssh command failed: {}".format(stderr)
    #     print("The output is {}".format(stdout.readlines()))
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_is_process_running(self):
    #     """Test is_process_running"""
    #     assert self.treerunner.is_process_running(self.process)
    #
    # @pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_reboot(self):
    #     """Test reboot"""
    #     self.treerunner.reboot()
    #     assert self.treerunner.is_process_running(self.process)

    #@pytest.mark.skip(reason="Needs Hardware to execute")
    def test_collect_slog2info(self):
        """Test collect_slog2info"""
        self.treerunner.collect_slog2info(self.log_dir)
        assert os.path.join(self.log_dir, "treerunner_slog2info.txt")

    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_pidin(self):
    #     """Test collect_pidin"""
    #     self.treerunner.collect_pidin(self.log_dir)
    #     assert os.path.join(self.log_dir, "pidin.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_pidin_ar(self):
    #     """Test collect_pidin_ar"""
    #     self.treerunner.collect_pidin_ar(self.log_dir)
    #     assert os.path.join(self.log_dir, "pidin_ar.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_pidin_syspage(self):
    #     """Test collect_pidin_syspage"""
    #     self.treerunner.collect_pidin_syspage(self.log_dir)
    #     assert os.path.join(self.log_dir, "pidin_syspage.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_top(self):
    #     """Test collect_top"""
    #     self.treerunner.collect_top(self.log_dir)
    #     assert os.path.join(self.log_dir, "top.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_hogs(self):
    #     """Test collect_hogs"""
    #     self.treerunner.collect_hogs(self.log_dir)
    #     assert os.path.join(self.log_dir, "hogs.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_nicinfo(self):
    #     """Test collect_nicinfo"""
    #     self.treerunner.collect_nicinfo(self.log_dir)
    #     assert os.path.join(self.log_dir, "nicinfo.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_tcpdump(self):
    #     """Test collect_tcpdump"""
    #     self.treerunner.collect_tcpdump(self.log_dir)
    #     assert os.path.join(self.log_dir, "tcpdump.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_uname(self):
    #     """Test collect_uname"""
    #     self.treerunner.collect_uname(self.log_dir)
    #     assert os.path.join(self.log_dir, "uname.txt")
    #
    # #@pytest.mark.skip(reason="Needs Hardware to execute")
    # def test_collect_all_logs(self):
    #     """Test collect_all_logs"""
    #     self.treerunner.collect_all_logs(self.log_dir)
    #     assert os.path.join(self.log_dir, "uname.txt")
