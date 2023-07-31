# HuggingFace Open LLM Leaderboard Tracker

The HuggingFace Open LLM Leaderboard Tracker is a Python script that provides notifications for models listed in the Open LLM Leaderboard pending, running, or finished list. It periodically checks the leaderboard website and sends desktop notifications with relevant information about the model's status.

## Getting Started

### Prerequisites
To run the script, you need to have the following installed on your system:

- Python 3
- requirements.txt

You can install the required Python packages using pip3:

```bash
pip3 install –r requirements.txt
```

### Usage

1. Clone the repository.
   
2. Open a terminal or command prompt and navigate to the directory containing the script.

```bash
cd open_llm_leaderboard_tracker
```

3. Run the script with the following command:

```bash
python3 main.py --models "<model1>" "<model2>" --wait <seconds>
```

Replace `<model1>`, `<model2>` etc. with the names of the models you want to track, separated by spaces. The `--wait` option allows you to set the time interval (in seconds) between checks. The default interval is 60 seconds.

For example, to track models `"user/model1"` and `"user/model2"` every 120 seconds, you would run:

```bash
python huggingface_llm_tracker.py --models "user/model1" "user/model2" --wait 120
```

### Notifications

The script will check the Open Law LLM Leaderboard website for the status of the specified models (pending, running, or finished) and display desktop notifications accordingly.

If a model is pending or running, you will receive a notification stating that the model is currently on the pending or running list.

If a model is finished, you will receive a notification stating that the model is on the Open LLM Leaderboard finished list.

If a model is not found on any list, you will receive a notification indicating that the model was not found in the HuggingFace Space.

## Screenshots

![image](https://github.com/Weyaxi/open_llm_leaderboard_tracker/assets/81961593/85af5e70-08a3-4803-99cb-7b0df663842d)

![image](https://github.com/Weyaxi/open_llm_leaderboard_tracker/assets/81961593/8e9b0c50-9a3b-4075-9d8a-1863d17e3c0f)

![image](https://github.com/Weyaxi/open_llm_leaderboard_tracker/assets/81961593/57c0f9e6-ea2f-49f7-bc6e-1cd91da3b9bc)

![image](https://github.com/Weyaxi/open_llm_leaderboard_tracker/assets/81961593/817be87a-e257-41c7-a86c-cfcba235aec5)


## Acknowledgments

The script utilizes BeautifulSoup and requests libraries to scrape data from the HuggingFace Open LLM Leaderboard website.

It also uses the `win11toast` library to display desktop notifications on Windows.

## Disclaimer

This project is not affiliated with HuggingFace It is a community project created by me. 
