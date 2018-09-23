'''
Markov Poetry by Thorne Wolfenbarger
Python3

Primary sript for the Markov Project
Everything should run from this script

USAGE:





'''

import parsePoemDirectory as PoemDir
import generatePoem as genPoem
def main():
	'''
	print("What kind of poem will you be generating?")
	poem_kind = input()
	print("What poem directory will you be using?")
	poem_dir = './Poems/'+input()
	'''
	poem_dir = './Poems/'+'Sonnet'
	'''
	print("What is the theme of the poem to be generated")
	poem_theme = input()
	'''

	concatString = PoemDir.concat_dir_poems(poem_dir)
	freqDict = PoemDir.gen_freq_dict(concatString)
	finishedPoem = genPoem.generate_poem("a",['150'],freqDict)
	print(finishedPoem)








main()