# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module is responsible for the first part of the selection step in the WP5 
methodology. It contains functions to match the requirements computed in the 
feasibility functions, with the parameters of vessels and equipments imported 
in the load functions.

BETA VERSION NOTES: These functions are mature and should not suffer many
changes from the current version to the following beta version.
"""

def select_e (install, log_phase):
    """select_e function selects the equipments that satisfy the minimum 
    requirements calculated in the feasibility functions. The current method to 
    achieve this is erasing the unfeasible equipments from the panda dataframes 
    included in the ve_combination objects.

    Parameters
    ----------
    install : dict
     among other data contains the feasibility requirements of equipments
    log_phase : class
     class of the logistic phase under consideration for assessment, contains 
     data refered to the vessel and equipment combinations specific of
     each operation sequence of the logistic phase

    Returns
    -------
    eq : dict
     A dict of panda dataframes with all the feasibile equipments
    log_phase : class
     An updated version of the log_phase argument containing only the feasible
     equipments within each vessel and equipment combinations dataframes
    """

    req_e = install['requirement'][0]
    #Initialize an empty dic with the name of the equip to be evaluated
    eq = dict.fromkeys(req_e.keys())

    for typ in range(len(req_e)):
        e_key_req = req_e.keys()[typ]

        for seq in range(len(log_phase.op_ve)):
            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                for nr_eq in range(len(log_phase.op_ve[seq].ve_combination[combi]['equipment'])):

                    e_key_phase = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].id
                    e_pd = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda

                    if e_key_phase == e_key_req:

                        for req in range(len(req_e[e_key_req])):
                            e_para = req_e[e_key_req][req][0]
                            e_meth = req_e[e_key_req][req][1]
                            e_val = req_e[e_key_req][req][2]

                            if e_meth == 'sup':
                                e_pd = e_pd[e_pd[e_para] >= e_val]

                        # Check if no vessel is feasible within the req for this particular ve_combination
                        if e_pd.empty:
                            del log_phase.op_ve[seq].ve_combination[combi]   # If so, force the combination to be 0
                            break
                        else:
                            eq[e_key_req] = e_pd
                            log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda = e_pd

    return eq, log_phase


def select_v (install, log_phase):
    """select_v function selects the vessels that satisfy the minimum requirements
    calculated in the feasibility functions. The current method to do this is
    erasing the unfeasible vessels from the panda dataframes included in the
    ve_combination objects

    Parameters
    ----------
    install : dict
     among other data contains the feasibility requirements of vessels
    log_phase : class
     contains data refered to the vessel and equipment combinations specific of
     each operation sequence of the logistic phase

    Returns
    -------
    eq : dict
     A dict of panda dataframes with all the feasibile vessels
    log_phase : class
     An updated version of the log_phase argument containing only the feasible
     vessels within each vessel and equipment combinations dataframes
    """

    req_v = install['requirement'][1]
    #Initialize an empty dic with the name of the vessels to be evaluated
    ves = dict.fromkeys(req_v.keys())

    for typ in range(len(req_v)):
        v_key_req = req_v.keys()[typ]

        for seq in range(len(log_phase.op_ve)):
            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                for nr_ves in range(len(log_phase.op_ve[seq].ve_combination[combi]['vessel'])):

                    v_key_phase = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].id
                    v_pd = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda

                    if v_key_phase == v_key_req:

                       for req in range(len(req_v[v_key_req])):
                           v_para = req_v[v_key_req][req][0]
                           v_meth = req_v[v_key_req][req][1]
                           v_val = req_v[v_key_req][req][2]

                           if v_meth == 'sup':
                               v_pd = v_pd[v_pd[v_para] >= v_val]

                       # Check if no vessel is feasible within the req for this particular ve_combination
                       if v_pd.empty:
                           del log_phase.op_ve[seq].ve_combination[combi]   # If so, force the combination to be 0
                           break
                       else:
                           ves[v_key_req] = v_pd
                           log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda = v_pd

    return ves, log_phase