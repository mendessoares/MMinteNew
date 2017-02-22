#! /usr/bin/env python

import argparse
from tempfile import gettempdir
from os.path import join
from spyre import server
import cherrypy

import sys
sys.path.extend(['/Users/m097749/Source/MMinte'])

from mminte.site import Index
from mminte.site import Widget1
from mminte.site import Widget2
from mminte.site import Widget3
from mminte.site import Widget4
from mminte.site import Widget5
from mminte.site import Widget6
from mminte.site import Widget7
from mminte.site import WidgetRunAll


if __name__ == '__main__':
    # Parse command line arguments.
    parser = argparse.ArgumentParser(prog='launchMMinte')
    parser.add_argument('--port', help='port number of MMinte site', action='store', default=None)
    parser.add_argument('--log-folder', help='path to folder for storing log files', action='store',
                        dest='log_folder', default=gettempdir())
    args = parser.parse_args()

    # Set the cherrypy configuration.
    cherrypy.config.update({
        "response.timeout": 1000000,
        'log.access_file': join(args.log_folder, 'logAccess_file.txt'),
        'log.error_file': join(args.log_folder, 'logError_file.txt'),
        'log.screen': True
    })

    # Create the MMinte website.
    site = server.Site(Index)
    site.addApp(Widget1, '/app1')
    site.addApp(Widget2, '/app2')
    site.addApp(Widget3, '/app3')
    site.addApp(Widget4, '/app4')
    site.addApp(Widget5, '/app5')
    site.addApp(Widget6, '/app6')
    site.addApp(Widget7, '/app7')
    site.addApp(WidgetRunAll, '/app8')
    site.root.templateVars['app_bar'] = [
        ('/', 'Intro'),
        ('/app1', 'Widget1'),
        ('/app2', 'Widget2'),
        ('/app3', 'Widget3'),
        ('/app4', 'Widget4'),
        ('/app5', 'Widget5'),
        ('/app6', 'Widget6'),
        ('/app7', 'Widget7'),
        ('/app8', 'WidgetRunAll')]
    for fullRoute, _ in site.site_app_bar[1:]:
        parent, route = site.get_route(fullRoute)

    # Launch the website (which runs until explicitly ended).
    site.launch()
