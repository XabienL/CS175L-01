def main():
    # Open the numbers.txt file for reading.
    
    total = 0
    totalLines = 0
    # Read all the lines from the file.
    try:
        numbers_file = open('numbers.txt', 'r')
        for line in numbers_file:
            try:
                amount = float(line)
            except ValueError:
                line = line.strip('\n')
                print('Non-numeric data found in the file:'+line)
        
            else:
                total += amount
                totalLines += 1
                print('I read in', totalLines, 'number(s) Current number is:', amount, 'Total is:', f'{amount:.2f}')
            
            
        average = total / totalLines
        print(f'Average: {average:.2f}')
        
    # Close the file.
        numbers_file.close()  
        
    
    except IOError:
            print('An error occured trying to read the file')
# Call the main function.
if __name__ == '__main__':
    main()
