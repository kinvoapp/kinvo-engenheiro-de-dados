from configparser import ConfigParser
import logging, sys, os
import logging.config



class Singleton(type):
    """Classes created from this singleton can only be instantiated once in each code. 
    Even if you try to instantiate again, you will receive the same instance."""


    __instance = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.__instance[cls]


class AppParameterLoadUtil(metaclass=Singleton):
    """Insert resources via configuration file .cfg
    Enable logging in debug mode if there is no config file"""

    __instances = None
    CONFIG_PARAMS = None
    def __new__(cls, *args, **kwds):
        if not AppParameterLoadUtil.__instances:
            AppParameterLoadUtil.__instances = super(AppParameterLoadUtil, cls).__new__(cls, *args, **kwds)
        return AppParameterLoadUtil.__instances

    def __init__(cls):
        cls.__setconfig = {}
        #default logging.basicConfig
        

    def get_dictinary(cls,file_name, section_name=None):
        if not cls.CONFIG_PARAMS:
            cls.CONFIG_PARAMS = {}
            cls._load_config_params(file_name, section_name)
        if section_name:
            return cls.CONFIG_PARAMS[section_name]
        return cls.CONFIG_PARAMS

    def _load_logging_params(cls):
        # logging_config = cls.CONFIG_PARAMS.get('logging_config')
        level = cls._fit_logging_config()
        if not level:
            return
        logging.info(f'Set log level: {level}')
        logging.getLogger().setLevel(eval(level))

    def _load_log_default(cls):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)s %(levelname)s %(message)s'
        )
    def _fit_logging_config(cls):
        logging_config = cls.CONFIG_PARAMS.get('logging_config')
        if not logging_config:
            logging.info(f'logging_config does not exist')
            return None
        level = f'logging.{logging_config["level"]}'
        # format = logging_config['format']
        # format = format.replace('(', '%(').replace('-', ' - ')
        return level

    def _load_config_params(cls, file_name, section_name):
        cls._load_log_default()
        cls._get_section_from_parser(file_name)
        if (section_name is not None) and (not cls.CONFIG_PARAMS.get(section_name, None)):
            cls._show_help()
        cls._load_logging_params()

    def _get_section_from_parser(cls, file_name):
        """Load configures of file in configparse format from home.
        args:
        file: string. 
        section: string.
        option: list.
        """
        try:
            logging.debug("--> load_config")
            sys.path.insert(0, os.path.expanduser("~"))
            parser = ConfigParser()
            parser.read(
                f'{os.path.expanduser("~")}/{file_name}'
            )
            for section_name in parser.sections():
                # if section_name == section_name:
                cls.CONFIG_PARAMS[section_name] = {}
                for options_name, value in parser.items(section_name):
                    cls.CONFIG_PARAMS[section_name][options_name] = value.replace("'","")
            logging.info(f"Config Parms: {cls.CONFIG_PARAMS}")
        except Exception as e:
            logging.error(f'Error: {e}')
            cls._show_help()
        finally:
            logging.debug("<-- load_config")

    def _show_help(cls):
        help_message = """
        Create config_webcrawlear.cfg file in your $HOME environment 
        in the following format for the WebCrawlear application to work:
        """
        format_to_config_webcrawlear = """
        [logging_config]
        level=DEBUG
        [webcrawlear]
        url = https://url.sample.com
        """
        logging.info(
                    f"{help_message} {format_to_config_webcrawlear}"
        )
        sys.exit(1)
        

if __name__ == "__main__":
    appParameterLoadUtil = AppParameterLoadUtil()
    CONFIG_PARAMS = appParameterLoadUtil.get_dictinary(
        file_name='config.cfg', section_name='webcrawlear')
    # logging.info(CONFIG_PARAMS)    
    # logging.debug('dontworkED')
    # logging.info('workED')