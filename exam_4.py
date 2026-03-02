#URL
# must start with http:// or https://
# must have something after it
# must contain at least one dot
# must not contain spaces

# startswith() checks the beginning of a string (so if it is nor right -> false)
# we used the rest entered number of characters because http:// has 7 and https:// has 8
# if rest is blank, means no letters, so false
# if no ".", then url is false

def is_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    if url.startswith("http://"):
        rest = url[7:]
    else:
        rest = url[8:]
    if rest == "":
        return False
    if "." not in rest:
        return False
    if " " in url:
        return False

    return True
print(is_url("https://www.economist.com/"))
print(is_url("hattps://www.economist.com/"))
print(is_url("https://wwweconomist)"))
print(is_url("https://wwweconomist. com"))