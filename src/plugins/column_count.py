from typing import List
from pandas import DataFrame
from main_app.base import BasePlugin
from main_app.plugin_response import PluginResponse


class ColumnCountPlugin(BasePlugin):
    """
    Example plugin which counts the number of columns in each dataframe.
    """
    description = "Column counter."
    version = 0

    def do_work(self, standard_frames: {str, DataFrame}) -> List[PluginResponse]:
        response = []

        for name, df in standard_frames.items():
            response.append(PluginResponse(f"{name} is {len(df.columns)} columns wide",
                                           self.__class__.__name__, False))

        return response
