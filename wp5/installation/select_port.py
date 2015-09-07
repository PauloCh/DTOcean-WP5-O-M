# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module is responsible for the selection of ports for both the installation
and O&M logistic activities. 

BETA VERSION NOTES: This current version is limited to the feasibility functions 
of two logistic phases (one for the installation module and one for the O&M), 
this will be upgraded for the beta version due to october.
"""


def install_port(user_inputs, wp3_outputs, wp4_outputs, port_data):
    """install_port function selects the home port used by all logistic phases
    during installation. This selection is based on a 2 step process: 
        1 - the port feasibility functions from all logistic phases are taken
        into account, and the unfeasible ports are erased from the panda dataframes.  
        2 - the closest port to the project site is choosen from the feasbile
        list of ports.

    Parameters
    ----------
    user_inputs : dict
     dictionnary containing all required inputs to WP5 coming from WP1/end-user
    wp3_outputs : dict
     dictionnary containing all required inputs to WP5 coming from WP3
    wp4_outputs : DataFrame
     panda table containing all required inputs to WP5 coming from WP4
    port_data : DataFrame
     panda table containing the ports database     

    Returns
    -------
    port : dict
     dictionnary containing the results of the port selection
    """    
    # initialisation
    port = {'Terminal Load Bearing [ton/m2]': 0,
            'Terminal area [m2]': 0,
            'Port list satisfying the minimum requirements': 0,
            'Distance port-site': 0,
            'Selected base port for installation': 0}
    # calculate loading and projeted area of foundations/anchors
    load = []
    area = []
    if user_inputs['device']['technology type'].ix[0] == "seabed fixed":
        for x in range(wp4_outputs['quantity'].ix[0]):
            key1 = "diameter foundation " + str(x) + " [m]"
            key2 = "length foundation " + str(x) + " [m]"
            key3 = "weight foundation " + str(x) + " [kg]"
            load[len(load):] = [wp4_outputs[key1].ix[0] * wp4_outputs[key2].ix[0] / wp4_outputs[key3].ix[0]]
            area[len(area):] = [wp4_outputs[key1].ix[0] * wp4_outputs[key2].ix[0]]
    # terminal load bearing minimum requirement
    port['Terminal Load Bearing [ton / m2]'] = max(user_inputs['device']['length [m]'].ix[0] * user_inputs['device']['width [m]'].ix[0] / user_inputs['device']['drymass [kg]'].ix[0],
                                                   max(load))
    port_list = port_data[port_data['Terminal Load Bearing [ton/m2]'] >= port['Terminal Load Bearing [ton/m2]']]
    port['Terminal area [m2]'] = max(user_inputs['device']['length [m]'].ix[0] * user_inputs['device']['width [m]'].ix[0], sum(area))
    port_list = port_list[port_list['Terminal area [m2]'] >= port['Terminal area [m2]']]

    port['Port list satisfying the minimum requirements'] = port_list

    # Distance ports-site calculation
    # to be implemented once the transit distance algorithm is available
    # by making use of the grid coordinate position of the site and the ports

    # Nearest port selection
    # to be modified by making use of port['Distance port-site'] will be
    # implemented

    port['Selected base port for installation'] = port_list.ix[0]

    return port

def OM_port(wp6_outputs, port_data):
    """OM_port function selects the home port used by all logistic phases
    required by the O&M module. This selection is based on a 2 step process: 
        1 - the port feasibility functions from all logistic phases are taken
        into account, and the unfeasible ports are erased from the panda dataframes.  
        2 - the closest port to the project site is choosen from the feasbile
        list of ports.

    Parameters
    ----------
    user_inputs : dict
     dictionnary containing all required inputs to WP5 coming from WP1/end-user
    wp3_outputs : dict
     dictionnary containing all required inputs to WP5 coming from WP3
    wp4_outputs : DataFrame
     panda table containing all required inputs to WP5 coming from WP4
    port_data : DataFrame
     panda table containing the ports database     

    Returns
    -------
    port : dict
     dictionnary containing the results of the port selection
    """       
    # initialisation
    port = {'Terminal Load Bearing [ton/m2]': 0,
            'Terminal area [m2]': 0,
            'Port list satisfying the minimum requirements': 0,
            'Distance port-site': 0,
            'Selected base port for installation': 0}

    # Calculate loading and projeted area of Spare Parts

    # Input collection
    lenght_SP = wp6_outputs['LogPhase1']['Length_SP [m]'].ix[0]
    width_SP = wp6_outputs['LogPhase1']['Width_SP [m]'].ix[0]
    height_SP = wp6_outputs['LogPhase1']['Height_SP [m]'].ix[0]
    total_mass_SP = wp6_outputs['LogPhase1']['Total_Mass_SP [t]'].ix[0]
    indiv_mass_SP = wp6_outputs['LogPhase1']['Indiv_Mass_SP [t]'].ix[0]

    # Feasibility functions
    SP_area = float(lenght_SP) * float(width_SP)
    SP_loading = float(total_mass_SP) / float(SP_area)

    # terminal load bearing minimum requirement
    port_list = port_data[port_data['Terminal area [m2]'] >= SP_area]
    port_list = port_list[port_list['Terminal Load Bearing [ton/m2]'] >= SP_loading]

    port['Port list satisfying the minimum requirements'] = port_list

    # Distance ports-site calculation
    # to be implemented once the transit distance algorithm is available
    # by making use of the grid coordinate position of the site and the ports

    # Nearest port selection
    # to be modified by making use of port['Distance port-site'] will be
    # implemented

    port['Selected base port for installation'] = port_list.ix[0]

    return port
