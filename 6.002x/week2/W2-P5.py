#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:42:29 2022

@author: jmfustinoni

iRobot is testing out a new robot design. The proposed new robots differ in 
that they change direction randomly after every time step, rather than just 
when they run into walls. You have been asked to design a simulation to 
determine what effect, if any, this change has on room cleaning times.

Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot)
but implements the new movement strategy. RandomWalkRobot should have the same
interface as StandardRobot.

Test out your new class. Perform a single trial with the StandardRobot 
implementation and watch the visualization to make sure it is doing the right 
thing. Once you are satisfied, you can call runSimulation again, passing 
RandomWalkRobot instead of StandardRobot.

"""

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        next_position = self.getRobotPosition().getNewPosition(random.randint(0, 359), self.speed)
        if self.room.isPositionInRoom(next_position) == False:
            self.setRobotDirection(random.randint(0, 359))
        else:
            self.setRobotPosition(next_position)
            self.setRobotDirection(random.randint(0, 359))
            self.room.cleanTileAtPosition(next_position)
