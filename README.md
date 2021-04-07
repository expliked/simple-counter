# simple-counter
a counter program made specifically for use on OBS studio.

an example use of this app is keeping track of deaths in a Halo legendary-difficulty run.

# how to use
when you the the program, it will ask for a text file containing some basic data. here's an example of what to put in that text file:
```
hotkey: F2
text: example text {}
value: 250
```

you can change these values to whatever you want.

`hotkey` must be a valid key on your keyboard. (ex. `a`, `F3`) This is the key you will press to increase your counter.<br>
`text` can be anything. `{}` will be replaced with your value.<br>
`value` must be an integer (number). set it to anything and the program will default that value.
<hr>

When you update your counter, it will also write to that data text file, meaning you can just load the same file over and over again and keep the value between runs.

To decrement the value, press `ctrl+shift+` the hotkey for the counter.

# for issues
if you find an issue, shoot me a DM on discord: `expliked#7824` or just create a github issue and i'll be glad to help.
