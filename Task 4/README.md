Task 4: SQL Query for Counting Reserved Tickets
Description
In this task, you are given two tables: plays and reservations, which describe theater plays and reservations for these plays in specific theaters. The plays table contains information about the plays, including their id, title, and writer. The reservations table contains reservation details, including id, play_id, number_of_tickets, and theater.

Your task is to write an SQL query that counts the total number of tickets reserved for each play. The resulting table should have three columns: id (the play's ID), title (the play's title), and reserved_tickets (the total number of reserved tickets for the play). The rows should be ordered by decreasing reserved_tickets. In case of a tie, rows should be sorted by increasing id of the play.

Examples
Example 1:
Input:
plays:

id	title	writer
109	Queens and Kings of Madagascar	Nameless. Paul Sat Lee
123	Merlin	Roy Max Rogers Bohring
142	Key of the tea	Note Nul
144	ROMEance Comedy Ashell	
145	Homo	
reservations:

id	play_id	number_of_tickets	theater
12	34	84	Mc Rayleigh
13	109	24	Theater
24	109	45	Theater
37	145	46	Theater
49	145	46	Theater
51	145	3	Theater
68	123	0	Theater
83	142	2	Theater
Output:
id	title	reserved_tickets
145	Homo	170
109	Queens and Kings of Madagascar	46
142	Key of the tea	46
123	Merlin	3
144	ROMEance Comedy Ashell	0
Example 2:
Input:
plays:

id	title	writer
34	The opera of the phantom	
35	The legend of the cake	
36	Stone swords	
43	The Jupiter	
reservations:

id	play_id	number_of_tickets	theater
10	36	13	Theater
30	35	20	Theater
31	36	21	Theater
32	35	23	Theater
33	36		
40	34	29	Assembly Theater
41	34	19	Assembly Theater
42	34		Assembly Theater
19	The Legend	6	Theater
20	The Jupiter		Theater
Output:
id	title	reserved_tickets
34	The opera of the phantom	54
36	Stone swords	53
35	The legend of the cake	43
43	The Jupiter	6
