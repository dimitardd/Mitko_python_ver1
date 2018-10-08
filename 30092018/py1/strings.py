myname = "teodor kolev"

print(myname.capitalize())
print(myname.title())
print(myname.upper())
print(myname.lower())

Str='this is string example....wow!!!!'
suffix='!!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix,20))
suffix='exam'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))

str = "this is string example....wow!!!";
print(str.startswith( 'this' ))
print(str.startswith( 'is', 2, 4 ))
print(str.startswith( 'this', 0, 4 ))