# [“Maeve Millay”, “Bernard Lowe”, “Dolores Abernathy”, “Charlotte Hale”].
#  Remove the letter “a” (not “A”) from each element of an array.

names= ['Maeve Millay','Bernard Lowe','Dolores Abernathy','Charlotte Hale']
print([s.strip('a') for s in names]) # remove the a from the string borders
print([s.replace('a', '') for s in names]) # remove all the as 