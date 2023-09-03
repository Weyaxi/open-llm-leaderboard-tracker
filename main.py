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


def get_datas(which_one, data, base_index):
    data_components_map = {
        'pending': {'component_index': base_index+17, 'pattern': r'<a[^>]*>(.*?)</a>', "zero_or_one": 0},
        'running': {'component_index': base_index+14, 'pattern': r'<a[^>]*>(.*?)</a>', "zero_or_one": 0},
        'finished': {'component_index': base_index, 'pattern': r'href="([^"]*)"', "zero_or_one": 1}
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

    image_links = {"Pending": "https://raw.githubusercontent.com/Weyaxi/open_llm_leaderboard_tracker/main/images/pending.jpeg",
                   "Running": "https://raw.githubusercontent.com/Weyaxi/open_llm_leaderboard_tracker/main/images/running.jpeg",
                   "Finished": "https://raw.githubusercontent.com/Weyaxi/open_llm_leaderboard_tracker/main/images/finished.jpeg",
                   "Not": "https://raw.githubusercontent.com/Weyaxi/open_llm_leaderboard_tracker/main/images/not_found.png"}

    toast("Model Not Found" if section == "Not" else section + "List", text, icon=image_links[section], on_click='https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard')


def find_base_index(data):
    for i in range(17, 50):
        try:
            get_datas("finished", data, i)
            return i
        except KeyError:
            continue
    raise ValueError("Base index not found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HuggingFace Model Notification Script")
    parser.add_argument('--models', nargs='+', required=True, help="List of model names separated by spaces")
    parser.add_argument('--wait', type=int, default=60, help="Time interval in seconds between checks")

    args = parser.parse_args()
    models = args.models
    how_much_wait = args.wait
    while True:
        data = get_json_format_data() 
        base_index = find_base_index(data)

        for model in models:
            try:

                finished_models = get_datas('finished', data, base_index)
                running_models = get_datas('running', data, base_index)
                pending_models = get_datas('pending', data, base_index)

                if model in finished_models:
                    notifi("Finished", model)
                elif model in running_models:
                    notifi("Running", model)
                elif model in pending_models:
                    notifi("Pending", model)
                else:
                    notifi("Not", model)
            except ValueError as e:
                print(f"Error: {e}") 

        time.sleep(how_much_wait)
