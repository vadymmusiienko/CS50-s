filename <- readline("The CSV file to analize: ")

pitstops <- read.csv(filename)

total_stops <- nrow(pitstops)
shortest <- min(pitstops$time)
longest <- max(pitstops$time)
total_time_all <- sum(pitstops$time)

print(paste("The total number of pit stops:", total_stops))
print(paste("The duration of the shortest pit stop:", shortest))
print(paste("The duration of the longest pit stop:", longest))
print(paste("The total time spent on pit stops during the race, across all racers:", total_time_all))