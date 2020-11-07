#!/usr/bin/env python3
from pyvotecore.stv import STV

candidates = "ГЧ ДЛ ГС АЛ СБ МЧ ДН ФВ ИШ ОД".split()
#candidates = "Ч Л С л Б ч Н В Ш Д".split()

ballots_data = """
9	7	5	4	1	10	6	3	2	8
1	2	10	8	6	5	3	7	9	4
10	8	4	2	3	9	7	1	5	6
5	1	10	9	7	4	2	3	6	8
2	7	6	4	5	8	1	9	10	3
2	4	9	8	5	1	3	7	6	10
10	8	6	3	2	5	9	1	7	4
6	10	4	1	2	3	7	8	5	9
7	4	2	5	3	6	10	8	1	9
3	2	10	5	8	4	1	6	9	7
10	6	3	2	4	7	9	1	8	5
6	2	5	9	3	4	1	7	10	8
2	3	4	5	7	6	1	8	9	10
8	10	5	4	1	7	9	6	3	2
1	10	8	7	5	1	1	9	4	6
3	10	9	6	5	1	2	7	4	8
9	8	2	4	7	5	10	1	6	3
8	4	10	7	3	6	1	2	5	9
6	9	8	4	3	7	10	1	2	5
4	2	10	3	6	9	1	8	5	7
1	1	7	8	10	1	1	5	6	9
10	2	8	3	1	7	4	9	5	6
3	10	2	6	7	9	5	4	1	8
10	9	8	4	3	5	6	1	2	7
9	4	7	6	2	5	10	1	3	8
8	9	1	7	7	1	10	7	7	1
8	10	1	6	3	5	9	7	4	2
10	2	6	8	1	5	3	9	4	7
8	7	1	6	6	9	10	6	6	1
9	7	2	1	4	8	10	5	3	6
3	2	9	5	7	4	1	6	10	8
4	5	6	7	2	1	3	10	8	9
10	5	4	2	6	8	1	9	7	3
5	10	4	7	2	8	1	9	6	3
2	4	10	7	5	1	3	9	6	8
9	8	3	4	5	10	2	1	6	7
3	2	1	4	5	10	9	8	6	7
2	8	9	10	4	6	1	5	7	3
9	5	2	3	1	8	7	4	10	6
9	4	7	3	1	8	10	5	2	6
6	7	4	10	8	5	3	1	9	2
4	8	5	3	1	10	9	7	6	2
5	1	6	9	8	4	3	7	2	10
7	6	9	3	1	10	5	4	2	8
1	6	10	2	5	7	8	3	4	9
9	3	2	7	1	6	8	10	5	4
6	9	2	5	3	10	4	1	8	7
2	9	8	10	5	4	1	3	7	6
1	7	9	8	2	6	5	4	3	10
"""

def parse(s):
	return int(s) if s else 0

ballots_marks = [list(map(parse, s.split('\t'))) for s in ballots_data.split('\n') if s]
print(ballots_marks)

ballots_marks_temp = [
	[3, 1, 2],
	[3, 1, 2],
	[3, 2, 1]
]

def to_ballot(array):
	a = [x[0] for x in sorted(zip(candidates, array), key=lambda x: -x[1])]
	return {"ballot": [x for x in a]}

def to_ballot_list(array):
	a = [x[0] for x in sorted(zip(candidates, array), key=lambda x: -x[1])]
	return {"ballot": [[x] for x in a]}

from pyvotecore.schulze_method import SchulzeMethod
from pyvotecore.schulze_stv import SchulzeSTV
from pyvotecore.condorcet import CondorcetHelper
#a = SchulzeMethod(list(map(to_ballot_list, ballots_marks)), ballot_notation = CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict()	
#print(a)
#b = STV(list(map(to_ballot, ballots_marks)), required_winners=2).as_dict()
#print(b)
c = SchulzeSTV(list(map(to_ballot_list, ballots_marks)), required_winners=6, ballot_notation=SchulzeSTV.BALLOT_NOTATION_GROUPING).as_dict()
print(c)
d = STV(list(map(to_ballot, ballots_marks)), required_winners=6).as_dict()
print(d)
