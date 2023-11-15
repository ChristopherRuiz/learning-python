def id_validator(verified_ids, feedback_ids):
    unverified = 0
    for fId in feedback_ids:
        if fId not in verified_ids:
            #print(fId + ' was not in' + str(verified_ids))
            unverified += 1
        else:
            continue
            
    print(str(unverified) + ' of ' + str(len(feedback_ids)) + ' IDs unverified.')
    print(str(round((unverified/len(feedback_ids))*100,2)) + '% unverified')
    

v=['1a', '2b', '3c']
f=['1a', '4d']
id_validator(v, f)
