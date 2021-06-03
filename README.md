# COMP 305 Spring 2021 Project: Lighting Edison's Workplace

## Implemented by:
 * Dilara Deveci
 * Ecre Çınar
 * Michael Bora Sanuk
 * Hazal Mengüaslan

## Short Summary:
  Our task was to find out the maximum number of cells you can illuminate without spending less than the budget.
  We tried to put lamps to the areas that need to be illuminated by deciding which location would result in the maximum area illuminated;
  meaning minimum interaction with walls, far enough from other lamps so that two lamps will not illuminate same area, 
  but not too far so that there small would be unilluminated areas in between the lamps. 
  Then we tried to connect the lamps to each other by finding the closest lamp and connecting those two with cables. 
  
    
## How to Run the Code:
  After the program is run, it asks for an input (either test1, test2, test3, or test4)
  It executes the algorithm on the given test case and writes the results to a txt file 
  The output file is called outtest1.txt if the test1 is run.
      
## Result of the Test Cases:
  * We have implemented two versions.
  * The results for the test cases are provided as a txt file in the relevant the test files.
  * The walls are represented with the character ”#”, cells that can be lighten up are represented with the character ".",
  * Areas that do not need any lighting are represented with "-", the cables are represented with "1", and finally, the illuminated areas are represented with "i" characters.
  * With version 1 (second_app.py)
    * The run times are as follows:
    * Test case 1: 5.1s
    * Test case 2: 13.4s
    * Test case 3: 9.2s
    * Test case 4: 55.9s
  * With version 2 (first_app.py) (the final algorithm)
    * The run times are as follows:
    * Test case 1: 2.5s
    * Test case 2: 9.9s
    * Test case 3: 16.9s
    * Test case 4: Does not terminate

## Summary of the Final Algorithm:
  By using isOptimal function which calls checkWalls function, we first check the area; and decided where to put the lamp; which posiiton would be optimal. Then again in the isOPtimal method, after the optimal position is found we put the lmap by calling the putLamp function and updated the budget.
  The putLamp function changes the cell into "x" and finds the nearest lamp and puts cable between those two by changing the cells into 1's.
  Finally, the isOptimal funciton calls illuminate function in order find out the illuminated area.
  If the budget is still greater than 0, we put random lamps to the empty cells as long as the budget allows.
  
    
