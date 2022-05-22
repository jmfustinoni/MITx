#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 14:05:36 2022

@author: jmfustinoni
"""

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.
    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.
    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    import numpy as np
    
    data_1 = np.zeros(300)
    data_2 = np.zeros(300)
    for i in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        virusCount, resistVirusCount = [], []
        for j in range(150):
            patient.update()
            virusCount.append(patient.getTotalPop())
            resistVirusCount.append(patient.getResistPop(['guttagonol']))
        patient.addPrescription('guttagonol')
        for k in range(150):
            patient.update()
            virusCount.append(patient.getTotalPop())
            resistVirusCount.append(patient.getResistPop(['guttagonol']))
        data_1 = data_1 + virusCount
        data_2 = data_2 + resistVirusCount
    dataAverage_1 = data_1/numTrials
    dataAverage_2 = data_2/numTrials
    
    pylab.plot(list([float('{0:.1f}'.format(i)) for i in dataAverage_1]), label = r'Non-resistant population')
    pylab.plot(list([float('{0:.1f}'.format(j)) for j in dataAverage_2]), label = r'Guttagonol Resistant population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Average Virus Population')
    pylab.title(r'Virus Simulation in Patient')
    pylab.legend()
    pylab.show()