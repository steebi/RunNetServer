import configparser
from django.core.management.utils import get_random_secret_key
import argparse
import os


def create_new_secret_key(configuration):
	key = get_random_secret_key()
	configuration['Keys'] = {'SECRET_KEY': key}


def retrieve_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-file", "-f", type=str, required=True)
	return parser.parse_args()


if __name__ == "__main__":
	# retrieve the arguments
	arguments = retrieve_arguments()
	if not os.path.exists(arguments.file):
		raise Exception(f'The path {arguments.file} does not exist! Ensure you are targeting the correct directory.')

	# use the raw config parser to avoid issues with attempted string interpolation
	config = configparser.RawConfigParser()
	create_new_secret_key(config)
	
	# save to file
	with open(arguments.file, 'w') as configFile:
		config.write(configFile)
		print(f"Wrote config file to: {arguments.file}")
