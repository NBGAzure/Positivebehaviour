import argparse
import logging
import logging.handlers
import os
import shutil

try:
    import configparser
except:
    import ConfigParser as configparser
#import six.moves.configparser as configparser

# -----------------------------------------------------------------------------


def get_data(path):
    """Helper to return correct path to our non-python package data files."""
    root = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(root, 'data', path)


def copy_file(filename, dst):
    """Copy data files from data folder."""
    # Create dir if needed
    dir_path = os.path.dirname(os.path.expanduser(dst))
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    src = os.path.join(get_data(''), filename)
    dst = os.path.expanduser(dir_path)
    shutil.copy2(src, dst)

if not os.path.exists(os.path.expanduser('~/.pipfreezer/pipfreezer.cfg')):
    copy_file('pipfreezer.cfg', '~/.pipfreezer/pipfreezer.cfg')

# -----------------------------------------------------------------------------

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='Freezes project requirements.')
parser.add_argument('--config', help='Config file path',
                    default='~/.pipfreezer/pipfreezer.cfg')
# parser.add_argument('-p,', '--password', help='SFTP Password')
parser.add_argument('-s', '--sub', action='store_true', help='Output sub-dependencies to a file')
args = parser.parse_args()

# Read config
config_file = os.path.expanduser(args.config)
config = configparser.ConfigParser()
config.read(config_file)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create logging format
msg_fmt = '[%(levelname)s] [%(asctime)s] [%(name)s] %(message)s'
date_fmt = '%Y-%m-%d %I:%M:%S %p'
formatter = logging.Formatter(msg_fmt, date_fmt)

# Create file handler
logfile = os.path.expanduser('~/.pipfreezer/pipfreezer.log')
if not os.path.exists(os.path.dirname(logfile)):
    os.makedirs(os.path.dirname(logfile))
fh = logging.handlers.RotatingFileHandler(logfile, maxBytes=10485760, backupCount=5)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# Add logging handlers
logger.addHandler(fh)
# logger.addHandler(ch)
