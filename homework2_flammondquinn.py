month_list={ 'January':'1','February':'2','March':'3','April':'4', 'May':'5','June':'6','July':'7','August':'8','September':'9','October':'10','November':'11','December':'12'}

input_file=open('inputDates.txt','r')
output_file=open('parsedDates.txt','w')

for each in input_file:
    if each !='-1':
        word=each.split()
        if len(word) >=3:
            month=word[0]
            day=word[1]
            year=word[2]


            if month.lower() in month_list:
                comma=day[-1]
                if comma==',':
                    day=day[:len(day)-1]
                    month_number=month_list[month.lower()]
                    date=month_number+'/'+day+'/'+year


                    output_file.write(date)
                    output_file.write('\n')


output_file.close()
input_file.close()
