import requests
import json

IPX800 = 'http://192.168.1.200'
apikey = ""
virtual_input_index_blanc = 3
virtual_input_index_rouge = 4

# Function to retrieve the code of the day from the API
def get_code_of_the_day():
    url = "https://www.api-couleur-tempo.fr/api"
    try:
        response = requests.get(url+'/jourTempo/tomorrow')
        data = response.json()
        code_of_the_day = int(data['codeJour'])
        return code_of_the_day
    except Exception as e:
        print("Error occurred while retrieving code of the day:", e)
        return None

# Function to set virtual input in IPX800
def set_virtual_input(state:bool , index):

    if state:
        status = "SetVI"
    else:
        status = "Clear"

    ipx800_url = IPX800+"/api/xdevices.json?key="+apikey+"&"+status+"="+str(index)

    try:
        response = requests.get(ipx800_url)
        if response.status_code == 200:
            print("Virtual input", index, " set to:", state)
        else:
            print("Failed to set virtual input")
    except Exception as e:
        print("Error occurred while setting virtual input:", e)

# Main function
        

def main():
    code_of_the_day = get_code_of_the_day()
    if code_of_the_day is not None:
        if code_of_the_day == 2:
            set_virtual_input(1, virtual_input_index_blanc)
            set_virtual_input(0, virtual_input_index_rouge)
        elif code_of_the_day == 3:
            set_virtual_input(0, virtual_input_index_blanc)
            set_virtual_input(1, virtual_input_index_rouge)
        else:
            set_virtual_input(0, virtual_input_index_blanc)
            set_virtual_input(0, virtual_input_index_rouge)


if __name__ == "__main__":
    main()
