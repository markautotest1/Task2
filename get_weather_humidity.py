# -*- coding: utf-8 -*- 
"""
@Author:    mzhang
@File:      get_weather_humidity.py
@Date:      2021/09/25
@Desc:
"""
import requests
import argparse
from datetime import datetime, timedelta
requests.packages.urllib3.disable_warnings()


def get_forecast_humidity(off_days):
	off_days = 0 if off_days < 0 else off_days
	forecast_url = "https://pda.weather.gov.hk/sc/locspc/data/ocf_data/HKO.trim.xml"
	target_date = (datetime.now() + timedelta(off_days)).strftime("%Y%m%d")
	res = requests.get(forecast_url, verify=False)
	if res.status_code == 200:
		hourlyforecast = list(res.json()['HourlyWeatherForecast'])
		humidity_list = [x['ForecastRelativeHumidity'] for x in hourlyforecast if x['ForecastHour'].startswith(target_date)]
		return target_date, humidity_list
	else:
		return f"The humibity of day: [{target_date}] not found, pls re-check!"

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Get Weather Forecast.')
	parser.add_argument('--offdays', type=str, required=True, help='Off Days')

	args = vars(parser.parse_args())

	off_days = int(args["offdays"])
	print(get_forecast_humidity(off_days))
