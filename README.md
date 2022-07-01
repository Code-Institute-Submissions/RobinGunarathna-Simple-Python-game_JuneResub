# Just a simple Hangman game!
A simple game to kill time with!

## Rules And how to play
1. You get 6 failed guesses before you have to try again.
2. When you are done you can press "Y" to play again and "N" to quit.
3. Just press on the letter you want to use.
4. Only letters no numbers.
5. guessing the same letter twice counts as a guess.

## How it should work!

If you select a letter that is in the word the letter you picked saves and the hangman does not animate.
But if you guess the wrong letter it tells you that you selected the wromg letter and the hangman animates 1 out of 6 each failed guess
(guessing same letter twice counts as a failed guess).

## Testing

I've done manual testing to see if everything works correctly.
I tried failing on purpose to see if it tells me that I either put the wrong letter or that I've used that letter allready and I check to see if it animates accordingly.
I tried to Win to See if i does not animate when i guess the correct letters.
I had issues that I wouldn't have noticed without the manual testing for example it could animate when I guessed the correct letter and not animate when guessing the wrong letter but still count as a try. 
All these mistakes/bugs should be fixed.

I have a few Errors according to http://pep8online.com/.
These are the errors:

![image](https://user-images.githubusercontent.com/95103308/176815438-2c9c3a71-6be9-41c0-9f91-aab804bc8a70.png)

I tried "\"(backslash) like it sais in the feedback from the assessor but when i did that i got another error.
I have googled it and tried to fix this in other ways but when i did that there was allways another problem that accurd.
Same for the linter errors if I changed anything the code broke in some way.
Really hope I still pass done everything I can think off.

## Source

only source I had was this Youtube video : https://www.youtube.com/watch?v=m4nEnsavl6w.
The animiation in the constants.py file is taken from this youtube video.
Had to change a lot to meet project criterias.

## Deployment

Was simple to deploy to heroku.
1. Pressed on Create new app and followed the steps.
2. Went to the deploy section immediately because I don't need config vars.
3. Chose Github as deployment method.
4. I searched for your github repository I wanted to connect and pressed on connect.
5. Last step was to press on deploy branch and my game was deployed.

## Adressing assessor feedback
"Version control is not taken into consideration with the use of Git, or large chunks of code were committed together instead of properly separated into more manageable pushes."
I could not get it to work at first so I got 48 hours to get a working deployed link but I only got to use 1 commit to do so. I had no choice I'm sorry. Hopefully its better this time!
