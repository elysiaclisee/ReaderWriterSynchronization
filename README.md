# Operating Systems Project

This repository contains implementation of a classic synchronization problems in operating systems: **Readers-Writers Problem**  

This problem serves as foundational examples for understanding resource sharing and synchronization in concurrent systems. By exploring its solutions, this project examines the challenges of deadlock prevention, fairness, and efficiency in multi-process environments.

## Table of Contents

- [Project Description](#project-description)
  - [Readers-Writers Problem](#readers-writers-problem-1)
    - [Readers Priority](#readers-preference)
    - [Writers Priority](#writers-preference)
    - [Fair (Mixed) Approach](#fair-mixed-approach)
- [Conclusion](#conclusion)
- [Possible Improvements](#possible-improvements)

## Project Description
The **Readers-Writers Problem** synchronizes access to a shared resource (e.g., a database) between:
- **Readers**, which can access the resource concurrently.
- **Writers**, which require exclusive access.  

This project explores three approaches:
1. **Readers Priority**: Prioritizes readers over writers, allowing multiple readers to access the resource simultaneously.  
2. **Writers Priority**: Gives priority to writers, ensuring they can access the resource without waiting excessively.  
3. **Fair (Mixed) Approach**: Balances access between readers and writers to ensure fairness.

Each approach is analyzed for its advantages, trade-offs, and suitability in different scenarios.


## Implementation Details

#### Readers Priority  
- **Readers** can access the shared resource concurrently.  
- **Writers** must wait until all readers finish accessing the resource.  
- Best for scenarios where reading operations are more frequent than writing.

#### Writers Priority 
- **Writers** get priority, ensuring exclusive access when required.  
- Readers must wait if there are pending writer requests.  
- Suitable for write-intensive applications.

#### Fair (Mixed) Approach  
- Balances access between readers and writers to ensure fairness.  
- No process (reader or writer) experiences indefinite starvation.  
- Ideal for systems with a balanced read/write workload.


## Conclusion

This project provides a detailed exploration of synchronization challenges in operating systems. By implementing solutions to the Readers-Writers Problems, it highlights key concepts like:
- Deadlock prevention techniques.  
- Fair and efficient resource allocation strategies.  
- Trade-offs between simplicity, fairness, and scalability.  

