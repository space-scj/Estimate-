-v.02

##############~/ UPDATED FEATURES \~################
        Rooms now selectable, and drawing is now toglable based on the draw button.  Selected items will now highlight as a light gray to visually show what is selected. v.02

        Rooms can now be deleted when selected by pressing d

        Build mode can be toggled by pressing b

        
        
        $$$$~/ Features to come \~$$$$
#Work out collision detection on rooms.

#Test line item functionality with list items pulled from SQLite3.

///----#Figure out how to implement canvas.delete to reflect and record removal of individual room shapes.----\\\

#Amend room objects to be collections of walls, and implement logic to detect if they're contained loops so that the rooms can be modified

#Clean up UI and bar functions

#Add a width tag to room, to reflect the linear feet.

#Add a function that calculates sqft of walls, floor, and ceiling.



    \ (^) /
  ___\{*}/___          ****************BUGS*****************
     /{|}\
    /  |  \

/\Resolve bug where selecting a room has to be done in the order that rooms are created.  
/\Resolve bug with teleporting rooms when attempted to update the position by dragging.
/\Resolve bug when trying to update the length tag text.