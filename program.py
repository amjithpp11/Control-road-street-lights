# Constants for traffic thresholds and light duration
TRAFFIC_THRESHOLD = 10  # number of cars on main road
GREEN_LIGHT_DURATION = 30  # seconds
YELLOW_LIGHT_DURATION = 5  # seconds

# Initialize all street lights to red
main_road_lights = "red"
side_road_lights = "green"

while True:
  # Monitor the traffic at the intersection
  main_road_traffic = get_traffic_on_main_road()

  # If the main road traffic reaches the threshold, switch the lights
  if main_road_traffic >= TRAFFIC_THRESHOLD:
    main_road_lights = "green"
    side_road_lights = "red"
    sleep(GREEN_LIGHT_DURATION)  # wait for the green light duration
    main_road_lights = "yellow"  # switch to yellow
    sleep(YELLOW_LIGHT_DURATION)  # wait for the yellow light duration
    main_road_lights = "red"  # switch to red
    side_road_lights = "green"  # switch the side road lights to green
