# HuggingFace Open LLM Leaderboard Tracker

The HuggingFace Open LLM Leaderboard Tracker is a Python script that provides notifications for models listed in the Open LLM Leaderboard pending, running, or finished list. It periodically checks the leaderboard website and sends desktop notifications with relevant information about the model's status.

## Getting Started

### Prerequisites
To run the script, you need to have the following installed on your system:

- Python 3
- Liblaries from `requirements.txt`

### Usage

1. Clone the repository.

```bash
git clone https://github.com/Weyaxi/open-llm-leaderboard-tracker
```
   
2. Open a terminal or command prompt and navigate to the directory containing the script.

```bash
cd open-llm-leaderboard-tracker
```

3. Install the required Python packages using pip3:

```bash
pip3 install -r requirements.txt
```

4. Run the script with the following command:

```bash
python3 main.py --models "<model1>" "<model2>" --wait <seconds>
```

Replace `<model1>`, `<model2>` etc. with the names of the models you want to track, separated by spaces. The `--wait` option allows you to set the time interval (in seconds) between checks. The default interval is 60 seconds.

For example, to track models `"user/model1"` and `"user/model2"` every `120` seconds, you would run:

```bash
python3 main.py --models "user/model1" "user/model2" --wait 120
```

### Notifications

The script will check the Open LLM Leaderboard website for the status of the specified models (pending, running, or finished) and display desktop notifications accordingly.

## Screenshots

![image](https://github.com/Weyaxi/open-llm-leaderboard-tracker/assets/81961593/32f063b8-2b43-4517-9ccf-efe6f95b0af2)

![image](https://github.com/Weyaxi/open_llm_leaderboard_tracker/assets/81961593/817be87a-e257-41c7-a86c-cfcba235aec5)

![image](https://github.com/Weyaxi/open_llm_leaderboard_tracker/assets/81961593/85af5e70-08a3-4803-99cb-7b0df663842d)

![image](https://github.com/Weyaxi/open-llm-leaderboard-tracker/assets/81961593/1905eae6-d5c2-4c29-8323-5728f4d968c2)

## Acknowledgments

The script utilizes `bs4` and `requests` libraries to scrape data from the HuggingFace Open LLM Leaderboard website. After that `json` liblary helps process the scraped data.

It also uses the `win11toast` library to display desktop notifications on Windows.

## Disclaimer

This project is not affiliated with HuggingFace It is a community project created by me. 
