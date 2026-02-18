# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib
matplotlib.use('Agg')  # Makes graphs work in Replit automatically
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
#print(lwd.shape)

# Settings, context, and question
print("Setting\n")
print("The story takes place in Egypt from 1990 to 2015 and the population of women in Egypt throughout that time was approximately 29 million in 1990 and approximately 49 million in 2015. Over the years 2000-2010 (the years with the most fluctuation in the scatterplot), there was a terrorist attack, a key presidential election, and a rise in activism and protests.The major political events that occurred in Egypt from 1990 through 2015 led to women's roles in the workforce shifting.\n")

print("---------------------------------------------------------------------------------------\n")

print("Characters\n")
print("Young Egyptian women who entered the workforce in 2000. Single mothers who had to balance caring for their children on top of working a job to support them\n")

print("---------------------------------------------------------------------------------------\n")

print("Context\n")
print("Egypt’s society often placed women in traditional roles, which meant they were to care for children, take care of the house, and not work. Access to childcare and employment opportunities was slim during those times, especially. Women faced discrimination when trying to enter the workforce and were heavily frowned upon for trying to do so.\n")

print("---------------------------------------------------------------------------------------\n")

print("Based on my findings, my proposed research question is:\n")
print("What are the main reasons for the decline of women in the workplace between 1990 and 2015?")

# Creating variables
oneCountryBooleanList = lwd["country_name"]=="Egypt"
oneCountryData = lwd.loc[oneCountryBooleanList]

# Print out the number of rows and columns
#print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(oneCountryData["year"],oneCountryData["WK_working_p"],color="red")

# add a title to the plot
plt.title("Percent of Women Who are Working over Time")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women currently working (%) (%)")

# set the range for the y-axis
plt.ylim(0,40)

# Automatically save and display graph (Replit + GitHub friendly)
plt.tight_layout()
plt.savefig("women_working_scatter.png", dpi=300)
print("\nGraph has been automatically generated and saved as: women_working_scatter.png")
print("Open the file from the Files panel to view the graph.")
plt.close()