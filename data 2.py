import matplotlib.pyplot as plt

# A function to create a pie chart
def create_pie_chart(data, labels):
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.show()

# A function to create a bar chart
def create_bar_chart(data, labels):
    plt.bar(labels, data)
    plt.show()

# A function to create a line chart
def create_line_chart(data, labels):
    plt.plot(labels, data)
    plt.show()

# The main function to get user input and call the chart functions
def main():
    data = []
    labels = []
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        item = input(f"Enter data of item {i+1}: ")
        data.append(int(item))
        label = input(f"Enter label for data item {i+1}: ")
        labels.append(label)
    chart_type = input("Enter chart type (pie, bar, or line): ")
    if chart_type == "pie":
        create_pie_chart(data, labels)
    elif chart_type == "bar":
        create_bar_chart(data, labels)
    elif chart_type == "line":
        create_line_chart(data, labels)
    else:
        print("Invalid chart type")

    # Ask the user if they want to change the chart type
    while True:
        change_chart = input("Do you want to change the chart type? (y/n): ")
        if change_chart == "y":
            new_chart_type = input("Enter new chart type (pie, bar, or line): ")
            if new_chart_type == "pie":
                create_pie_chart(data, labels)
            elif new_chart_type == "bar":
                create_bar_chart(data, labels)
            elif new_chart_type == "line":
                create_line_chart(data, labels)
            else:
                print("Invalid chart type")
        elif change_chart == "n":
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
