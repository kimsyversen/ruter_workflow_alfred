# encoding: utf-8
import datetime, sys, os
from workflow import Workflow, ICON_WEB, web
from Config import Config

def find_route_id(string, start_pattern, end_pattern):
	start_index = string.find(start_pattern) + len(start_pattern)

	end_index = string.find(end_pattern, start_index)

	return string[start_index:end_index]


if __name__ == u"__main__":
	wf = Workflow()

	c = Config()

	routes = c.get_routes()

	route_name = os.getenv('env_route_name')

	url = os.getenv('env_url')

	start_id = find_route_id(url, "Fra/(", ")")
	stop_id = find_route_id(url, "til/(", ")")

	c.add("routes",route_name,start_id,stop_id)

	c.save()