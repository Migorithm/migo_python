from types import MappingProxyType

writable = {"one":1, "two":2}
read_only = MappingProxyType(writable)

print(read_only["one"])

try:
    read_only["one"] = 23
except TypeError as t:
    print(t)
    
#Updates to the original are reflected in the proxy
writable["one"] = 42
print(read_only) #{"one":42, "two":2}