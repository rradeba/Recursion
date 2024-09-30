BE Module 12 Lesson 6: Assignment | Recursion
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!


Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

Assignment: Recursive Task Scheduler
Objective: The objective of this assignment is to develop a recursive task scheduler that efficiently manages tasks within a nested hierarchy.

Problem Statement: You are tasked with implementing a recursive function to schedule tasks within a hierarchical structure. Each task can have subtasks, forming a nested hierarchy. Your task is to design and implement a recursive task scheduler that traverses through the hierarchy and schedules tasks according to their dependencies and priorities.

Task 1: Design the Task Scheduler Function

Design a Python function named schedule_tasks that takes a single parameter: task_hierarchy. The task_hierarchy parameter represents the nested hierarchy of tasks, where each task is a dictionary with the following keys:

id: Unique identifier for the task.
name: Name or description of the task.
subtasks: List of subtasks (nested hierarchy), if any.
priority: Priority level of the task (optional).
The function should traverse through the task hierarchy recursively and schedule tasks based on their dependencies and priorities.

Task 2: Implement Task Scheduling Logic

Implement the task scheduling logic within the schedule_tasks function. Tasks should be scheduled based on their dependencies and priorities. Tasks with higher priority levels should be scheduled before tasks with lower priority levels. Ensure that subtasks are scheduled after their parent tasks.

Task 3: Test the Task Scheduler Function

Test your schedule_tasks function with various task hierarchies, including nested hierarchies with different priorities and dependencies. Verify that tasks are scheduled correctly according to their dependencies and priorities.

Task 4: Analyze Time and Space Complexity

Analyze the time and space complexity of your schedule_tasks function. Provide insights into the efficiency of the task scheduling algorithm and any potential optimization opportunities.

Expected Outcomes:

Upon completing this assignment, students should be able to:

Design and implement a recursive task scheduler function capable of managing tasks within a nested hierarchy.
Implement task scheduling logic to prioritize tasks based on their dependencies and priorities.
Test the task scheduler function with various task hierarchies to ensure correct scheduling behavior.
Analyze the time and space complexity of the task scheduler algorithm and identify potential optimization opportunities for improved efficiency.
NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

Enter Github Link Here:
