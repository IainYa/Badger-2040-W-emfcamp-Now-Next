import urllib.request, json 

# This builds the static schedule file, for non-W versions of the Badger 2040, and as a backup for Badger-W without WiFi access
# Run:
#   python3 make_static_schedule.py

output_filepath = "../code/schedule/static-schedule.json"

try:
    # Nothing on the main stages yet for 2024.json, so we'll use 2022.json and cross fingers for the same format :)
    with urllib.request.urlopen("https://www.emfcamp.org/schedule/2024.json") as url:
        data_out = []
        match_venues = ["Stage A", "Stage B", "Stage C"]
        schedule = json.load(url)
        for event in schedule:
            if event['venue'] in match_venues:
                data_out.append({
                    'venue': event['venue'],
                    'start_date': event['start_date'],
                    'end_date': event['end_date'],
                    'title': event['title'],
                    'speaker': event['speaker'],
                    'description': event['description'][0:255]            
                })
        data_out = sorted(data_out, key=lambda k: k['start_date'])
        with open(output_filepath, 'w') as file_out:
            json.dump(data_out, file_out)

        print("Successfully built schedule file!")
        
except BaseException as e:
    print("*** ERROR: Failed to build schedule file.")
    print("Error: ", e)
    exit(1)
