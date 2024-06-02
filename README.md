# xfce-thunar-numblems
XFCE Thunar File manager Custom Action for number emblems

![2](https://github.com/behnamgolds/xfce-thunar-numblems/assets/29102609/b7fa3279-d2b2-4b56-9b90-d80f080537aa)

I just wanted to add some actions to my thunar custom actions ,
so that I could mark some files/directories with a number and
easily increase or decrease the number .

This was intended to be used as thunar custom action, but it
could be used on its own like this :

```
$ python numblems.py <file-or-directory-path> <inc|dec>
```
or
```
$ ./numblems.py <file-or-directory-path> <inc|dec>
```
But you have to refresh(F5) your thunar window manually.
If used as thunar custom action it will automatically send
the F5 key to the active window(aka thunar)

You could also use it in other scripts and just run something
like the following to send F5 to the active window :
```
$ xdotool key F5
```

I used some svg emblems and put it into my icons directory here :
```
~/.icons/Papirus-Dark/symbolic/emblems/
```
There are 19 [1..19] svgs since that is what I needed .
The script will clear the emblem if the number goes out of range .
I included them in the emblems/ directory in this repo .
Also the source is mentioned there in emblems/source.txt .
"Papirus-Dark" is the name of the theme I use, you should change
it to your theme name and make a symbolic link to this directory
in your "your-theme-name" directory if you want this emblems be
visible in other themes .

then run this to read the new emblems :
```
$ thunar -q
```

My numblems script is located here :
```
~/bin/non-interactive/
```
Adding the action to thunar is straightforward from :
```
Thunar > Edit > Configure Custom Actions
```
![1](https://github.com/behnamgolds/xfce-thunar-numblems/assets/29102609/d28dbfb5-1e21-4536-b536-24476e55b2d3)

The changes will be saved here :
```
~/.config/Thunar/uca.xml
```
The changes related to numblems for my config will be saved like this :
```
</actions>
<action>
	<icon>list-add</icon>
	<name>Inc Num</name>
	<submenu>Emblem</submenu>
	<unique-id>1717335346720586-1</unique-id>
	<command>/home/behnam/bin/non-interactive/numblems.py %f inc</command>
	<description>Increase Number Emblem</description>
	<range>*</range>
	<patterns>*</patterns>
	<directories/>
	<audio-files/>
	<image-files/>
	<other-files/>
	<text-files/>
	<video-files/>
</action>
<action>
	<icon>list-remove</icon>
	<name>Dec Num</name>
	<submenu>Emblem</submenu>
	<unique-id>1717335485659165-2</unique-id>
	<command>/home/behnam/bin/non-interactive/numblems.py %f dec</command>
	<description>Decrease Number Emblem</description>
	<range>*</range>
	<patterns>*</patterns>
	<directories/>
	<audio-files/>
	<image-files/>
	<other-files/>
	<text-files/>
	<video-files/>
</action>
</actions>
```



