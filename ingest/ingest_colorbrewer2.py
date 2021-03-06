""" Ingests the CET (Centre for Exploration Targeting) color maps into the data directory.
"""
import json
import logging
import os.path

import numpy as np

from cmlib.cmap import DataCategory, CmMetaData, CatalogMetaData
from cmlib.misc import LOG_FMT, save_rgb_floats

logger = logging.getLogger(__name__)

SOURCE_DIR = "../source_data/ColorBrewer2"
TARGET_DIR = "../cmlib/data/ColorBrewer2"

STR2CAT = {
    'seq' : DataCategory.Sequential,
    'div' : DataCategory.Diverging,
    'qual' : DataCategory.Qualitative
}

# MAPS = [
#     # Linear
#     ('CET-L1',  'linear_grey_0-100_c0_n256', DataCategory.Sequential),
#     ('CET-L2',  'linear_grey_10-95_c0_n256', DataCategory.Sequential),
#     ('CET-L3',  'linear_kryw_0-100_c71_n256', DataCategory.Sequential),
#     ('CET-L4',  'linear_kry_0-97_c73_n256', DataCategory.Sequential),
#     ('CET-L5',  'linear_kgy_5-95_c69_n256', DataCategory.Sequential),
#     ('CET-L6',  'linear_kbc_5-95_c73_n256', DataCategory.Sequential),
#     ('CET-L7',  'linear_bmw_5-95_c86_n256', DataCategory.Sequential),
#     ('CET-L8',  'linear_bmy_10-95_c71_n256', DataCategory.Sequential),
#     ('CET-L9',  'linear_bgyw_20-98_c66_n256', DataCategory.Sequential),
#     ('CET-L10', 'linear_gow_60-85_c27_n256', DataCategory.Sequential),
#     ('CET-L11', 'linear_gow_65-90_c35_n256', DataCategory.Sequential),
#     ('CET-L12', 'linear_blue_95-50_c20_n256', DataCategory.Sequential),
#     ('CET-L13', 'linear_ternary-red_0-50_c52_n256', DataCategory.Sequential),
#     ('CET-L14', 'linear_ternary-green_0-46_c42_n256', DataCategory.Sequential),
#     ('CET-L15', 'linear_ternary-blue_0-44_c57_n256', DataCategory.Sequential),
#     ('CET-L16', 'linear_kbgyw_5-98_c62_n256', DataCategory.Sequential),
#     ('CET-L17', 'linear_worb_100-25_c53_n256', DataCategory.Sequential),
#     ('CET-L18', 'linear_wyor_100-45_c55_n256', DataCategory.Sequential),
#     ('CET-L19', 'linear_wcmr_100-45_c42_n256', DataCategory.Sequential),
#
#     # Diverging
#     ('CET-D1',  'diverging_bwr_40-95_c42_n256', DataCategory.Diverging),
#     ('CET-D1A', 'diverging_bwr_20-95_c54_n256', DataCategory.Diverging),
#     ('CET-D2',  'diverging_gwv_55-95_c39_n256', DataCategory.Diverging),
#     ('CET-D3',  'diverging_gwr_55-95_c38_n256', DataCategory.Diverging),
#     ('CET-D4',  'diverging_bkr_55-10_c35_n256', DataCategory.Diverging),
#     ('CET-D6',  'diverging_bky_60-10_c30_n256', DataCategory.Diverging),
#     ('CET-D7',  'diverging-linear_bjy_30-90_c45_n256', DataCategory.Diverging),
#     ('CET-D8',  'diverging-linear_bjr_30-55_c53_n256', DataCategory.Diverging),
#     ('CET-D9',  'diverging_bwr_55-98_c37_n256', DataCategory.Diverging),
#     ('CET-D10', 'diverging_cwm_80-100_c22_n256', DataCategory.Diverging),
#     ('CET-D13', 'diverging_bwg_20-95_c41_n256', DataCategory.Diverging),
#     ('CET-R3',  'diverging-rainbow_bgymr_45-85_c67_n256', DataCategory.Diverging),
#
#     # Rainbow
#     ('CET-R1',  'rainbow_bgyrm_35-85_c69_n256', DataCategory.Sequential),
#     ('CET-R2',  'rainbow_bgyr_35-85_c72_n256',  DataCategory.Sequential),
#
#     # Cyclic
#     ('CET-C1',  'cyclic_mrybm_35-75_c68_n256', DataCategory.Cyclic),
#     ('CET-C2',  'cyclic_mygbm_30-95_c78_n256', DataCategory.Cyclic),
#     ('CET-C4',  'cyclic_wrwbw_40-90_c42_n256', DataCategory.Cyclic),
#     ('CET-C5',  'cyclic_grey_15-85_c0_n256',   DataCategory.Cyclic),
#
#     # Isoluminant
#     ('CET-I1',  'isoluminant_cgo_70_c39_n256', DataCategory.Sequential),
#     ('CET-I2',  'isoluminant_cgo_80_c38_n256', DataCategory.Sequential),
#     ('CET-I3',  'isoluminant_cm_70_c39_n256',  DataCategory.Sequential),
#     ('CET-D11', 'diverging-isoluminant_cjo_70_c25_n256', DataCategory.Diverging),
#     ('CET-D12', 'diverging-isoluminant_cjm_75_c23_n256', DataCategory.Diverging),
#
#     # Color blind friendly
#     ('CET-CBL1',  'linear-protanopic-deuteranopic_kbjyw_5-95_c25_n256', DataCategory.Sequential),
#     ('CET-CBL2',  'linear-protanopic-deuteranopic_kbw_5-98_c40_n256', DataCategory.Sequential),
#     ('CET-CBD1',  'diverging-protanopic-deuteranopic_bwy_60-95_c32_n256', DataCategory.Diverging),
#     ('CET-CBC1',  'cyclic-protanopic-deuteranopic_bwyk_16-96_c31_n256', DataCategory.Cyclic),
#     ('CET-CBC2',  'cyclic-protanopic-deuteranopic_wywb_55-96_c33_n256', DataCategory.Cyclic),
#     ('CET-CBTl1', 'linear-tritanopic_krjcw_5-98_c46_n256', DataCategory.Sequential),
#     ('CET-CBTl2', 'linear-tritanopic_krjcw_5-95_c24_n256', DataCategory.Sequential),
#     ('CET-CBTD1', 'diverging-tritanopic_cwr_75-98_c20_n256', DataCategory.Diverging),
#     ('CET-CBTC1', 'cyclic-tritanopic_cwrk_40-100_c20_n256', DataCategory.Cyclic),
#     ('CET-CBTC2', 'cyclic-tritanopic_wrwc_70-100_c20_n256', DataCategory.Cyclic),
# ]

def parseRgbString(rgbString):
    """ Parses string in the form 'rgb(x,y,z)' where x, y and z are integers.
        
        Returns (x, y, z) tuple.
    """
    return [int(s) for s in rgbString[4:-1].split(',', 3)]

def parseRbgValues(rgbStrings):

    allStrings = [parseRgbString(s) for s in rgbStrings]

    data = np.array(allStrings) / 256
    return data






def ingest_files():

    # From http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer_updates.html
    smd = CatalogMetaData()
    smd.key = "ColorBrewer"
    smd.name = "Color Brewer 2"
    smd.version = "2.0"
    smd.date = "2019-07-18" # Download date
    smd.author = "Cynthia A. Brewer"
    smd.url = "https://colorbrewer2.org/"
    smd.doi = ""
    smd.license = "Apache License, Version 2.0"

    smd.save_to_json_file(os.path.join(TARGET_DIR, CatalogMetaData.DEFAULT_FILE_NAME))

    source_file_name = os.path.join(SOURCE_DIR, 'colorbrewer.json')
    logger.info("Opening: {}".format(source_file_name))
    with open(source_file_name, 'r') as fp:
        source_json = json.load(fp)

    for cm_base_name, cm_dict in sorted(source_json.items()):

        catStr = cm_dict['type']
        logger.debug("Processsing: {} ({})".format(cm_base_name, catStr))

        category = STR2CAT[catStr]

        for key in sorted(cm_dict.keys()):

            if key == 'type':
                continue

            # Parse input
            numColors = int(key)
            rbgStrings = cm_dict[key]
            cm_name = "{}-{:02}".format(cm_base_name, numColors)
            assert len(rbgStrings) == numColors, "size mismatch: for {}".format(cm_base_name)
            array = parseRbgValues(rbgStrings)

            # Write metadata
            target_file = cm_name + '.csv'
            target_path = os.path.join(TARGET_DIR, target_file)
            logger.debug("Writing data to: {}".format(target_path))
            save_rgb_floats(target_path, array)

            md = CmMetaData(cm_name)
            md.file_name = target_file
            md.category = category
            md.notes = ''
            md.recommended = True
            md.perceptually_uniform = False

            md.black_white_friendly = False
            md.isoluminant = False
            md.color_blind_friendly = False

            md.save_to_json_file(os.path.join(TARGET_DIR, "{}.json".format(cm_name)))



if __name__ == "__main__":
    logging.basicConfig(level='DEBUG', format=LOG_FMT)
    ingest_files()

