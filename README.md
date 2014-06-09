cs471
=====

This repository contains the code used in CS471
-----------------------------------------------

                    Summer 2014, Group Project
                       Due June 18th, 2014

You are to simulate a dispatcher using a priority queue system. 

New processes are to be entered using a GUI with priority included
(numbering should be automatic). Processes are also to be terminated
by GUI command. Context switches are to be by command with the cause of the
switch being immaterial. Assume only one CPU.

Priorities and numbers of processes can be kept small, just big enough
to demonstrate the below listed functionality.

Functionality to be provided by you:

1. Priority based Ready Queue(s).

2. Blocked list.

3. Output of complete system status after every context switch showing
   ready, blocked, and running processes.

4. A process status on GUI command (p#, priority and current state).


Details for Requirements
------------------------

1. Priority Scheduling -- Ready queue maintained in priority order, where priority of a process is:
determined by OS (e.g., run system processes before user processes use average time of last CPU bursts, number of open files, memory size (to get memory hogs out as quickly as possible))
purchased by user
based on corporate policy (e.g. give high priority to some project viewed as very important to company)

2. Schedulers
High level schedulers (mostly for batch systems) selects from queue of waiting processes. Often tries to balance job mix (e.g. mix of I/O bound and CPU bound tasks). Often call the job scheduler.
Low level scheduler: selects a process from the ready queue. Often called the dispatcher.
Medium level scheduler: purpose is to improve performance by selecting processes to swap out. Usually means that the memory allocated to them is reallocated to other processes to improve performance. Swapped out processes must later be reinstated.
