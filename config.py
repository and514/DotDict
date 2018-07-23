# coding=utf-8
import os
import yaml

from dot_dict import DotDict


conf = DotDict()


class _Conf(object):

    __loaded = False

    @classmethod
    def get_config(cls, base_dir=None, name_config=None):
        u""" загружаем конфиг один раз

        """
        if cls.__loaded:
            return conf

        # при загрузке базовый каталог и имя конфига должны быть заданы
        assert base_dir is not None
        assert name_config is not None

        with open(os.path.join(base_dir, 'configs', '%s.conf.yml' % name_config), 'r') as f:
            cls.update_conf(conf, yaml.load(f))

        # локальный конфиг (если есть)
        try:
            with open(os.path.join(base_dir, 'configs', '%s.conf.local.yml' % name_config), 'r') as f:
                lc = yaml.load(f)
                cls.update_conf(conf, lc)
        except IOError:
            pass

        cls.__loaded = True
        return conf

    @classmethod
    def update_conf(cls, conf_, data):
        if data is None:
            return
        for key, val in data.items():
            if isinstance(val, dict):
                if conf_[key] is None:
                    conf_[key] = DotDict()
                cls.update_conf(conf_[key], val)
            elif len(key.split('.')) > 1:
                cls.update_conf(conf_[key.split('.')[0]], {'.'.join(key.split('.')[1:]): val})
            else:
                conf_[key] = val


get_config = _Conf.get_config