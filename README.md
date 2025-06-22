This is a super basic Python script I quickly bodged together for ripping `.vag` files (which can be read by [vgmstream](https://vgmstream.org/)) from The Simpsons Skateboarding's `ASSETS.BLT` file. Decided to share this on the off-chance anyone finds it useful, though note it is very much *not* robust or polished or anything.

## Usage

```
python rip.py "path/to/ASSETS.BLT"
```

## Warning

The music track 'Springfield Mall 3' does not get ripped by this script, and I have no idea why. I'm guessing there's probably some cursed reason like it being stored in a different format from all the other songs, or being compressed, or something like that. But whatever the reason, it *can* be ripped from the `ASSETS.BLT` file in the [E3 Demo](https://hiddenpalace.org/The_Simpsons_Skateboarding_(May_10,_2002_prototype)), which is officially **Good Enough™**.