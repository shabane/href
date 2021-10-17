# href

## this program will find all the link with a spesfic __Regex__ pattern from a site.



### what it will do

in any site there are a lots of url that may you need the file behind them, this program will find all the `<a>` tag, then list the `href` of the tags. you can use __Regex__ to find the special link(s)

all the finded url's have some special charater's, so the __Regex__ pattern will try to match with all finded url, if match, the url will return. if not match, try for next url in the list.

if you do not write any pattern the program will print all link of site, defualt pattern is: `.*`

and the last thing is that the program is __case-insensitive__




### how to use

__usage__:

        --url 'the url of site'

        --pattern 'Regex pattern'

        --load-headers` path header file

        href.py --url 'URL' --pattern 'RegegPattern' --load-headers ./headers

__example__:

        href.py --url 'https://guitarmusic.ir/hayedeh-songs/' --pattern '.*mp3.*'

### example:
![href](https://s4.uupload.ir/files/ezgif.com-gif-maker_6tmk.gif)





### note:

1. __all the switch have a small way to use__
> `--help`: `-h`
>
> `--url`: `-u`
>
> `--pattern`: `-p`
>
> `--load-headers`: `-l`

2. __use pipe__
> to use the program some time you need to pipe or redirect the result
>
> some site repeated their link to preview a video or music before download them, so you can pipe the result to `uniq` command for prevent link duplicate.
>
> and for having the link in a text file, you should redirect the result to a file. `href.py -u "URL" -p "patternt" > links.txt`

3. __run easy__
> to run the program with out cd to the source dir or wite the full path each time, you can _link_ it to your `~/<user>/.local/bin/href`
do it by this command: `ln -s href.py ~/.local/bin/href`
>
> and do not forget to make it __executable__

4. __headers__
> if you got __4xx__ or __5xx__ _http status code_ try to use a __http header__, or use the default header in the directory
> by this switch `--load-header [file]`


