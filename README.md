# **COMP382-Assignment03**

## **Team Members: Gurveer, Harjot, Inder, Leo, Sahil**

## **Startup Steps**
1. Create a virutal environment - python3 -m venv venv
2. Activate virtual environment - source venv/bin/activate
3. Download the dependencies - pip install -r requirements.txt
4. Run the program - python3 main.py
5. Enter 3SAT 

## **1. Project Description**
This project explores the NP-completeness of SAT through the Cook–Levin framework by taking a 3SAT instance with k=8 clauses, transforming it into an equivalent CLIQUE problem, and then solving the resulting graph problem. The program will construct the graph exactly as described in the reduction: each clause becomes a partite set of literal-vertices, and edges are added only between non-conflicting literals from different clauses. It will then search for an 8-clique, which corresponds to selecting one mutually consistent literal from each clause. If an 8-clique is found, the project will convert that clique back into a satisfying truth assignment for the original 3SAT formula and verify the result by showing that every clause evaluates to true. If no such clique exists, the program will report that there is no solution. Alongside the implementation, the project will also include a short research component highlighting resources on computational complexity, using SAT as the central starting point for understanding NP-complete problems and reductions to other hard problems like CLIQUE.

## **2. What is SAT**

### **2.1 Boolean Review**
- Any variable the can take on values of True & False are called Boolean Variables
- True is represented by 1 | False is represented by 0
- Boolean operations include AND,  OR, and NOT through symbols like ∧, ∨, ¬ respectively
- A Boolean formula is an expression which combines the Boolean variables and operations: (x1 ∨ x2) ∧ ¬x1 | Which essentially reads x1 OR x2 and not x1
- This is satisfiable if we can make the formula evaluate to 1. In this example above you could set x1=0, x2=1 and ¬x1 would therefore be 1 giving you 1 so it is satisfiable

### **2.2 Boolean Satisfiability Problem**
- SAT is a satisfiable Boolean formula like the example shown above
- It is made up variables or literals like x1, x2, etc
- A group of literals forms a clause like (x1 ∨ x2)
- A Boolean formula is in conjunctive normal form or cnf-formula when several clauses are connected with ANDs
- Where a 3SAT is a 3cnf-formula, 3SAT = { ⟨φ⟩ | φ is a satisfiable 3CNF formula }  where essentially all the clauses are going to have three literals like (x1 ∨ x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ x4) ∧ (x2 ∨ ¬x3 ∨ x5) ∧ ...

### **2.3 Our Problem**
- For our instance it is a 3SAT with k=8 so there will be eight clauses in total with each having three literals
- An example input would something like this:
(x1 v x2 v x3) ^ (~x1 v x4 v x5) ^ (x2 v ~x3 v x6) ^ (x1 v x5 v ~x6) ^ (~x2 v x3 v x7) ^ (x4 v ~x5 v x8) ^ (x6 v x7 v ~x8) ^ (~x1 v ~x4 v x8)

## **3. What is a Clique**

### **3.1 Clique**
- A set of vertices (nodes) in a undirected graph where each pair of vertices has an edge connecting them
- If there are 3 nodes: A, B, C | There would be a connecting edge between all so: A-B, B-C, A-C forming a K3

### **3.2 Converting SAT --> Clique**
- For each literal there must be a node
- A k-clique is found by picking a vertex from every clause and choose non-complements
- Two vertices are connected based on two rules:
    1. Vertices are from different clauses
    2. They are not contradictory (x1 and ~x1)

## **4 What is the process of converting back to 3SAT instance**

## **4.1 Converting clique to assignment**
- Once 8-clique is determined, the selected literals are converted into a truth assignment for the original 3SAT problem
- Positive literal = true variable & negative literal = false variable

## **4.2 Solution verification**
- The assignment made is used to evaluate each clause in original 3SAT formula
1. Clause is satisfied when at least one literal is true
2. Program executes statement whether each clause is true or false
3. If all clauses are satisfied, the assignment is valid to be the orignal 3SAT instance solution

## **5. Complexity Difficulty**



## **6. References**
- Patel, P. (2024, September 30). NP-Completeness - Priya Patel - Medium. Medium. https://medium.com/@learning3601/np-completeness-c1de865b2b60<br>
- Sipser, M. (2013). Introduction to the theory of computation. Course Technology Cengage Learning.<br>
- NetworkX Development Team. (2024). NetworkX - Tutorial: Drawing graphs. NetworkX. https://networkx.org/documentation/stable/tutorial.html#drawing-graphs<br>
- jeandoe123. (2019, April 18). 3SAT_Problem. Kaggle. https://www.kaggle.com/code/jeandoe123/3sat-problem<br>
- Kelson. (2021, March 8). Boolean satisfiability problem Checker. Kelson Martins. https://iamkel.dev/sat-problem-checker/<br>



## **Dependencies**
The following python dependencies are needed (pip install):
- networkx
- matplotlib
