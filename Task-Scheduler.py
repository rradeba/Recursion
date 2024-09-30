def schedule_tasks(task_hierarchy):
   
    
    scheduled_tasks = []  

    def traverse_tasks(tasks):

        for task in tasks:
            
            
            scheduled_tasks.append(task)  
            
           
            if 'subtasks' in task and task['subtasks']:
                
                traverse_tasks(task['subtasks'])

    
    sorted_tasks = sorted(task_hierarchy, key=lambda x: x.get('priority', 0), reverse=True)
    
    
    traverse_tasks(sorted_tasks)

    return scheduled_tasks  


task_hierarchy = [
    {
        'id': 1,  
        'name': 'Task A',  
        'priority': 2,  
        'subtasks': [  
            {
                'id': 2,
                'name': 'Task A1',
                'priority': 1,
                'subtasks': []  
            }
        ]
    },
    {
        'id': 4,
        'name': 'Task B',
        'priority': 1,
        'subtasks': []  
    },
    {
        'id': 5,
        'name': 'Task C',
        'priority': 3,
        'subtasks': [  
            {
                'id': 6,
                'name': 'Task C1',
                'priority': 2,
                'subtasks': []  
            }
        ]
    }
]

scheduled = schedule_tasks(task_hierarchy)

for task in scheduled:
    print(f"Task ID: {task['id']}, Name: {task['name']}, Priority: {task.get('priority', 'N/A')}")



'''
Time Complexity: sorting the tasks is O(nlogn), traversing heirarchy is O(n)

Space Complexity: sorting the tasks is O(n), traversing the heirarchy is O(m). 

'''







