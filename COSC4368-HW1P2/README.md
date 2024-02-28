# COSC4368-HW1P2
Write a program which finds solution to the following 3 hierarchically organized9 constraint satisfaction problems, involving 15 variables {A,B,C,…,N,O} which can take integer values in {1,…,100}.

**Problem A**: Find a solution to the constraint satisfaction problem involving the six variables A, B, C, D, E and F and constraints C1,…,C4:
- (C1) A=B+C+E+F
- (C2) D=E+F+21
- (C3) D\*\*2=E\*E\*A + 694
- (C4) E+F<A

**Problem B**: Find a solution to the constraint satisfaction problem involving ten variables A,…,J which satisfy constrains C1,…,C7:
- (C5) H\*J+E\*16=(G+I)\*\*2 -48
- (C6) A-C=(H-F)\*\*2 +4
- (C7) 4\*J=G\*\*2+7

**Problem C**: Find a solution to the constraint satisfaction problem involving 15 variables A,…,O which satisfy constrains C1,..,C13:
- (C8) 2\*M=K\*\*2 -25
- (C0) (N-O)\*\*2 = (J-F)\*O\*2
- (C10) N\*\*2=M\*J+100
- (C11) (L+N)\*\*2+1875=G\*(B+F)\*(K+M+N+30)
- (C12) L\*O=(A\*\*2)\*(K-G)
- (C13) L\*\*3 = M\*\*2- (O\*F\*A)

Your program should contain a counter nva (“number of variable assignments) that counts the number of times an initial integer value is assigned to a variable or the assigned integer to the particular variable is changed; in addition to outputting the solution to the CSV also report the value of this variable at the end of the run, and develop an interface to call your program for CSP Problems A, B, or C. Your program should return a solution or “no solution exists” and the value of nva after the program terminates. Moreover, terminate the search as soon as you found a solution—do not search for additional solutions.

Submit a report which...
- Gives a brief description of the strategy you used to solve the CSP
- Provides Pseudo Code of your CSP solver
- Explains the Pseudo Code in a paragraph or two
- Describes strategies (if you employed any) you employed to reduce the runtime of your program, measured by the final value of the variable nva.
- If you conducted a mathematical pre-analysis to eliminate variables, to obtain additional ‘<’ constraints to reduce search complexity or came up with other problem complexity reduction strategies based on such a pre-analysis, describe the results of the pre-analysis you conducted, and how the results of this pre-analysis were used for reducing the search complexity.
- If your program takes advantage of the hierarchical structure10 of the three CSP problems also explain how this was done.
- If the program you developed is generic in the sense that its code could be reused to solve constraint satisfactions which have a similar structure but different constraints, include a paragraph presenting evidence why your program has this property and what you did to make your program ‘generic’…
