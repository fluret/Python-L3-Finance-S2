from follow_instructions import follow

assert follow("fflff") == (-1, 4)
assert follow("ffrff") == (1, 4)
assert follow("fblr") == (0, 0)
print("All tests passed!")