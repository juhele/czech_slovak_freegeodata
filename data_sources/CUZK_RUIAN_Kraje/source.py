from .. source import Source
import os
from qgis.core import QgsVectorLayer, QgsMessageLog

class Kraje(Source):

    def get_vector(self, extent, EPSG):
        url = 'https://geoportal.cuzk.cz/zakazky/SPH/SPH_SHP_JTSK.zip'
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'SPH_SHP_JTSK.zip')
        self.download_data(url, path, "ČUZK Ruian Kraje")
        path = '/vsizip/' + os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'SPH_SHP_JTSK.zip') + '/JTSK/SPH_KRAJ.shp'
        vector = QgsVectorLayer(path, "Kraje", "ogr")
        vector.loadNamedStyle(os.path.dirname(__file__) + '/data/style.qml')
        if not vector.isValid():
            QgsMessageLog.logMessage("Vrstvu " + path + " se nepodařilo načíst", "GeoData")
            return None
        else:
            return vector

    def get_raster(self, extent, EPSG):
        return None