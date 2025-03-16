import re, sys
from typing import Callable


def parse_log_line(line: str) -> dict:
    
    topics = line.split()
    logs_dict = {topics[2]: \
            str(re.sub(r"\sINFO\s|\sDEBUG\s|\sWARNING\s|\sERROR\s", ' - ', line))}
    
    return logs_dict

def load_logs(file_path: str, func: Callable[[str], dict]) -> list:

    with open(file_path, 'r') as file:
        return [func(string.strip()) for string in file.readlines()]

def count_logs_by_level(logs: list) -> dict:

    count_topic = dict()


    count_topic.update({"INFO": len(list(filter(lambda log_string: "INFO" in log_string, logs)))})
    count_topic.update({"ERROR": len(list(filter(lambda log_string: "ERROR" in log_string, logs)))})
    count_topic.update({"DEBUG": len(list(filter(lambda log_string: "DEBUG" in log_string, logs)))})
    count_topic.update({"WARNING": len(list(filter(lambda log_string: "WARNING" in log_string, logs)))})      
    

    return count_topic

def display_log_counts(counts: dict):

    tab_header = "|{:^17}|{:^10}|".format("Logging level", "Count")
    separator = "-"*len(tab_header)
    body = ""

    for k, v in counts.items():
        body += "|{:<17}|{:<10}|\n".format(k, v)

    print("\n".join([tab_header, separator, body]))

    return None



def  main():

    file_path = sys.argv[1]

    if not file_path.endswith(".log"):
        print("Incorrect file extension")
        return None

    else:
        logs_list = load_logs(file_path, parse_log_line)

        count_logs = count_logs_by_level(logs_list)
        
        display_log_counts(count_logs)

        command = sys.argv[2].upper()

        if command not in count_logs:
            print("Invalid command")
            return None
        
        for string_log in logs_list:

            if command in string_log:
                print(string_log.get(command))
                
            else:
                continue
                

if __name__ == "__main__":

    try:
       
       main()

    except FileNotFoundError:
        print("File not found")

    except IndexError:
        pass


