def zip_checker(zipcode):
    if len(zipcode) == 5:
        if zipcode[:2] != '00':
            print(zipcode)
        else:
            print("Invalid ZIP Code.")
            
    elif len(zipcode) == 4:
        if zipcode[0] != '0':
            zipcode = '0' + zipcode
            print(zipcode)
        else:
            print("Invalid ZIP Code.")
            
            
zip_checker('02806')    # Should return 02806.
zip_checker('2806')      # Should return 02806.
zip_checker('0280')      # Should return 'Invalid ZIP Code.'
zip_checker('00280')     # Should return 'Invalid ZIP Code.'
