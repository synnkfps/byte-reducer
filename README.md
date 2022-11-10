# byte reducer
reduces bytes to get "obfuscated" strings

## how it works
gets the hexadecimal bytes of a string, reduces it by 1 (e.g: 5e turns into 4d) and then convert to string again

## limitations
- some strings can be only reduced 4 times, due to reducing logic. (will be fixed soon)
- to reduce more than 1 time you have to run the program more than 1 time
