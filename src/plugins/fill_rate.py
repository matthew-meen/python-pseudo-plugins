from typing import List
from pandas import DataFrame
from main_app.base import BasePlugin
from main_app.plugin_response import PluginResponse


class FillRatePlugin(BasePlugin):
    """
    Example plugin which calculates fill rate for every column in each dataframe.
    Considered an error if the fill rate is < 100%.
    """
    description = "Fill rate calculator."
    version = 0

    def do_work(self, standard_frames: {str, DataFrame}) -> List[PluginResponse]:
        response = []

        for name, df in standard_frames.items():
            for col in df.columns:
                null_count = df[col].isnull().sum()
                fill_rate = round((len(df[col]) - null_count) / len(df[col]) * 100, 2)
                response.append(PluginResponse(f"{col} in {name} has a fill rate of {fill_rate}%",
                                               self.__class__.__name__,
                                               null_count != 0))

        return response
