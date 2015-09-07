# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module governs the definition of the logistic phases. The functions included
are responsible to initialize and characterize the logistic phases both of the 
installation and O&M modules. The functions return a class of each logistic phase
characterized in terms of operations sequence and vessel & equipment combination.

BETA VERSION NOTES: In this version, only two logistic phases were characterized,
one related to Moorings and Foundation Installation: Driven Pile, and another
related to Operation and Maintenance: Offshore Inspection.
"""


class LogPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.op_ve = {}
#        self.feasibility = feasiblity
#        self.matching = matching
#        self.v&e&p_selected = {}
#        self.schedule = {}
#        self.time = {}
#        self.cost = {}
#        self.environmental = environment
#        self.risk = risk


class DefPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.op_sequence = {}
        self.ve_combination = {}
        self.sol = {}


class VE_solutions(object):

    def __init__(self, id):
        self.id = id
        self.sol_ves = {}
        self.sol_eq = {}
        self.schedule = {}
        self.cost = {}


def logPhase_install_init(logOp, vessels, equipments):
    """This function initializes and characterizes all logistic phases associated
    with the installation module. The first step uses LogPhase class to initialize
    each class with a key ID and description, the second step uses the DefPhase
    class to characterize each phase with a set of operation sequences and vessel
    and equipment combinations.
    Explanation of the key ID numbering system implemented:
     1st digit: 1 = Installation;
                9 = O&M
     2nd digit: 0 = Electrical infrastructure;
                1 = Moorings and foundations;
                2 = Wave and Tidal devices;
     3rd digit: component/sub-system type - differ depending on the logistic phase
     4th digit: method (level 1) - differ depending on the logistic phase
     5th digit: sub-method (level 2) - differ depending on the logistic phase

    Parameters
    ----------
    logOp : dict
     dictionnary containing all classes defining the individual logistic operations
    vessels : DataFrame
     Panda table containing the vessel database
    equipments : DataFrame
     Panda table containing the equipment database

    Returns
    -------
    logPhase_install : dict
     dictionnary containing all classes defining the logistic phases for installation
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_install = {'E_export': LogPhase(100, "Installation of static subsea export power cables"),
                        'E_array': LogPhase(101, "Installation of static subsea inter-array power cables"),
                        'E_cp': LogPhase(102, "Installation of offshore electrical collection point"),

                        'F_driven': LogPhase(110, "Installation of driven piles foundations"),
                        'F_suction': LogPhase(111, "Installation of suction caissons for foundation systems"),
                        'F_gravity': LogPhase(112, "Installation of gravity based foundations"),

                        'M_drag': LogPhase(113, "Installation of mooring systems with drag-embedment anchors"),
                        'M_direct': LogPhase(114, "Installation of mooring systems with direct-embedment anchors"),

                        'D_fixed': LogPhase(120, "Installation of bottom fixed devices"),
                        'D_floating': LogPhase(121, "Installation of floating devices")
                        }


    # 2nd Level - Define the diferent operations sequence and corresponding V&E combination for each Phase

    logPhase_install['F_driven'].op_ve[0] = DefPhase(1, 'Drilling')
    logPhase_install['F_driven'].op_ve[1] = DefPhase(2, 'Hammering')
    logPhase_install['F_driven'].op_ve[2] = DefPhase(3, 'Vibro Pilling')

    logPhase_install['F_driven'].op_ve[0].op_sequence = [logOp["op1"],
                                                         logOp["op2"],
                                                         logOp["op3"],
                                                         logOp["op4"],
                                                         logOp["op5"],
                                                         logOp["op_F1"],
                                                         logOp["op_F7"],
                                                         logOp["op6"],
                                                         logOp["op7"],
                                                         logOp["op8"]]

    logPhase_install['F_driven'].op_ve[1].op_sequence = [logOp["op1"],
                                                         logOp["op2"],
                                                         logOp["op3"],
                                                         logOp["op4"],
                                                         logOp["op5"],
                                                         logOp["op_F2"],
                                                         logOp["op_F7"],
                                                         logOp["op6"],
                                                         logOp["op7"],
                                                         logOp["op8"]]

    logPhase_install['F_driven'].op_ve[2].op_sequence = [logOp["op1"],
                                                         logOp["op2"],
                                                         logOp["op3"],
                                                         logOp["op4"],
                                                         logOp["op5"],
                                                         logOp["op_F3"],
                                                         logOp["op_F7"],
                                                         logOp["op6"],
                                                         logOp["op7"],
                                                         logOp["op8"]]

    logPhase_install['F_driven'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    return logPhase_install


def logPhase_OM_init(logOp, vessels, equipments):
    """This function initializes and characterizes all logistic phases associated
    with the O&M module. The first step uses LogPhase class to initialize
    each class with a key ID and description, the second step uses the DefPhase
    class to characterize each phase with a set of operation sequences and vessel
    and equipment combinations.
    Explanation of the key ID numbering system implemented:
     1st digit: 1 = Installation;
                9 = O&M
     2nd digit: 0 = Electrical infrastructure;
                1 = Moorings and foundations;
                2 = Wave and Tidal devices;
     3rd digit: component/sub-system type - differ depending on the logistic phase
     4th digit: method (level 1) - differ depending on the logistic phase
     5th digit: sub-method (level 2) - differ depending on the logistic phase

    Parameters
    ----------
    logOp : dict
     dictionnary containing all classes defining the individual logistic operations
    vessels : DataFrame
     Panda table containing the vessel database
    equipments : DataFrame
     Panda table containing the equipment database

    Returns
    -------
    logPhase_OM : dict
     dictionnary containing all classes defining the logistic phases for O&M
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_OM = {'Om_topside': LogPhase(900, "O&M of top-side elements"),
    'Om_underwater_divers': LogPhase(901, "O&M underwater with divers"),
    'Om_underwater_rov': LogPhase(902, "O&M underwater with rovs"),
    'Om_moorings': LogPhase(903, "O&M of moorings sytems"),
    'Om_electrical': LogPhase(904, "O&M of electrical system"),
    'Rt_ondeck': LogPhase(905, "Retrieval of component by on-deck transportation"),
    'Rt_towing': LogPhase(906, "Retrieval of component by towing transportation"),
    'Rt_mooring': LogPhase(907, "Retrieval of a mooring line"),
    'Rt_umbilical': LogPhase(908, "Retrieval of umbilical cable")
    }


    # 2nd Level - Define the diferent operations sequence and corresponding v&e combination for each Phase

    # PHASES
    logPhase_OM['Om_topside'].op_ve[0] = DefPhase(1, 'Om_topside')
    
    logPhase_OM['Om_underwater_divers'].op_ve[0] = DefPhase(1, 'Om_underwater_divers')
    
    logPhase_OM['Om_underwater_rov'].op_ve[0] = DefPhase(1, 'Underwater')
    logPhase_OM['Om_underwater_rov'].op_ve[1] = DefPhase(2, 'Near_surface')

    
    logPhase_OM['Om_moorings'].op_ve[0] = DefPhase(1, 'Replace_mooring')
    logPhase_OM['Om_moorings'].op_ve[1] = DefPhase(2, 'Maintenance_anchor')
    
    logPhase_OM['Om_electrical'].op_ve[0] = DefPhase(1, 'Om_nonburied')
    logPhase_OM['Om_electrical'].op_ve[1] = DefPhase(2, 'Om_buried')
    
    logPhase_OM['Rt_ondeck'].op_ve[0] = DefPhase(1, 'Rt_surfece')
    logPhase_OM['Rt_ondeck'].op_ve[1] = DefPhase(2, 'Rt_underwater')   
    
    logPhase_OM['Rt_towing'].op_ve[0] = DefPhase(1, 'Rt_surface')
    logPhase_OM['Rt_towing'].op_ve[1] = DefPhase(2, 'Rt_underwater')    
    
    logPhase_OM['Rt_mooring'].op_ve[0] = DefPhase(1, 'Rt_mooring')
        
    logPhase_OM['Rt_umbilical'].op_ve[0] = DefPhase(1, 'Rt_umbilical')
    

    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------                      



    # OPERATIONS
    logPhase_OM['Om_topside'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM1"],
                                                    logOp["op7"],
                                                    logOp["op8"]]

    # COMBINATION
    logPhase_OM['Om_topside'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(0, 0, 0)]
                                                      }

    logPhase_OM['Om_topside'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(0, 0, 0)]
                                                      }
         
    logPhase_OM['Om_topside'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Helicopter'])],
                                                      'equipment': [(0, 0, 0)]
                                                      }                                             
                                                      
     # ---------------------------------------------------------------------------------------                                                     
     # ---------------------------------------------------------------------------------------                      
                                
                                     
                                                      
    # OPERATIONS
    logPhase_OM['Om_underwater_divers'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM2"],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION Added Dive Support Vessel!!!
    logPhase_OM['Om_underwater_divers'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }

    logPhase_OM['Om_underwater_divers'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }
         
    logPhase_OM['Om_underwater_divers'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Dive Support Vessel'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }                                                        
                                                      
    # ---------------------------------------------------------------------------------------       
    # ---------------------------------------------------------------------------------------                      

                                         
                                                      
    # OPERATIONS
    logPhase_OM['Om_underwater_rov'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM3"],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Om_underwater_rov'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(1, equipments['Rov inspection'], 0)]
                                                      }

    logPhase_OM['Om_underwater_rov'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }
         
    logPhase_OM['Om_underwater_rov'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(1, equipments['Rov inspection'], 0)]
                                                      }                                     
                                                      
    logPhase_OM['Om_underwater_rov'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }       
                                                      
     # ---------------------------------------------------------------------------------------                                                     
                                                      
                                                      
    # OPERATIONS
    logPhase_OM['Om_underwater_rov'].op_ve[1].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM4"],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Om_underwater_rov'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }                              
                                                      
    logPhase_OM['Om_underwater_rov'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      } 
                                                      
                                                      
    # ---------------------------------------------------------------------------------------                      
    # ---------------------------------------------------------------------------------------                      
                                
     

    # OPERATIONS
    logPhase_OM['Om_moorings'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM5"],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Om_moorings'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Om_moorings'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  
                                                      
    logPhase_OM['Om_moorings'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }                                                  

    logPhase_OM['Om_moorings'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  


# ---------------------------------------------------------------------------------------                      
                                
     

    # OPERATIONS
    logPhase_OM['Om_moorings'].op_ve[1].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM6],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Om_moorings'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Om_moorings'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  
                                                      
    logPhase_OM['Om_moorings'].op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }                                                  

    logPhase_OM['Om_moorings'].op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  


# ---------------------------------------------------------------------------------------                      
# ---------------------------------------------------------------------------------------                      
                                
     

    # OPERATIONS
    logPhase_OM['Om_electrical'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM7],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION Added Cable Repair Vessel !!!!
    logPhase_OM['Om_electrical'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Cable Repair Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      

# ---------------------------------------------------------------------------------------                      
                                
     

    # OPERATIONS
    logPhase_OM['Om_electrical'].op_ve[1].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_OM8],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION Added Cable Repair Vessel !!!! Added Subsea Excavating Tools !!!!
    logPhase_OM['Om_electrical'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Cable Repair Vessel'])],
                                                      'equipment': [(1, equipments['Rov burial'], 0)]
                                                      }   
                                                      
    logPhase_OM['Om_electrical'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Cable Repair Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)],
                                                      'equipment': [(1, equipments['Subsea Excavating Tools'], 0)]
                                                      }  
                                                      


    # ---------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------                      
                                
     

    # OPERATIONS
    logPhase_OM['Rt_ondeck'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_RT1],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Rt_ondeck'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_ondeck'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_ondeck'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }   

    logPhase_OM['Rt_ondeck'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }                                                         
                         
                             
# ---------------------------------------------------------------------------------------                      
                             

    # OPERATIONS
    logPhase_OM['Rt_ondeck'].op_ve[1].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_RT2],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Rt_ondeck'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_ondeck'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_ondeck'].op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   

    logPhase_OM['Rt_ondeck'].op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  
                                                      

# ---------------------------------------------------------------------------------------                      
# ---------------------------------------------------------------------------------------                      


    # OPERATIONS
    logPhase_OM['Rt_towing'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_RT3],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION 
    logPhase_OM['Rt_towing'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_towing'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_towing'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Anchor Handling'])],
                                                      'equipment': [(1, equipments['Divers'], 0)]
                                                      }   
                                                      

# ---------------------------------------------------------------------------------------                      


    # OPERATIONS
    logPhase_OM['Rt_towing'].op_ve[1].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_RT4],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION Rov workclass or inspection ????!
    logPhase_OM['Rt_towing'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_towing'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_towing'].op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Anchor Handling'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }                                                       

# ---------------------------------------------------------------------------------------                      
# ---------------------------------------------------------------------------------------                      


    # OPERATIONS 
    logPhase_OM['Rt_mooring'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_RT5],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION Equipment ?????????!
    logPhase_OM['Rt_mooring'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_mooring'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_mooring'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   

    logPhase_OM['Rt_mooring'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  



# ---------------------------------------------------------------------------------------                      
# ---------------------------------------------------------------------------------------                      


    # OPERATIONS 
    logPhase_OM['Rt_umbilical'].op_ve[0].op_sequence = [logOp["op1"],
                                                    logOp["op2"],
                                                    logOp["op3"],
                                                    logOp["op4"],
                                                    logOp["op_RT6],
                                                    logOp["op7"],
                                                    logOp["op8"]]
                                                    
    # COMBINATION Equipment ?????????!
    logPhase_OM['Rt_umbilical'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_umbilical'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   
                                                      
    logPhase_OM['Rt_umbilical'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }   

    logPhase_OM['Rt_umbilical'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                      'equipment': [(1, equipments['Rov workclass'], 0)]
                                                      }  
                                                      
                                                      

    return logPhase_OM
