
# get weather data from NWS with Longitude and latitude



library(tidyverse)
library(httr2)


get_weather_data <- function() {
  # Get forecast URL from NWS
  NWS_base_url <- 'https://api.weather.gov'
  NWS_response <- request(NWS_base_url) |> 
    req_url_path_append(
      'points',
      '38.8894,-77.0352'
    ) |> 
    req_perform()
  
  # Extract forecast URL
  forecast_url <- NWS_response |> 
    resp_body_json() |> 
    pluck('properties', 'forecastHourly')
  
  # Get actual forecast data
  forecast_response <- request(forecast_url) |> 
    req_perform()
  
  # Bring data into tibble format
  extracted_data <- forecast_response |> 
    resp_body_json() |> 
    pluck('properties', 'periods') |> 
    map_dfr( # iterates over each list and binds rows to a tibble
      \(x) {
        tibble(
          time = x |> pluck('startTime'),
          temp_F = x |> pluck('temperature'),
          rain_prob = x |> pluck('probabilityOfPrecipitation', 'value'),
          forecast = x |> pluck('shortForecast')
        )
      }
    )
  jsonlite::toJSON(extracted_data, pretty = TRUE)
}



get_weather_data_x_y <- function(x,y) {
  # Get forecast URL from NWS
  NWS_base_url <- 'https://api.weather.gov'
  NWS_response <- request(NWS_base_url) |> 
    req_url_path_append(
      'points',
      paste0(x,',',y)
    ) |> 
    req_perform()
  
  # Extract forecast URL
  forecast_url <- NWS_response |> 
    resp_body_json() |> 
    pluck('properties', 'forecastHourly')
  
  # Get actual forecast data
  forecast_response <- request(forecast_url) |> 
    req_perform()
  
  # Bring data into tibble format
  extracted_data <- forecast_response |> 
    resp_body_json() |> 
    pluck('properties', 'periods') |> 
    map_dfr( # iterates over each list and binds rows to a tibble
      \(x) {
        tibble(
          time = x |> pluck('startTime'),
          temp_F = x |> pluck('temperature'),
          rain_prob = x |> pluck('probabilityOfPrecipitation', 'value'),
          forecast = x |> pluck('shortForecast')
        )
      }
    )
  jsonlite::toJSON(extracted_data, pretty = TRUE)
}



#(34.0522,-118.2436) # Los Angeles
#(40.7128,-74.0060) # New York
#(41.8781,-87.6298) # Chicago
#(29.7604,-95.3698) # Houston
#(33.4484,-112.0740) # Phoenix
#(39.7392,-104.9903) # Denver
#(47.6062,-122.3321) # Seattle
#(37.7749,-122.4194) # San Francisco
#(32.7157,-117.1611) # San Diego
#(42.3601,-71.0589) # Boston
#(22.5429, 114.0596) # Shenzhen



get_weather_data() 

#  New York
get_weather_data_x_y(40.7128,-74.0060)




