import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

city1_rain = [12, 15, 20, 25, 60, 120, 200, 180, 140, 80, 30, 15]
city2_rain = [5, 10, 18, 30, 70, 150, 220, 210, 160, 90, 40, 20]
city3_rain = [8, 12, 22, 35, 80, 160, 250, 230, 170, 100, 50, 25]
city4_rain = [10, 14, 19, 28, 65, 140, 210, 195, 150, 85, 35, 18]

fig, ax = plt.subplots()

ax.plot(months, city1_rain, label='City 1')
ax.plot(months, city2_rain, label='City 2')
ax.plot(months, city3_rain, label='City 3')
ax.plot(months, city4_rain, label='City 4')

ax.set_xlabel('Months')
ax.set_ylabel('Rainfall (mm)')
ax.set_title('Monthly Rainfall Comparison for Four Cities')

ax.legend()

plt.show()