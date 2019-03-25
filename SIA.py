import random
import math
import itertools
import numpy as np
import time
import sys

from multiprocessing import Process, Queue

def generate_random_coordinates():
	return [random.uniform(0,1), random.uniform(0,1)]
	
def get_distance(p1, p2):
	return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

NUM_POINTS = 8	

def generate_case():
	MIN = 0
	MAX = 1

	index = []

	currentNodePositions = []
	requiredFuturePositions = []

	for i in range(NUM_POINTS):
		currentNodePositions.append(generate_random_coordinates())
		requiredFuturePositions.append(generate_random_coordinates())
		index.append(i)
		
	distances = np.zeros([NUM_POINTS,NUM_POINTS])

	for i in range(NUM_POINTS):
		for j in range(NUM_POINTS):
			distances[i][j] = get_distance(currentNodePositions[i], requiredFuturePositions[j])

	combinations = itertools.permutations(index,NUM_POINTS)
	minDistance = MAX * NUM_POINTS
	minCombo = 0
	minComboIndex = 0
	curComboIndex = 0
	
	for combo in combinations:
		totalDistance = 0
		for x in range(NUM_POINTS):
			totalDistance += distances[x,combo[x]]
			if totalDistance > minDistance:
				totalDistance = MAX * NUM_POINTS
				break
		if totalDistance < minDistance:
			minDistance = totalDistance
			minCombo = combo
			minComboIndex = curComboIndex
		curComboIndex += 1

	input = []
	output = minComboIndex
	input = currentNodePositions + requiredFuturePositions
	
	return input,output,minCombo
	

import csv
	
TEST_CASES = int(sys.argv[2])

startTime = time.time()
with open(str(sys.argv[1]) + '.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	header = []
	for j in range(NUM_POINTS):
		header.append("CN" + str(j))
	for j in range(NUM_POINTS):
		header.append("RFP" + str(j))
	header.append("minComboIndex")
	header.append("minCombo")
	#writer.writerow(header)
	for c in range(TEST_CASES):
		row = []
		print ("test case: " + str(c), end='\r')
		input, output, minCombo = generate_case()
		row = input
		row.append(output)
		row.append(minCombo)
		writer.writerow(row)
	worktime = time.time() - startTime
	print("\nDone!")
	print("It took " + str(worktime) +" to complete " + str(TEST_CASES) + " cases")

