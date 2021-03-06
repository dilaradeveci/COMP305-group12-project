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
  The program can be run through terminal by the command "python3 first_app.py" or "python3 second_app.py" depending on which verison will be run.
  After the program is run, it asks for an input (either test1, test2, test3, or test4)
  It executes the algorithm on the given test case and writes the results to a txt file 
  There are 3 output files; the one with the cables and the lamps is called outtest1.txt if the test1 is run, the one with the illuminated area which is in .txt format is called illuminationtest1.txt and finally, the visualized one in .png format is called test1.png.
      
## Result of the Test Cases:
  * We have implemented two versions.
  * The results for the test cases are provided in the relevant test file in both .txt and .png format.
  * With version 1 (second_app.py)
    * The illuminated areas and number of lamps put are as follows:
    * Test case 1:  
      * Area: 18152
      * Lamps: 277
    * Test case 2:  
      * Area: 42694
      * Lamps: 179
    * Test case 3: 
      * Area: 137299
      * Lamps: 822
    * Test case 4: 
      * Area: 272443
      * Lamps: 12005
  * With version 2 (first_app.py)
    * The illuminated areas and number of lamps put are as follows:
    * Test case 1:  
      * Area: 12258
      * Lamps: 48
    * Test case 2:  
      * Area: 30875
      * Lamps: 106
    * Test case 3:  
      * Area: 118853
      * Lamps: 868
    * Test case 4: Does not terminate
  * The walls are represented with the character ”#”, cells that can be lighten up are represented with the character ".",
  * The electric source which cables should be connected to is represeted with "E"
  * Areas that do not need any lighting are represented with "-", the cables are represented with "1", and finally, the illuminated areas are represented with "i" characters.
  * With version 1 (second_app.py)
    * The run times are as follows:
    * Test case 1: 5.1s
    * Test case 2: 13.4s
    * Test case 3: 9.2s
    * Test case 4: 55.9s
  * With version 2 (first_app.py)
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
  
    
