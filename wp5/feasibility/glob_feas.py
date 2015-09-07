# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:25:21 2015

@author: BTeillant
"""
from wp5.feasibility.wp1 import wp1_feas
from wp5.feasibility.wp4 import wp4_feas
from wp5.feasibility.wp3 import wp3_feas
# wp3_feas, wp4_feas


def glob_feas(log_phase, log_phase_id, user_inputs, wp2_outputs, wp3_outputs, wp4_outputs):
    if log_phase_id == 100 or 101 or 102:
        feasibility = wp3_feas(install, log_phase_id, wp3_outputs)
    elif log_phase_id == 110 or 111 or 112 or 113 or 114:
        feasibility = wp4_feas(install, log_phase_id, wp2_outputs, wp4_outputs)
    elif log_phase_id == 120 or 121:
        feasibility = wp1_feas(install, log_phase_id, user_inputs)
    return feasibility
