car={
    'model':'suzuki',
    'year':[2203,2006,2004,],
    'color':('black','red'),
    'docs':{'original':'yes','duplicate':'no',}


}

print(car)
new_docts=dict([('model','suzuli'),('color','black'),('year',[2006,2003])])
print(new_docts)

del new_docts['year']
print(new_docts)



