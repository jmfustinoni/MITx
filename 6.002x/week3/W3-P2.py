#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 12:16:52 2022

@author: jmfustinoni
"""

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.
    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    import numpy as np
    
    data = np.zeros(300)
    for i in range(numTrials):
        virus = SimpleVirus(maxBirthProb, clearProb)
        viruses = [virus] * numViruses
        patient = Patient(viruses, maxPop)
        count = []
        for j in range(300):
            patient.update()
            count.append(patient.getTotalPop())            
        data = data + count
    dataAverage = data/numTrials
    
    pylab.plot(list(dataAverage), label=r'Average SimpleVirus Population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Virus Population')
    pylab.title(r'Simple Virus Simulation in Patient')
    pylab.legend()
    pylab.show()