#!/usr/bin/env python3
from pyvotecore.stv import STV

candidates = ["X", "Y", "Z"]

ballots_marks = [
	[3, 1, 2],
	[3, 1, 2],
	[3, 2, 1]
]

def to_ballot(array):
	a = [x[0] for x in sorted(zip(candidates, array), key=lambda x: x[1])]
	return {"ballot": [x for x in a]}

def to_ballot_list(array):
	a = [x[0] for x in sorted(zip(candidates, array), key=lambda x: x[1])]
	return {"ballot": [[x] for x in a]}

from pyvotecore.schulze_method import SchulzeMethod
from pyvotecore.condorcet import CondorcetHelper
a = SchulzeMethod(list(map(to_ballot_list, ballots_marks)), ballot_notation = CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict()	
print(a)
b = STV(list(map(to_ballot, ballots_marks)), required_winners=2).as_dict()
print(b)
