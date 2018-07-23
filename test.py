import os

from config import get_config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config = get_config(BASE_DIR, "example")

print('example_bool=', config.example_bool)
print('example_int=', config.example_int)
print('example_list=', config.example_list)
print('example_dict.second_level.one_str=', config.example_dict.second_level.one_str)
print('example_dict.second_level.two_str=', config.example_dict.second_level.two_str)
print('one_void_param (void)=', config.one_void_param)
print('two_void_param (redefined)=', config.two_void_param)
print('three_void_param.sub_param (undefined)=', config.three_void_param.sub_param)
