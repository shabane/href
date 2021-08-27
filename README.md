# hrep

this program will find all the link with a spesfic __Regex__ pattern from a site.




usage:
	`href.py --url URL --pattern RegegPattern`
	
example:
	`href.py --url 'https://example.com/songs/tylor_swift/index.html' --pattern '.*mp3.*'`


> note:
> 
> 1- all the switch have a small way to use,
>
> `--url`: `-u`
>
> `--pattern`: `-p`
>
> 2- use pipe
>
> to use the program some time you need to pipe or redirect the result
>
> some site repeated their link to preview a video or music before download them, so you can pipe the result to `uniq` command for prevent link duplicate.
>
> and for having the link in a text file, you should redirect the result to a file. `href.py -u "URL" -p "patternt" > links.txt`