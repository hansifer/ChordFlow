ChordFlow
=========

Use natively unsupported keyboard shortcut chords in Sublime Text such as ```alt+k+x```, ```alt+alt+y```, or ```alt+alt+k+z```

**Currently for Windows only**

I use this to facilitate a keyboard shortcut scheme for Sublime Text commands that minimizes moving hands away from home keys. ```Alt``` is within easy reach of thumbs on my keyboard, so that's the favored modifier key over ```Ctrl``` or ```Shift``` in my case. I've also selected the ```K``` key to act as an alphanumeric modifier key when used in conjunction with ```Alt```. This allows me to do things like overload a simple shortcut with up to 3 additional related actions.

Eg:

| Chord       | Command                                               |
|:------------|:------------------------------------------------------|
| alt+d       | move the cursor down one line                         |
| alt+k+d     | scroll up one line                                    |
| alt+alt+d   | move the cursor down one line, extending selection    |
| alt+alt+k+d | multi-select down one line                            |


The code currently hardcodes ```K``` as the alphanumeric modifier, but can be easily changed to accommodate alternative needs. See: [Virtual-Key Codes (Windows)](http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731.aspx)


TODO
----

- Adaptations for Mac, Linux.
- Allow specification/overriding of alphanumeric modifiers via ST keymap config. 
- Add support for ```ctrl+ctrl+``` and ```shift+shift+``` chords.
- Distinguish between left and right keys for ```Alt```, ```Ctrl```, and ```Shift``` for additional modifier combinations.
- Allow for specifying "context" per sub-command in ST keymap config.

CAVEATS
-------

- Using ```Alt``` keys as modifiers is problematic in ST if you're also hiding the menu because of a ST quirk that shows the menu on ```Alt+<key>``` combo keydown if ```<key>``` matches a menu accelerator. The desired behavior is for the menu to only show up on ```Alt``` or ```Alt+<key>``` combo *keyup* and only if that keyup is not associated to a bound chord. Workaround: always show ST menu.

- When troubleshooting chords, keep in mind that keyboard ghosting can be an issue.
