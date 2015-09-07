# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module imports the WP5 databases required to run WP5 package.  All data
imported is translated to panda dataframes.

BETA VERSION NOTES: the module also aims to provide a buffer between the database
source and WP5 package, so it becomes simple to shift from the temporary .xlsx
and .csv files to the final SQL solution.
"""

import pandas as pd

from ..logistics import VesselType
from ..logistics import EquipmentType

def load_vessel_data(file_path):
    """Imports vessel database into panda dataframe and creates a class for each
    vessel type

    Parameters
    ----------
    file_path : string
     the folder path of the vessel database

    Returns
    -------
    vessels : dict
     dictionnary containing all classes defining the different vessel types
    """
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    pd_vessel = excel.parse('Python_Format', header=0, index_col=0)
    # Splits the pd_vessel object with the full dataset, into smaller panda
    # objects with specific vessel types. Each vessel object is initiated with
    # the vessel class: VesselType
    vessels = {'Tugboat': VesselType("Tugboat", pd_vessel[pd_vessel['Vessel type'] == 'Tugboat']),
               'Crane Barge': VesselType("Crane Barge", pd_vessel[pd_vessel['Vessel type'] == 'Crane Barge']),
               'Crane Vessel': VesselType("Crane Vessel", pd_vessel[pd_vessel['Vessel type'] == 'Crane Vessel']),
               'JUP Barge': VesselType("JUP Barge", pd_vessel[pd_vessel['Vessel type'] == 'JUP Barge']),
               'JUP Vessel': VesselType("JUP Vessel", pd_vessel[pd_vessel['Vessel type'] == 'JUP Vessel']),
               'Anchor Handling': VesselType("AHTS", pd_vessel[pd_vessel['Vessel type'] == 'AHTS']),
               'Multicat': VesselType("Multicat", pd_vessel[pd_vessel['Vessel type'] == 'Multicat']),
               'CLV': VesselType("CLV", pd_vessel[pd_vessel['Vessel type'] == 'CLV']),
               'CLB': VesselType("CLB", pd_vessel[pd_vessel['Vessel type'] == 'CLB']),
               'CTV': VesselType("CTV", pd_vessel[pd_vessel['Vessel type'] == 'CTV']),
               'Dive Support Vessel': VesselType("Dive Support Vessel", pd_vessel[pd_vessel['Vessel type'] == 'Dive Support Vessel']),
               'Cable Repair Vessel': VesselType("Cable Repair Vessel", pd_vessel[pd_vessel['Vessel type'] == 'Cable Repair Vessel'])
               }

    return vessels


def load_equipment_data(file_path):
    """Imports equipment database into panda dataframes and creates a class for
    each equipment type

    Parameters
    ----------
    file_path : string
     the folder path of the equipment database

    Returns
    -------
    vessels : dict
     dictionnary containing all classes defining the different equipment types
    """

    # Transform Equipment database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    hammer = excel.parse('hammer', header=0, index_col=0)
    drillingRig = excel.parse('drill rig', header=0, index_col=0)
    # Define equipment types by invoking EquipmentType class
    equipments = {'Hammer': EquipmentType("Hammer", hammer),
                  'Drill Rig': EquipmentType("Drill Rig", drillingRig)
                  }

    return equipments


def load_port_data(file_path):
    """Imports port database into a panda table

    Parameters
    ----------
    file_path : string
     the folder path of the port database

    Returns
    -------
    vessels : dict
     dictionnary containing a panda dataframe with all ports
    """
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    ports = excel.parse('python', header=0, index_col=0)

    return ports
