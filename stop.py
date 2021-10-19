import os

import pysc


if __name__ == '__main__':
    service_name = 'testing'
    #pysc.stop(service_name)
    pysc.delete(service_name)
