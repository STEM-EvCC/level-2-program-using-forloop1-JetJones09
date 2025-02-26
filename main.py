mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = len(mission_names)
print("\nThe total amount of successful missions were: " , total_missions)

total_success = sum(mission_success)
print("\nThe amount of sucessful missions: " , total_success)

success_rate = (total_success / total_missions) * 100
print("\nThe total sucess rate for the missions completed: " , success_rate , "%")

mission_count = 0

for mission in mission_names:
    mission_count += 1
print(mission_count)

missions_before_2000 = []
for i in range(total_missions):
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

print(f"\n\nTotal number of missions: {total_missions}")
print(f"Number of successful missions: {total_success}")
print(f"Success rate: {success_rate:.2f}%")
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print(f"- {mission}")
