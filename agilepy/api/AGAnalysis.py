"""
 DESCRIPTION
       Agilepy software

 NOTICE
       Any information contained in this software
       is property of the AGILE TEAM and is strictly
       private and confidential.
       Copyright (C) 2005-2020 AGILE Team.
           Addis Antonio <antonio.addis@inaf.it>
           Baroncelli Leonardo <leonardo.baroncelli@inaf.it>
           Bulgarelli Andrea <andrea.bulgarelli@inaf.it>
           Parmiggiani Nicolò <nicolo.parmiggiani@inaf.it>
       All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os

from agilepy.config.AgilepyConfig import AgilepyConfig
from agilepy.config.XMLconfig import SourcesConfig
from agilepy.utils.Utils import AgilepyLogger
from agilepy.utils.ProcessWrapper import ctsMapGenerator

class AGAnalysis:

    def __init__(self, configurationFilePath):

        self.config = AgilepyConfig(configurationFilePath)

        self.logger = AgilepyLogger(self.config.getConf("output","outdir"), self.config.getConf("output","logfilename"), self.config.getConf("output","debuglvl"), init=True)

        self.sourcesconfig = SourcesConfig("./agilepy/testing/demo/sourceconf.xml")

    def setOptions(self, **kwargs):

        rejected = self.config.setOptions(**kwargs)

        if rejected:

            self.logger.warning(self, "Some options have not been set: {}".format(rejected))

    def printOptions(self):

        self.config.printOptions()

    def generateMaps(self):

        if "PFILES" not in os.environ:
            self.logger.critical(self, "Please, set PFILES environment variable.")
            exit(1)

        # check energybin

        # check fovbinnumber

        # for energy
        # for fovbinnumber

        #compute newmape = prefix+mapname self.setOptions(mapname=newmapname)
        #
        ctsMapGenerator.setArguments(self.config)
        ctsMapGenerator.call()
