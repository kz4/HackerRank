Jim Bone, the Husky Dog secret agent, has finished his secret mission in the Kat Kingdom capital, and now has to return to the Dog District. However, the Kitties Guarding Boarders know that Jim Bone is in their country, and are attempting to stop him by spreading his picture to the kitty police at their train stations.

You must help Jim Bone escape the kitty capital by determining which trains he should take to leave the country. However, because the police are actively looking for him, Jim has decided that he cannot sit still at any one train station for too long. Thus you need to determine which trains he should take so that his layover is never too long.

Details of traveling 
At the very start, Jim is at station 1, at time 0. Suppose that Jim arrives at station xx at time tt. Then he can move to station yy if and only if:

There is a train going from xx to yy at time t1t1, where t1≥tt1≥t, but t1−t≤Tt1−t≤T, the max time he can spend at the station.

If there is such a train ride, labeled as x, y, t1, t2x, y, t1, t2, then after taking this train, he will be at station yy at time t2t2.

Input Format

Line 1: NN MM TT. 
10≤N≤20000010≤N≤200000 
50≤M≤50000050≤M≤500000 
1≤T≤1001≤T≤100

NN is the max label of any train station (1 is the starting point, NN is the destination outside the country). Jim Bone always starts at station 1 at time 0.
MM is the number of train rides which appear on the schedule.

TT is the max time Jim can spend at any one station without being caught by the Kitties Guarding Borders. Note that he is allowed to spend exactly TT time steps at a station, but not a moment more.

Next MM Lines: xx yy t1t1 t2t2. 
1≤x,y≤N1≤x,y≤N 
0≤t1≤t2≤50000000≤t1≤t2≤5000000 
* xx is the station label where a train will be leaving from

yy is the station label where this train will arrive

t1t1 is the time the train will leave station xx.

t2t2 is the time the train will arrive at station yy.

Output Format

"NO" if, no matter what trains Jim takes, he will not be able to reach station N without being caught.

"YES TminTmin" if he can escape , where TminTmin is the time that he arrives at station NN. If there are multiple such paths, you should find the one with smallest possible TminTmin.

Sample Input

4 5 20 
1 2 15 20 
1 3 1 6 
2 4 25 30 
3 4 2 7 
3 4 30 35

Sample Output

YES 30

Explanation

Jim could take the following trains: 
* Station 1 to station 2, leaves at 15, arrives at 20 
* Station 2 to station 4, leaves at 25, arrives at 30

The only other train that arrives earlier at station 4 leaves station 3 at time 2, but it is not possible to get to station 3 before time 2.
