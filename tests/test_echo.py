#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class EchoTest(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_parser(self):
        args = ['--upper', '--lower', '--title', 'HELLO']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.title)
        self.assertTrue(ns.text)

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        """Running the program with -u argument should return uppercase"""
        args = ['-u', 'hello']
        self.assertEquals(echo.main(args), 'HELLO')

    def test_upper_long(self):
        """Running the program with --upper argument should return uppercase"""
        args = ['--upper', 'hello']
        self.assertEquals(echo.main(args), 'HELLO')

    def test_lower_short(self):
        """Running the program with -l argument should return lowercase"""
        args = ['-l', 'HELLO']
        self.assertEquals(echo.main(args), 'hello')

    def test_lower_long(self):
        """Running the program with --lower argument should return lowercase"""
        args = ['--lower', 'HELLO']
        self.assertEquals(echo.main(args), 'hello')

    def test_title_short(self):
        """Running the program with -t argument should return title case"""
        args = ['-t', 'HELLO']
        self.assertEquals(echo.main(args), 'Hello')

    def test_title_long(self):
        """Running the program with --title argument should return title case"""
        args = ['--title', 'HELLO']
        self.assertEquals(echo.main(args), 'Hello')

    def test_all_args(self):
        """Running echo with -ul or -lu argument should return lowercase. Running with any combination of -u, l and t arguments should return title case. """
        args_duo_1 = ['-ul', 'HEllO']
        self.assertEquals(echo.main(args_duo_1), 'hello')
        args_duo_2 = ['-lu', 'HEllO']
        self.assertEquals(echo.main(args_duo_2), 'hello')
        args_trio_1 = ['-lut', 'HeLlO']
        self.assertEquals(echo.main(args_trio_1), 'Hello')
        args_trio_2 = ['-ltu', 'HeLlO']
        self.assertEquals(echo.main(args_trio_2), 'Hello')
        args_trio_3 = ['-tlu', 'HeLlO']
        self.assertEquals(echo.main(args_trio_3), 'Hello')

    def test_no_args(self):
        """Running the program with no argument should return the unaltered string"""
        args = ['hello']
        self.assertEquals(echo.main(args), 'hello')


if __name__ == '__main__':
    unittest.main()
