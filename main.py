import argparse
import requests
from bs4 import BeautifulSoup
import json
import re
from win11toast import toast
import time


def get_json_format_data():
    url = 'https://huggingfaceh4-open-llm-leaderboard.hf.space/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    script_elements = soup.find_all('script')
    json_format_data = json.loads(str(script_elements[1])[31:-10])
    return json_format_data


def get_datas(which_one, data):
    data_components_map = {
        'pending': {'component_index': 28, 'pattern': r'<a[^>]*>(.*?)</a>', "zero_or_one": 0},
        'running': {'component_index': 25, 'pattern': r'<a[^>]*>(.*?)</a>', "zero_or_one": 0},
        'finished': {'component_index': 11, 'pattern': r'href="([^"]*)"', "zero_or_one": 1}
    }

    data_component_info = data_components_map[which_one.lower()]
    if not data_component_info:
        raise ValueError("Invalid option. Choose 'pending', 'running', or 'finished'.")

    component_index = data_component_info['component_index']
    pattern = data_component_info['pattern']
    zero_or_one = data_component_info['zero_or_one']

    result_list = []
    i = 0
    while True:
        try:
            unfiltered = data['components'][component_index]['props']['value']['data'][i][zero_or_one].rstrip("\n")
            normal_name = re.search(pattern, unfiltered).group(1)
            normal_name = "/".join(normal_name.split("/")[-2:]) if which_one == "finished" else normal_name
            # link = "https://huggingface.co/" + normal_name

            result_list.append(normal_name)
            i += 1
        except (IndexError, AttributeError):
            return result_list


def notifi(section, model_name):
    section = section.capitalize()

    if section == "Pending" or section == "Running":
        text = f"{model_name} is currently on {section} List"
    elif section == "Finished":
        text = f"{model_name} is currently on Open LLM Leaderboard Finished List"
    else:
        text = f"{model_name} was not found in HuggingFace Space."

    image_links = {"Pending": "https://i.hizliresim.com/1w2vova.png",
                   "Running": "https://i.hizliresim.com/crnac11.png",
                   "Finished": "https://i.hizliresim.com/kidaf5y.png",
                   "Not": "https://cdn-icons-png.flaticon.com/512/4225/4225690.png"}

    toast("Model Not Found" if section == "Not" else section + "List", text, icon=image_links[section], on_click='https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HuggingFace Model Notification Script")
    parser.add_argument('--models', nargs='+', required=True, help="List of model names separated by spaces")
    parser.add_argument('--wait', type=int, default=60, help="Time interval in seconds between checks")

    args = parser.parse_args()
    models = args.models
    how_much_wait = args.wait
    while True:     
        data = get_json_format_data()

        for model in models:
            if model in get_datas('pending', data):
                notifi("Pending", model)
            elif model in get_datas('finished', data):
                notifi("Finished", model)
            elif model in get_datas('running', data):
                notifi("Running", model)
            else:
                notifi("Not", model)
        time.sleep(how_much_wait)
