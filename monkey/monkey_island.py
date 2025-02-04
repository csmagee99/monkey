from gevent import monkey as gevent_monkey

from monkey_island.cc.arg_parser import parse_cli_args

gevent_monkey.patch_all()

import json  # noqa: E402
import os  # noqa: E402

from monkey_island import config_loader  # noqa: E402
from monkey_island.cc.server_utils.island_logger import setup_logging  # noqa: E402

if "__main__" == __name__:
    island_args = parse_cli_args()

    # This is here in order to catch EVERYTHING, some functions are being called on
    # imports, so the log init needs to be first.
    try:
        server_config_path = os.path.expanduser(island_args.server_config)

        config = config_loader.load_server_config_from_file(server_config_path)

        setup_logging(config["data_dir"], config["log_level"])

    except OSError as ex:
        print(f"Error opening server config file: {ex}")
        exit(1)

    except json.JSONDecodeError as ex:
        print(f"Error loading server config: {ex}")
        exit(1)

    from monkey_island.cc.main import main  # noqa: E402

    main(config["data_dir"], island_args.setup_only, island_args.server_config)
