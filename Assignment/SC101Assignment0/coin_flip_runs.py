"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""
import random as r


def main():
	print("Let's flip a coin!")
	times = int(input("Number of runs: "))
	success = 0
	out = ""
	con = ""
	while times != success:
		flip = r.randrange(2)
		if flip == 0:
			out += 'T'
		else:
			out += 'H'
		if con == "":
			if flip == 0:
				con = "T1"
			else:
				con = "H1"
		elif con == "T1":
			if flip == 0:
				success += 1
				con = "T2"
			else:
				con = "H1"
		elif con == "H1":
			if flip == 1:
				success += 1
				con = "H2"
			else:
				con = "T1"
		elif con == "T2":
			if flip == 0:
				con = 'T2'
			else:
				con = 'H1'
		elif con == "H2":
			if flip == 1:
				con = 'H2'
			else:
				con = 'T1'
	print(out)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()