
create schema bikes;

CREATE OR REPLACE TABLE project_data.bikes.rides(
    rideable_type varchar(15),
    started_at DATETIME,
    ended_at DATETIME,
    start_station_id varchar(10),
    end_station_id varchar(10),
    member_casual varchar(10)
);

CREATE OR REPLACE TABLE project_data.bikes.loading_log (
   loading_date DATETIME,
   total_rides_loaded int,
   total_stations int,
   loading_duration int
);


CREATE OR REPLACE TABLE project_data.bikes.stations (
    station_id varchar(10) ,
    station_name varchar(200),
    latitude FLOAT,
    longitude FLOAT,
    seasonal_status varchar(200),
    municipality varchar(200),
    total_docks  int
);