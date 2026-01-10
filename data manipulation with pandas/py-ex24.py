# Modify histogram transparency to 0.5 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()