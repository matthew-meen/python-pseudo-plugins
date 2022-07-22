import main_app
import plugins
import pandas as pd
import numpy as np
from main_app.plugin_loader import PluginLoader


def main():

    # Some example data to test with
    example_frames = {
        'fixed_nums': pd.DataFrame({'A': [5, 4, 3, 2, 1, 0], 'B': [0, 1, 2, 3, 4, 5], 'C': [2, 4, 1, 5, 0, 3]}),
        'random_nums': pd.DataFrame(np.random.randint(0, 100, size=(10, 3)), columns=list('ABC')),
        'ragged_nums': pd.DataFrame({'A': [5, 4, None, 2, 1, 0], 'B': [0, None, 2, 3, 4, 5], 'C': [2, 4, 1, None, None, None]}),
    }

    # This finds the plugins, but doesn't yet load them into memory
    print("Loading Plugins")
    pl = PluginLoader()
    pl.load_plugins(plugins)

    # Print some information about them
    print("Loaded Plugins:")
    [print(desc) for desc in pl.describe_plugins()]
    print()

    # This loads the plugins to memory
    print("Initializing plugins")
    pl.initialize_loaded_plugins()
    print()

    # This executes the common method in all plugins
    print("Executing plugins")
    results = pl.execute_loaded_plugins(example_frames)
    print()

    # Print the results
    print("Results:")
    [print(res) for res in results]


if __name__ == "__main__":
    main()
