#!/usr/bin/env python
import Queue, sys
""" 
  MovingAverage.py
  Author: Ariel Anders

  Moving Average creates a queue of length num_samples (defaults to 100).
  A sample is assumed to be a float.  

  self.que is initialized to 0 or values from init_vals.
  self.avg is actually the sum of the queue

  The two (usual) functions for Moving Average:

  put_sample(sample)
    this function removes the oldest element from the queue and inserts sample
  get_average(sample)
    this function computes the average of the queue (sum of queue)/num_sample

  The third function combines the two previous functions:

  get_new_average(sample)
    this function removes the oldest element, inserts sample, and returns
    the average of the modified queue

"""
__author__ = "Ariel Anders"
__copyright__ ="Copyright (C) 2013 Ariel Anders"
__license__ = "The MIT License (MIT)"


class MovingAverage:
  def __init__(self, num_samples=100, init_vals = None):
    self.que = Queue.Queue(num_samples)
    self.num_samples = float(num_samples)
    
    # initialize que and average
    if init_vals is not None: 
      # initialize que to init_vals
      if len(init_vals) is not num_samples:
        print "Error: length of init_vals != num_samples"
        sys.exit(2)
        
      for val in init_vals:
        self.que.put(val)
      self.avg = sum(init_vals)

    else:
      #initialize que to zero
      for i in range(num_samples):
        self.que.put(0.0)
      self.avg = 0.0

  def get_new_average(self,sample):
    last_sample = self.que.get()
    self.que.put(sample)
    self.avg = self.avg + sample - last_sample
    return self.avg / self.num_samples
  
  def get_average(self):
    return self.avg / self.num_samples
  
  def put_sample(self,sample):
    last_sample = self.que.get()
    self.que.put(sample)
    self.avg = self.avg + sample - last_sample

if __name__=="__main__":
  # Example main method shows how to use all function in 
  # MovingAverage.py
  example_q = MovingAverage(10)
  print "default initialized que average: %f" %(example_q.get_average())
  
  print "putting in samples %s " %(range(10))
  for i in range(10):
    print "adding %d to queue, new average: %f"\
        %(i, example_q.get_new_average(i))

  print "putting in samples %s " %(range(9,0,-1))
  for i in range(9, 0, -1):
    print "adding %d to queue, new average: %f"\
        %(i, example_q.get_new_average(i))

  print "putting in 10 samples of 0"
  for i in range(10):
    example_q.put_sample(0)
  print "new average is %f" % example_q.get_average()

  print "Making a queue with initial values %s" %range(10)
  example_init_q = MovingAverage(10, range(10))
  print "average of this new queue is %f" % example_init_q.get_average()
