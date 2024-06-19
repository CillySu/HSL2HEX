### Usage
Minimally, the script can be used as follows:


`python hsl2hex.py "FILE PATH/STRING" [options]`


The following can be achieved through passing -h or --help


```
usage: hsl2hex.py [-h] [--print-lines] [--output OUTPUT] file_or_string

Convert HSL colors in CSS to HEX format.


positional arguments:

file_or_string                Path to the CSS file or the CSS string containing HSL

                              colors



options:

-h, --help                    show this help message and exit

--print-lines                 Print variable names along with hex codes

--output OUTPUT, -o OUTPUT    Path to save the output to
```

While tested on CSS, this script will likely function adequately on most files containing HSL in the format hsl(\*, \*, \*). 

Note that the --print-lines argument simply outputs the file contents as they are originally, merely with substituted HSL → HEX. By default, the script will output a newline-separated list of the HEX values in the order provided.


Examples with Associated Output


*./sample.css:*
```css
/* Sample CSS file with HSL colors */
body {
    background-color: hsl(210, 50%, 60%);
}

.header {
    color: hsl(0, 100%, 50%);
    border-color: hsl(120, 75%, 50%);
}

.footer {
    background-color: hsl(240, 100%, 50%);
}

--custom-color: hsl(300, 100%, 25%);
--another-color: hsl(60, 100%, 50%);
```

*Sample Usage*
`python hsl2hex.py ./sample.css --print-lines -o ~/output.css`

*Sample Output*
```css
background-color:  #6598cc;
color:  #ff0000;
border-color:  #1fdf1f;
background-color:  #0000ff;
--custom-color:  #7f007f;
--another-color:  #feff00;
```

*Alternate Sample Usage*

If instead, no --print-lines argument is passed, the sample output is simply:

*Alternate Sample Output*

```
#6598cc
#ff0000
#1fdf1f
#0000ff
#7f007f
#feff00
```
