# **COMP382-Assignment03**

## **Team Members: Gurveer, Harjot, Inder, Leo, Sahil**

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

### **2.3 3SAT**
- A Boolean formula is in conjunctive normal form or cnf-formula when several clauses are connected with ANDs
- Where a 3SAT is a 3cnf-formula, 3SAT = { ⟨φ⟩ | φ is a satisfiable 3CNF formula }  where essentially all the clauses are going to have three literals like (x1 ∨ x2 ∨ x3) ∧ (¬x1 ∨ x2 ∨ x4) ∧ (x2 ∨ ¬x3 ∨ x5) ∧ ...
- For our instance it is a 3SAT with k=8 so there will be eight clauses in total with each having three literals 




