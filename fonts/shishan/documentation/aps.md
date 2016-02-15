# Attachment Points in Shishan

 Name | Diacritic Position | Description
------|--------------------|------------
 A    | origin | Attaching above base centrally
 AL   | origin | Attaching above base offset half vowel
 B    | origin | Attaching below base centrally
 BL   | origin | Attaching below base offset half vowel
 C    | | Unused
 F    | origin | Foot height attachment
 MV   | origin/advance | For chaining vowels of A and B forms
 R    | shifted origin | Right or mid height attachment
 S    | shifted origin | Shoulder (or T) height
 SP   | 0, lower stem centre | For attaching U+16F51 before base
 V    | advance | For chaining vowels for foot vowel forms

The positions of these are far from ideal. Many of the origin based APs are awkward to handle on the base character. Here are their positions in relation to the diacritic.


 Name | Diacritic Position | Better Position
------|--------------------|----------------
 A    | origin | centre, 0
 AL   | origin | advance, 0
 B    | origin | centre, 0
 BL   | origin | advance, 0
 C    | | Delete
 F    | origin | origin
 MV   | origin/advance | Merge with V
 R    | shifted origin | 0, centre
 S    | shifted origin | 0, centre
 SP   | as above | advance, bottom
 V    | origin/advance | 0/advance, centre

The R & S points on the base are tricky to calculate at the best of times due needing to know a working bounding rectangle for a vowel to see if one will fit. The maximum height of a base vowel is 729.
