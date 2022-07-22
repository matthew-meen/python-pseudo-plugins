from abc import ABC
from pandas import DataFrame
from typing import List
from plugin_response import PluginResponse


class BasePlugin():

    description = "Plugin base class."
    version = 0

    def do_work(self, standard_frames: {str, DataFrame}) -> List[PluginResponse]:
        raise NotImplementedError('Base plugin cannot do_work. Use an implementation.')
