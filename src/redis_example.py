#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
modify __new__() to make it a singleton
"""
import ConfigParser
import datetime
import time
import redis
import socket


CFG_PATH = '../config/db.ini'
LOG_DIR = '../log/'


class OneInstance(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class RedisInstance(OneInstance):
    def __init__(self, cfg, section):
        self.cfg_info = self.parse_redis_config(cfg, section)
        self.r = redis.Redis(self.cfg_info['host'], self.cfg_info['port'],
                             self.cfg_info['database'])

    def r_instance(self):
        return self.r

    @staticmethod
    def parse_redis_config(cfg_path, entity_name):
        conn_msg = {}
        config_handler = ConfigParser.ConfigParser()
        config_handler.read(cfg_path)
        # Set conn_msg.
        conn_msg['host'] = config_handler.get(entity_name, 'host')
        conn_msg['port'] = config_handler.getint(entity_name, 'port')
        conn_msg['database'] = config_handler.get(entity_name, 'database')
        return conn_msg


class RedisInstance2(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, cfg, section):
        self.cfg_info = self.parse_redis_config(cfg, section)
        self.r = redis.Redis(self.cfg_info['host'], self.cfg_info['port'],
                             self.cfg_info['database'])

    def r_instance(self):
        return self.r

    @staticmethod
    def parse_redis_config(cfg_path, entity_name):
        conn_msg = {}
        config_handler = ConfigParser.ConfigParser()
        config_handler.read(cfg_path)
        # Set conn_msg.
        conn_msg['host'] = config_handler.get(entity_name, 'host')
        conn_msg['port'] = config_handler.getint(entity_name, 'port')
        conn_msg['database'] = config_handler.get(entity_name, 'database')
        return conn_msg


if __name__ == "__main__":
    r1 = RedisInstance(CFG_PATH, "redis:redo")
    r2 = RedisInstance(CFG_PATH, "redis:redo")

    print(id(r1) == id(r2))

    r3 = RedisInstance2(CFG_PATH, "redis:redo")
    r4 = RedisInstance2(CFG_PATH, "redis:redo")

    print(id(r3) == id(r4))