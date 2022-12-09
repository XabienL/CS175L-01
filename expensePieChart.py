#Xabien Loor
#Expense Pie Chart Assignment
#CS175L

import matplotlib.pyplot as plt

def main():
    try:
        sales = []
        infile = open('expenses.txt', 'r')
        data = infile.readlines()
        infile.close()
        for index in range(len(data)):
            data[index] = data[index].rstrip('\n')
            cols = data[index].split('\t')
            sales.append(cols)
        slice_labels = []
        sales_data = []
    
        for list in sales:
            if list[1] ==  'abc':
                list[1] = 0.0    
            sales_data.append(list[1])
            slice_labels.append(list[0])
    
    # Create a pie chart from the values.

        plt.pie(sales_data, labels=slice_labels)

    # Add a title.
        plt.title('Monthly Expenses')

    # Display the pie chart.
        plt.show()
    except IOError:
        print('An error occured trying to read the file')

# Call the main function.
if __name__ == '__main__':
    main()
